
import psycopg2
from decouple import config
from datetime import datetime, timezone

from resorts import abasin, copper, eldora, loveland, mtnpowder, vailresorts

def GetResortsData():
    resorts = []
    try:
        resorts.append(abasin.GetData())
    except Exception as e:
        print(e)
    try:
        resorts.append(copper.GetData())
    except Exception as e:
        print(e)
    try:
        resorts.append(eldora.GetData())
    except Exception as e:
        print(e)
    try:
        resorts.append(loveland.GetData())
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Winter Park", "USA", "Colorado", "Ikon", 5, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Stratton", "USA", "New York", "Ikon", 1, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Snowshoe", "USA", "West Virginia", "Ikon", 2, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(mtnpowder.GetData("Tremblant", "Canada", "Quebec", "Ikon", 4, False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Vail", "www.vail.com", "USA", "Colorado", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Breckenridge", "www.breckenridge.com", "USA", "Colorado", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Keystone", "www.keystoneresort.com", "USA", "Colorado", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Beaver Creek", "www.beavercreek.com", "USA", "Colorado", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Heavenly Lake Tahoe", "www.skiheavenly.com", "USA", "California", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Park City", "www.parkcitymountain.com", "USA", "Utah", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Crested Butte", "www.skicb.com", "USA", "Colorado", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("North Star", "www.northstarcalifornia.com", "USA", "California", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Kirkwood", "www.kirkwood.com", "USA", "California", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Stevens Pass", "www.stevenspass.com", "USA", "Washington", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Stowe", "www.stowe.com", "USA", "Vermont", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Okemo", "www.okemo.com", "USA", "Vermont", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Mount Snow", "www.mountsnow.com", "USA", "Vermont", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Hunter", "www.huntermtn.com", "USA", "New York", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Attitash", "www.attitash.com", "USA", "New Hampshire", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Wildcat", "www.skiwildcat.com", "USA", "New Hampshire", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Mount Sunapee", "www.mountsunapee.com", "USA", "New Hampshire", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Crotched", "www.crotchedmtn.com", "USA", "New Hampshire", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Wilmot", "www.wilmotmountain.com", "USA", "Wisconsin", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Afton Alps", "www.aftonalps.com", "USA", "Minnesota", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Mt Brighton", "www.mtbrighton.com", "USA", "Michigan", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Alpine Valley", "www.alpinevalleyohio.com", "USA", "Ohio", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Boston Mills/Brandywine", "www.bmbw.com", "USA", "Ohio", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Mad River", "www.skimadriver.com", "USA", "Ohio", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Hidden Valley", "www.hiddenvalleyski.com", "USA", "Missouri", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Snow Creek", "www.skisnowcreek.com", "USA", "Missouri", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Paoli Peaks", "www.paolipeaks.com", "USA", "Indiana", "Epic", False))
    except Exception as e:
        print(e)
    try:
        resorts.append(vailresorts.GetData("Whistler Blackcomb", "www.whistlerblackcomb.com", "Canada", "British Columbia", "Epic", False))
    except Exception as e:
        print(e)

    return resorts

# resorts_old = [
#     abasin.GetData(),
#     copper.GetData(),
#     eldora.GetData(),
#     loveland.GetData(),
#     mtnpowder.GetData("Winter Park", "USA", "Colorado", "Ikon", 5, False),
#     mtnpowder.GetData("Stratton", "USA", "New York", "Ikon", 1, False),
#     mtnpowder.GetData("Snowshoe", "USA", "West Virginia", "Ikon", 2, False),
#     mtnpowder.GetData("Blue", "Canada", "Ontario", "Ikon", 3, False),
#     mtnpowder.GetData("Tremblant", "Canada", "Quebec", "Ikon", 4, False),
#     vailresorts.GetData("Vail", "www.vail.com", "USA", "Colorado", "Epic", False),
#     vailresorts.GetData("Breckenridge", "www.breckenridge.com", "USA", "Colorado", "Epic", False),
#     vailresorts.GetData("Keystone", "www.keystoneresort.com", "USA", "Colorado", "Epic", False),
#     vailresorts.GetData("Beaver Creek", "www.beavercreek.com", "USA", "Colorado", "Epic", False),
#     vailresorts.GetData("Heavenly Lake Tahoe", "www.skiheavenly.com", "USA", "California", "Epic", False),
#     vailresorts.GetData("Park City", "www.parkcitymountain.com", "USA", "Utah", "Epic", False),
#     vailresorts.GetData("Crested Butte", "www.skicb.com", "USA", "Colorado", "Epic", False),
#     vailresorts.GetData("North Star", "www.northstarcalifornia.com", "USA", "California", "Epic", False),
#     vailresorts.GetData("Kirkwood", "www.kirkwood.com", "USA", "California", "Epic", False),
#     vailresorts.GetData("Stevens Pass", "www.stevenspass.com", "USA", "Washington", "Epic", False),
#     vailresorts.GetData("Stowe", "www.stowe.com", "USA", "Vermont", "Epic", False),
#     vailresorts.GetData("Okemo", "www.okemo.com", "USA", "Vermont", "Epic", False),
#     vailresorts.GetData("Mount Snow", "www.mountsnow.com", "USA", "Vermont", "Epic", False),
#     vailresorts.GetData("Hunter", "www.huntermtn.com", "USA", "New York", "Epic", False),
#     vailresorts.GetData("Attitash", "www.attitash.com", "USA", "New Hampshire", "Epic", False),
#     vailresorts.GetData("Wildcat", "www.skiwildcat.com", "USA", "New Hampshire", "Epic", False),
#     vailresorts.GetData("Mount Sunapee", "www.mountsunapee.com", "USA", "New Hampshire", "Epic", False),
#     vailresorts.GetData("Crotched", "www.crotchedmtn.com", "USA", "New Hampshire", "Epic", False),
#     vailresorts.GetData("Wilmot", "www.wilmotmountain.com", "USA", "Wisconsin", "Epic", False),
#     vailresorts.GetData("Afton Alps", "www.aftonalps.com", "USA", "Minnesota", "Epic", False),
#     vailresorts.GetData("Mt Brighton", "www.mtbrighton.com", "USA", "Michigan", "Epic", False),
#     vailresorts.GetData("Alpine Valley", "www.alpinevalleyohio.com", "USA", "Ohio", "Epic", False),
#     vailresorts.GetData("Boston Mills/Brandywine", "www.bmbw.com", "USA", "Ohio", "Epic", False),
#     vailresorts.GetData("Mad River", "www.skimadriver.com", "USA", "Ohio", "Epic", False),
#     vailresorts.GetData("Hidden Valley", "www.hiddenvalleyski.com", "USA", "Missouri", "Epic", False),
#     vailresorts.GetData("Snow Creek", "www.skisnowcreek.com", "USA", "Missouri", "Epic", False),
#     vailresorts.GetData("Paoli Peaks", "www.paolipeaks.com", "USA", "Indiana", "Epic", False),
#     vailresorts.GetData("Whistler Blackcomb", "www.whistlerblackcomb.com", "Canada", "British Columbia", "Epic", False),
# ]

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
