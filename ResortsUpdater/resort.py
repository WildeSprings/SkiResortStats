class ResortActiveRecord:

    def __init__(self, resort_name, snow_overnight, snow_24hrs, snow_48hrs,
                 snow_72hrs, snow_7days, snow_30days, snow_total,
                 snow_base_depth, lifts_open, lifts_total, trails_open,
                 trails_total, country, region, passes):
        self.resort_name = resort_name
        self.snow_overnight = snow_overnight
        self.snow_24hrs = snow_24hrs
        self.snow_48hrs = snow_48hrs
        self.snow_72hrs = snow_72hrs
        self.snow_7days = snow_7days
        self.snow_30days = snow_30days
        self.snow_total = snow_total
        self.snow_base_depth = snow_base_depth
        self.lifts_open = lifts_open
        self.lifts_total = lifts_total
        self.trails_open = trails_open
        self.trails_total = trails_total
        self.country = country
        self.region = region
        self.passes = passes
