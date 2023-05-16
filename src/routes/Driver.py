from flask import blueprints, jsonify, request

# models
from models.RideModel import RideModel
from models.DriverModel import DriverModel
from models.RiderModel import RiderModel

# utils
from utils.DateFunctions import Date
from utils.CalculatePrice import CalculatePrice
from utils.MakePayment import PaymentModel

# entities
from models.entities.Driver import Driver
from models.entities.Ride import Ride
from models.entities.Payment import Payment

main = blueprints.Blueprint('driver_blueprint', __name__)


@main.route('/driver', methods=['POST'])
def driver():
    try:
        ride_id = int(request.json["ride_id"])
        ride = RideModel.get_Ride(ride_id)
        rider_information = RiderModel.get_Rider(ride["rider"])
        if ride == None:
            return jsonify({'error': 'ride id not found or not exist'}), 500
        driver = DriverModel.get_Driver(ride["driver"])
        if driver == None:
            return jsonify({'error': 'driver id not found or not exist'}), 500
        driver["state"] = "available"
        ride["state"] = "complete"
        ride["arrive_lat_long"] = driver["lat_long"]
        ride["finish_date"] = Date.get_date()
        price = CalculatePrice.calculate(ride)
        ride["total_price"] = price  
        driver = Driver(driver["id"], driver["lat_long"], driver["state"])
        ride = Ride(ride["id"], ride["rider"], ride["driver"], ride["origin_lat_long"], ride["arrive_lat_long"],
           ride["state"], ride["creation_date"], ride["finish_date"], ride["total_price"])
        try:
            payment_information = Payment(
                price, rider_information["mail"], ride.id, rider_information["payment_source_id"])
            payment = PaymentModel.make_Payment(
                payment_information)
            DriverModel.update_DriverStatus(driver)
            RideModel.update_Ride(ride)
            return jsonify({"message": "ride complete successfully",
                            "ride": Ride.to_JSON(ride),
                            "payment": str(payment.status)}), 200
        except Exception as ex:
            return jsonify({"message": "ride complete successfully",
                            "ride": Ride.to_JSON(ride),
                            "payment": str(ex)}), 500

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
