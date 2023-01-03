import requests
from bs4 import BeautifulSoup

from . import resort

RESORT_NAME = "Loveland Ski Area"
COUNTRY = "USA"
REGION = "Colorado"
PASSES = "Powder Alliance"
RESERVATION = False


def GetData():
    url = "https://skiloveland.com/snow-report/"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    if (page.status_code != 200):
        print("Loveland site returned %s" % page.status_code)
        return None
    soup = BeautifulSoup(page.content, 'html.parser')
    table5am = soup.find('table', class_="report-5am")
    table8am = soup.find('table', class_="report-8am")
    tableOtherInfo = soup.find('tr', class_="other-information")
    snow_overnight = float(
        soup.find('span', id="report-5-12-hour").get_text().replace('"', ''))
    snow_24hrs = float(
        soup.find('span', id='report-5-24-hour').get_text().replace('"', ''))
    snow_48hrs = float(
        table5am.findAll('tr')[1].findAll('td')[3].find(
            'h1').get_text().replace('"', ''))
    snow_72hrs = float(
        table5am.findAll('tr')[1].findAll('td')[4].find(
            'h1').get_text().replace('"', ''))
    snow_total = float(
        table8am.findAll('tr')[1].findAll('td')[4].find(
            'h1').get_text().replace('"', ''))
    lifts_open = int(tableOtherInfo.findAll('td')[2].find('h1').get_text())
    lifts_total = int(
        tableOtherInfo.findAll('td')[2].find('h5').get_text().split()[1])
    trails_open = int(tableOtherInfo.findAll('td')[3].find('h1').get_text())
    trails_total = int(
        tableOtherInfo.findAll('td')[3].find('h5').get_text().split()[1])
    return resort.ResortActiveRecord(RESORT_NAME, snow_overnight, snow_24hrs,
                                     snow_48hrs, snow_72hrs, None, None,
                                     snow_total, None, lifts_open, lifts_total,
                                     trails_open, trails_total, COUNTRY,
                                     REGION, PASSES, RESERVATION)


if __name__ == "__main__":
    print(GetData())
