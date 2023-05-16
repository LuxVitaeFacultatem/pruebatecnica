# utils
from utils.DateFunctions import Date
from utils.DistanceCalculate import DistanceCalculate

def to_cents(number):
    number = str(number)
    parts = number.split('.')
    if len(parts) == 2:
        decimals = parts[1][:2]
        return int(parts[0] + decimals)
    else:
        return int(number)


class CalculatePrice:
    @classmethod
    def calculate(self, ride):
        
        base_fee = 3500
        total_distance = DistanceCalculate.distanceCalculate(ride["origin_lat_long"], ride["arrive_lat_long"])
        elapsed_time = Date.time_Calculate(ride["creation_date"], ride["finish_date"])
        total_price = (base_fee + (total_distance * 1000) + (elapsed_time * 200))
        
        return to_cents(total_price)
    