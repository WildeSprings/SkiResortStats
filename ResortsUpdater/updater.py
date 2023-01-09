import psycopg2
from decouple import config
from datetime import datetime, timezone

from resorts import abasin, copper, eldora, loveland, mtnpowder, vailresorts

def GetResortsData():
    resorts = []
    try:
        resorts.append(abasin.GetData())
    except Exeception as e:
        print(e)
    try:
        resorts.append(copper.GetData())
    except Exeception as e:
        print(e)
    try:
        resorts.append(eldora.GetData())
    except Exeception as e:
        print(e)
    try:
        resorts.append(loveland.GetData())
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Winter Park", "USA", "Colorado", "Ikon", 5, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Stratton", "USA", "New York", "Ikon", 1, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Snowshoe", "USA", "West Virginia", "Ikon", 2, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Tremblant", "Canada", "Quebec", "Ikon", 4, False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Vail", "www.vail.com", "USA", "Colorado", "Epic", False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Breckenridge", "www.breckenridge.com", "USA", "Colorado", "Epic", False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Keystone", "www.keystoneresort.com", "USA", "Colorado", "Epic", False))
    except Exeception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Beaver Creek", "www.beavercreek.com", "USA", "Colorado", "Epic", False))
    except Exeception as e:
        print(e)
    return resorts

resorts_old = [
    abasin.GetData(),
    copper.GetData(),
    eldora.GetData(),
    loveland.GetData(),
    mtnpowder.GetData("Winter Park", "USA", "Colorado", "Ikon", 5, False),
    mtnpowder.GetData("Stratton", "USA", "New York", "Ikon", 1, False),
    mtnpowder.GetData("Snowshoe", "USA", "West Virginia", "Ikon", 2, False),
    mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False),
    mtnpowder.GetData("Tremblant", "Canada", "Quebec", "Ikon", 4, False),
    vailresorts.GetData("Vail", "www.vail.com", "USA", "Colorado", "Epic", False),
    vailresorts.GetData("Breckenridge", "www.breckenridge.com", "USA", "Colorado", "Epic", False),
    vailresorts.GetData("Keystone", "www.keystoneresort.com", "USA", "Colorado", "Epic", False),
    vailresorts.GetData("Beaver Creek", "www.beavercreek.com", "USA", "Colorado", "Epic", False),
]

if __name__ == "__main__":
    conn = psycopg2.connect(database="skidb",
                            user=config("DB_USER"),
                            password=config("DB_PASSWORD"),
                            host="127.0.0.1",
                            port="5432")
    cursor = conn.cursor()
    dt = datetime.now(timezone.utc)
    resorts = GetResortsData()
    for resort in resorts:
        try:
            sql = """ UPDATE resorts_activerecord
                        SET snow_overnight = %s,
                            snow_24hrs = %s,
                            snow_48hrs = %s,
                            snow_72hrs = %s,
                            snow_7days = %s,
                            snow_30days = %s,
                            snow_total = %s,
                            snow_base_depth = %s,
                            lifts_open = %s,
                            lifts_total = %s,
                            trails_open = %s,
                            trails_total = %s,
                            country = %s,
                            region = %s,
                            passes = %s,
                            reservation = %s,
                            last_updated = %s
                        WHERE resort_name = %s"""
            cursor.execute(
                sql, (resort.snow_overnight, resort.snow_24hrs, resort.snow_48hrs,
                      resort.snow_72hrs, resort.snow_7days, resort.snow_30days,
                      resort.snow_total, resort.snow_base_depth, resort.lifts_open,
                      resort.lifts_total, resort.trails_open, resort.trails_total,
                      resort.country, resort.region, resort.passes, resort.reservation_required,
                      dt, resort.resort_name))
            if (cursor.rowcount != 0):
                print("%s updated, stats below" % (resort.resort_name))
                print(resort)
            else:
                # ADD THE RECORD
                print("%s not found..." % (resort.resort_name))
                add_sql = """ INSERT INTO resorts_activerecord (resort_name, snow_overnight, snow_24hrs, snow_48hrs, snow_72hrs, snow_7days, snow_30days, snow_total, snow_base_depth, lifts_open, lifts_total, trails_open, trails_total, country, region, passes, last_updated, reservation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                record_to_insert = (resort.resort_name, resort.snow_overnight,
                                    resort.snow_24hrs, resort.snow_48hrs,
                                    resort.snow_72hrs, resort.snow_7days,
                                    resort.snow_30days, resort.snow_total,
                                    resort.snow_base_depth, resort.lifts_open,
                                    resort.lifts_total, resort.trails_open,
                                    resort.trails_total, resort.country,
                                    resort.region, resort.passes, dt,
                                    resort.reservation_required)
                cursor.execute(add_sql, record_to_insert)
                if (cursor.rowcount != 0):
                    print("%s added to table, stats below" % (resort.resort_name))
                    print(resort)
        except:
            print("%s had an error" % (resort.resort_name))

    conn.commit()
    cursor.close()
    if conn is not None:
        conn.close()
    print("Done")
