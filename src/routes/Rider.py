from utils.DateFunctions import Date
from utils.DistanceCalculate import DistanceCalculate
from flask import blueprints, jsonify, request

# models
from models.RiderModel import RiderModel
from models.RideModel import RideModel
from models.DriverModel import DriverModel

# entities
from models.entities.Ride import Ride
from models.entities.Driver import Driver

main = blueprints.Blueprint('rider_blueprint', __name__)

@main.route('/rider', methods=['POST'])
def rider():
    try:
        # service creation date
        creation_date = Date.get_date()
        
        # resolve request data "rider_id"
        rider_id = int(request.json["rider_id"])
        
        # get rider information id and lat_long
        rider_information = RiderModel.get_Rider(rider_id)
        
        # if rider_id not found comprobation
        if rider_information == None:
            return jsonify({'error': 'User id not found or does not exist'}), 500
        
        # create a driver blank object
        assigned_driver_id = {
            "id": None,
            "lat_long": None
        }
        
        # get all available drivers
        drivers = DriverModel.get_Drivers_state("available")
        
        # declare best distance as None for comparison
        best_distance = None
        
        # iterate through drivers to find the best driver
        for driver in drivers:
            # call the distance calculate function from utils
            distance = DistanceCalculate.distanceCalculate(rider_information["lat_long"], driver["lat_long"])
            
            # if the best distance is None or the distance is better, update assigned_driver_id
            if best_distance is None or distance < best_distance:
                assigned_driver_id["id"] = driver["id"]
                assigned_driver_id["lat_long"] = driver["lat_long"]
                best_distance = distance
        
        # create an instance of the assigned driver
        assigned_driver = Driver(assigned_driver_id["id"], assigned_driver_id["lat_long"], "occupied")
        
        # update the driver status to "occupied"
        DriverModel.update_DriverStatus(assigned_driver)
        
        # create a new ride instance
        ride = Ride(None, rider_id, assigned_driver_id["id"], rider_information["lat_long"], None, "progress", creation_date, None, None)
        
        # create the ride and get the affected rows and ride_id
        affected_rows, ride_id = RideModel.create_Ride(ride)
        
        if affected_rows == 1:
            return jsonify({
                'message': 'Ride created successfully',
                'assigned_driver': assigned_driver_id,
                'ride_id': ride_id
            })
        else:
            return jsonify({'error': 'Error on insert'}), 500
        
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
