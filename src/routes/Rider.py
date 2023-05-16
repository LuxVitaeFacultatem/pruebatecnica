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
            return jsonify({'error': 'User id not found or not exist'}), 500

        # create a driver blank objec
        assigned_driver_id = {
            "id": None,
            "lat_long": None
        }

        # get all drivers available
        drivers = DriverModel.get_Drivers_state("available")

        # declare best distance in None for compare
        best_distance = None

        # iterate drivers for find the best driver
        for driver in drivers:
            # call distance calculate function from utils
            distance = DistanceCalculate.distanceCalculate(
                rider_information["lat_long"], driver["lat_long"])
            # if found best distance update assigned_driver_id
            if best_distance is None or distance < best_distance:
                assigned_driver_id["id"] = driver["id"]
                assigned_driver_id["lat_long"] = driver["lat_long"]
                best_distance = distance
        
        assigned_driver = Driver(assigned_driver_id["id"], assigned_driver_id["lat_long"], "occupied")
        
        DriverModel.update_DriverStatus(assigned_driver)

        ride = Ride(None, rider_id, assigned_driver_id["id"], rider_information["lat_long"],
                     None, "progress", creation_date, None, None)

        affected_rows, ride_id = RideModel.create_Ride(ride)

        if affected_rows == 1:
            return jsonify({
                'message': 'Ride created successfully',
                'assigned_driver': assigned_driver_id,
                'ride_id': ride_id
            })
        else:
            return jsonify({'error': 'Error on insert'}), 500
        # return the confirmation of created ride, assigned_driver_id and position, and created ride_id

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
