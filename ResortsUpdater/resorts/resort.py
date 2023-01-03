class ResortActiveRecord:

    def __init__(self, resort_name, snow_overnight, snow_24hrs, snow_48hrs,
                 snow_72hrs, snow_7days, snow_30days, snow_total,
                 snow_base_depth, lifts_open, lifts_total, trails_open,
                 trails_total, country, region, passes, reservation_required):
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
        self.reservation_required = reservation_required
    def __str__(self):
        return """%s
                  snow_overnight: %s
                  snow_24hrs: %s
                  snow_48hrs: %s
                  snow_72hrs: %s
                  snow_7days: %s
                  snow_30days: %s
                  snow_total: %s
                  snow_base_depth: %s
                  lifts_open: %s
                  lifts_total: %s
                  trails_open: %s
                  trails_total: %s
                  country: %s
                  region: %s
                  passes: %s
                  reservation_required: %s""" % (self.resort_name,
                                   self.snow_overnight,
                                   self.snow_24hrs,
                                   self.snow_48hrs,
                                   self.snow_72hrs,
                                   self.snow_7days,
                                   self.snow_30days,
                                   self.snow_total,
                                   self.snow_base_depth,
                                   self.lifts_open,
                                   self.lifts_total,
                                   self.trails_open,
                                   self.trails_total,
                                   self.country,
                                   self.region,
                                   self.passes,
                                   self.reservation_required)
