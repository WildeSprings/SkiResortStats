import requests
from bs4 import BeautifulSoup

from . import resort

RESORT_NAME = "Arapahoe Basin"
COUNTRY = "USA"
REGION = "Colorado"
PASSES = "Ikon"
RESERVATION = False


def GetData():
    terrain_url = "https://www.arapahoebasin.com/the-mountain/terrain-status/"
    snow_url = "https://www.arapahoebasin.com/the-mountain/snow-report/"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    terrain_page = requests.get(terrain_url, headers=headers)
    snow_page = requests.get(snow_url, headers=headers)
    if (terrain_page.status_code != 200):
        print("ABasin terrain site returned %s" % page.status_code)
        return None
    if (snow_page.status_code != 200):
        print("ABasin snow site returned %s" % page.status_code)
        return None
    terrain_soup = BeautifulSoup(terrain_page.content, 'html.parser').findAll('div', class_="ab-condition_value")
    lifts = terrain_soup[7].get_text().replace('\n','').split('/')
    lifts_open = int(lifts[0])
    lifts_total = int(lifts[1])
    trails = terrain_soup[8].get_text().replace('\n','').split('/')
    trails_open = int(trails[0])
    trails_total = int(trails[1])

    snow_soup = BeautifulSoup(snow_page.content, 'html.parser').findAll('div', class_="ab-condition_value")
    snow_overnight = None
    snow_24hrs = None
    try:
        snow_24hrs = float(snow_soup[7].get_text().replace('"',''))
    except Exception as e:
        print("Error getting Abasin 24hrs snow: %s" % (e))
        snow_24hrs = "0"
    snow_48hrs = snow_24hrs # No value
    snow_72hrs = float(snow_soup[8].get_text().replace('"',''))
    snow_7days = None
    snow_30days = None
    snow_total = float(snow_soup[10].get_text().replace('"',''))
    snow_base_depth = float(snow_soup[9].get_text().replace('"',''))
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, None, None,
                                     snow_total, snow_base_depth, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES, RESERVATION)
