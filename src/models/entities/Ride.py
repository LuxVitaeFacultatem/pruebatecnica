from utils.DateFunctions import Date

def try_apply_Date(date):
    try:
        return Date.convert_date(date)
    except:
        return date

class Ride:

    def __init__(self, id, rider=None, driver=None, origin_lat_long=None, arrive_lat_long=None, state=None, creation_date=None, finish_date=None, total_price=None) -> None:
        self.id = id
        self.rider = rider
        self.driver = driver
        self.origin_lat_long = origin_lat_long
        self.arrive_lat_long = arrive_lat_long
        self.state = state
        self.creation_date = creation_date
        self.finish_date = finish_date
        self.total_price = total_price

    def to_JSON(self):
        return {
            "id": self.id,
            "rider": self.rider,
            "driver": self.driver,
            "origin_lat_long": self.origin_lat_long,
            "arrive_lat_long": self.arrive_lat_long,
            "state": self.state,
            "creation_date": try_apply_Date(self.creation_date),
            "finish_date": try_apply_Date(self.finish_date),
            "total_price": self.total_price
        }
     

