import requests, json
from bs4 import BeautifulSoup

from . import resort

def GetData(RESORT_NAME, WEBSITE, COUNTRY, REGION, PASSES, RESERVATION):

    snow_overnight = None
    snow_24hrs = None
    snow_48hrs = None
    snow_72hrs = None
    snow_7days = None
    snow_30days = None
    snow_total = None
    snow_base_depth = None

    lifts_open = None
    lifts_total = None
    trails_open = None
    trails_total = None

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    snow_url = "https://{web}/the-mountain/mountain-conditions/snow-and-weather-report.aspx".format(web=WEBSITE)
    terrain_url = "https://{web}/the-mountain/mountain-conditions/terrain-and-lift-status.aspx".format(web=WEBSITE)

    soup = BeautifulSoup(requests.get(snow_url).text, "html.parser")

    scripts = soup.find_all("script", {"type" : "module"})

    for script in scripts:

        txt = script.get_text().strip()
        if "FR.snowReportSettings" == txt[:len("FR.snowReportSettings")]:
            index = txt.find("FR.snowReportData = ")
            subtxt = txt[index+len("FR.snowReportData = "):]
            index_semicolon = subtxt.find(";")
            jstring = json.loads(subtxt[:index_semicolon])

            snow_overnight = jstring["OvernightSnowfall"]["Inches"]
            snow_24hrs = jstring["TwentyFourHourSnowfall"]["Inches"]
            snow_48hrs = jstring["FortyEightHourSnowfall"]["Inches"]
            snow_72hrs = snow_48hrs
            snow_7days = jstring["SevenDaySnowfall"]["Inches"]
            snow_30days = None
            snow_total = jstring["CurrentSeason"]["Inches"]
            snow_base_depth = jstring["BaseDepth"]["Inches"]

    soup = BeautifulSoup(requests.get(terrain_url).text, "html.parser")

    lift_data = soup.find("div", {"data-terrain-status-id" : "lifts"})

    lift_stats = lift_data.find("div", {"class" : "terrain_summary__circle"})
    lifts_open = lift_stats["data-open"]
    lifts_total = lift_stats["data-total"]

    trail_data = soup.find("div", {"data-terrain-status-id" : "runs"})

    trail_stats = trail_data.find("div", {"class" : "terrain_summary__circle"})
    trails_open = trail_stats["data-open"]
    trails_total = trail_stats["data-total"]


    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, snow_7days, snow_30days,
                                     snow_total, snow_base_depth, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES, RESERVATION)
