from geopy.distance import geodesic

class DistanceCalculate():
    @classmethod
    def distanceCalculate(self, rider_lat_long, driver_lat_long):
        #assign coordinates to variables
        rider_lat_long = eval(rider_lat_long)
        driver_lat_long = eval(driver_lat_long)
        rider_coords = (rider_lat_long[0], rider_lat_long[1])
        driver_coords = (driver_lat_long[0], driver_lat_long[1])
        
        #calculate distance between two points
        distance = geodesic(rider_coords, driver_coords).kilometers
        
        return distance