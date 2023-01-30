import requests, json

from . import resort

RESORT_NAME = "Eldora Ski Resort"
COUNTRY = "USA"
REGION = "Colorado"
PASSES = "Ikon"
RESERVATION = False


def GetData():
    url = "https://api.eldora.com/api/v1/dor/conditions"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
    }
    req = requests.get(url, headers=headers)
    req_json = json.loads(req.text)
    # Lift Info
    lifts_total = req_json['liftReport']['total']
    lifts_open = req_json['liftReport']['open']

    # Trail Info
    trails_total = req_json['trailReport']['total']
    trails_open = req_json['trailReport']['open']

    # Snow Info
    snow_overnight = -1
    snow_24hrs = -1
    snow_48hrs = -1
    snow_72hrs = -1
    snow_7days = -1
    snow_30days = -1
    snow_total = -1
    snow_base_depth = -1
    for item in req_json['snowReport'][0]['items']:
        if item["duration"] == "overnight":
            snow_overnight = item['amount']
        elif item["duration"] == "24 Hours":
            snow_24hrs = item['amount']
        elif item["duration"] == "48 Hours":
            snow_48hrs = item['amount']
        elif item["duration"] == "72 Hours":
            snow_72hrs = item['amount']
        elif item["duration"] == "7 days":
            snow_7days = item['amount']
        elif item["duration"] == "30 days":
            snow_30days = item['amount']
        elif item["duration"] == "total":
            snow_total = item['amount']
        elif item["duration"] == "base-depth":
            snow_base_depth = item['amount']
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, snow_7days,
                                     snow_30days, snow_total, snow_base_depth,
                                     lifts_open, lifts_total, trails_open,
                                     trails_total, COUNTRY, REGION, PASSES, RESERVATION)
