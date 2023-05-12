from flask import blueprints, jsonify

main = blueprints.Blueprint('driver_blueprint', __name__)

@main.route('/driver')
def driver():
    return jsonify({'Driver': "Driver"})