import requests, json
from bs4 import BeautifulSoup

from . import resort

def GetData(RESORT_NAME, COUNTRY, REGION, PASSES, RESORT_NUM, RESERVATION):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    url = "https://mtnpowder.com/feed?resortId={num}".format(num=RESORT_NUM)

    json_resp = json.loads(requests.get(url).content)

    snow_report = json_resp["SnowReport"]
    lifts_open = snow_report["TotalOpenLifts"] if snow_report["TotalOpenLifts"] != "--" else None
    lifts_total = snow_report["TotalLifts"] if snow_report["TotalLifts"] != "--" else None
    trails_open = snow_report["TotalOpenTrails"] if snow_report["TotalOpenTrails"] != "--" else None
    trails_total = snow_report["TotalTrails"] if snow_report["TotalTrails"] != "--" else None

    snow_stats = snow_report["BaseArea"] if snow_report["BaseArea"] != "--" else None
    snow_overnight = snow_stats["SinceLiftsClosedIn"] if snow_report["SinceLiftsClosedIn"] != "--" else None
    snow_24hrs = snow_stats["Last24HoursIn"] if snow_report["Last24HoursIn"] != "--" else None
    snow_48hrs = snow_stats["Last48HoursIn"] if snow_report["Last48HoursIn"] != "--" else None
    snow_72hrs = snow_stats["Last72HoursIn"] if snow_report["Last72HoursIn"] != "--" else None
    snow_7days = snow_stats["Last7DaysIn"] if snow_report["Last7DaysIn"] != "--" else None
    snow_30days = None
    snow_total = snow_report["SeasonTotalIn"] if snow_report["SeasonTotalIn"] != "--" else None
    snow_base_depth = snow_stats["BaseIn"] if snow_report["BaseIn"] != "--" else None
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, None, None,
                                     snow_total, snow_base_depth, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES, RESERVATION)



print(GetData("Winter Park", "USA", "Colorado", "Ikon", 5))
print(GetData("Stratton", "USA", "New York", "Ikon", 1))
# GetData("Snowshoe", "USA", "Colorado", "Ikon", 2),
# GetData("Blue", "Canada", "Ontario", "Ikon", 3),
# GetData("Tremblant", "Canada", "Quebec", "Ikon", 4),
