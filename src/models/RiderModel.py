from database.db import get_connection

#entities
from .entities.Rider import Rider

class RiderModel() :

    @classmethod
    def get_Rider(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, lat_long, payment_source_id, mail FROM public."Rider" WHERE id = %s', (id,))
                row = cursor.fetchone()
                
                rider = None
                if row != None:
                    rider = Rider(row[0],row[1], row[2], row[3])
                    rider = Rider.to_JSON(rider)
            connection.close()
            return rider
        except Exception as ex:
            raise Exception(ex)
