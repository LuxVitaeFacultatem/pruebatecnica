from database.db import get_connection

#entities
from models.entities.Ride import Ride

class RideModel() :
    
    @classmethod
    def get_Ride(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, rider, driver, origin_lat_long, arrive_lat_long, state, creation_date, finish_date, total_price FROM public."Ride" WHERE id = %s', (id,))
                row = cursor.fetchone()
                ride = None
                if row != None:
                    ride = Ride(row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    ride = Ride.to_JSON(ride)
            connection.close()
            return ride
        except Exception as ex:
            raise Exception(ex)

    

    @classmethod
    def update_Ride(self, ride):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('UPDATE public."Ride" SET arrive_lat_long = %s, state = %s , finish_date = %s, total_price = %s WHERE id = %s', (ride.arrive_lat_long, ride.state, ride.finish_date, ride.total_price, ride.id))
                affected_row = cursor.rowcount
                updated_id = cursor.lastrowid
                connection.commit()
                
            connection.close()
            return affected_row, updated_id
        except Exception as ex:
            raise Exception(ex)
            

    @classmethod
    def create_Ride(self, ride):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO public."Ride" (rider, driver, origin_lat_long, arrive_lat_long, state, creation_date, finish_date, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id',
                    (ride.rider, ride.driver, ride.origin_lat_long, ride.arrive_lat_long, ride.state, ride.creation_date, ride.finish_date, ride.total_price,))
                insert_id = cursor.fetchone()
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_row, insert_id
        except Exception as ex:
            raise Exception(ex)
