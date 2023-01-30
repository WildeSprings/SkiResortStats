import requests, json
from bs4 import BeautifulSoup

from . import resort

def GetData(RESORT_NAME, COUNTRY, REGION, PASSES, RESORT_NUM, RESERVATION, FLAG=False):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    url = "https://mtnpowder.com/feed?resortId={num}".format(num=RESORT_NUM)

    json_resp = json.loads(requests.get(url).content)

    snow_report = json_resp["SnowReport"]
    lifts_open = snow_report["TotalOpenLifts"] if snow_report["TotalOpenLifts"] != "--" else -1
    lifts_total = snow_report["TotalLifts"] if snow_report["TotalLifts"] != "--" else -1
    trails_open = snow_report["TotalOpenTrails"] if snow_report["TotalOpenTrails"] != "--" else -1
    trails_total = snow_report["TotalTrails"] if snow_report["TotalTrails"] != "--" else -1

    
    section_name = "BaseArea"
    if FLAG: 
        section_name = "MidMountainArea"

    snow_stats = snow_report[section_name]
    snow_overnight = snow_stats["SinceLiftsClosedIn"] if snow_stats["SinceLiftsClosedIn"] != "--" else -1
    snow_24hrs = snow_stats["Last24HoursIn"] if snow_stats["Last24HoursIn"] != "--" else -1
    snow_48hrs = snow_stats["Last48HoursIn"] if snow_stats["Last48HoursIn"] != "--" else -1
    snow_72hrs = snow_stats["Last72HoursIn"] if snow_stats["Last72HoursIn"] != "--" else -1
    snow_7days = snow_stats["Last7DaysIn"] if snow_stats["Last7DaysIn"] != "--" else -1
    snow_30days = -1
    snow_total = snow_report["SeasonTotalIn"] if snow_report["SeasonTotalIn"] != "--" else -1
    snow_base_depth = snow_stats["BaseIn"] if snow_stats["BaseIn"] != "--" else -1
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, -1, -1,
                                     snow_total, snow_base_depth, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES, RESERVATION)
