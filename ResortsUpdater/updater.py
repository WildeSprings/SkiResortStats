import psycopg2
from decouple import config

from resorts import copper, eldora, loveland

resorts = [
    copper.GetData(),
    eldora.GetData(),
    loveland.GetData(),
]

if __name__ == "__main__":
    conn = psycopg2.connect(database="skidb",
                            user=config("DB_USER"),
                            password=config("DB_PASSWORD"),
                            host="127.0.0.1",
                            port="5432")
    cursor = conn.cursor()
    for resort in resorts:
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
                        trails_open = %s
                    WHERE resort_name = %s"""
        cursor.execute(
            sql, (resort.snow_overnight, resort.snow_24hrs, resort.snow_48hrs,
                  resort.snow_72hrs, resort.snow_7days, resort.snow_30days,
                  resort.snow_total, resort.snow_base_depth, resort.lifts_open,
                  resort.trails_open, resort.resort_name))
        if (cursor.rowcount != 0):
            print("%s updated" % (resort.resort_name))
        else:
            # ADD THE RECORD
            print("%s not found..." % (resort.resort_name))
            add_sql = """ INSERT INTO resorts_activerecord (resort_name, snow_overnight, snow_24hrs, snow_48hrs, snow_72hrs, snow_7days, snow_30days, snow_total, snow_base_depth, lifts_open, lifts_total, trails_open, trails_total, country, region, passes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (resort.resort_name, resort.snow_overnight, resort.snow_24hrs, resort.snow_48hrs, resort.snow_72hrs, resort.snow_7days, resort.snow_30days, resort.snow_total, resort.snow_base_depth, resort.lifts_open, resort.lifts_total, resort.trails_open, resort.trails_total, resort.country, resort.region, resort.passes)
            cursor.execute(add_sql, record_to_insert)
            if (cursor.rowcount != 0):
                print("%s added to table" % (resort.resort_name))
    conn.commit()
    cursor.close()
    if conn is not None:
        conn.close()
    print("Done")
