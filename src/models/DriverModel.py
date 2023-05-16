from database.db import get_connection
from .entities.Driver import Driver

class DriverModel() :
        
    @classmethod
    def get_Drivers_state(self, status):
        try:
            connection = get_connection()
            drivers = []
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, lat_long FROM public."Driver" WHERE status= %s', (status,))
                resultset = cursor.fetchall()
                for row in resultset:
                    driver = Driver(row[0],row[1])
                    drivers.append(driver.to_JSON())
            connection.close()
            return drivers
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_Driver(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT id, lat_long, status FROM public."Driver" WHERE id = %s', (id,))
                row = cursor.fetchone()
                
                driver = None
                if row != None:
                    driver = Driver(row[0],row[1], row[2])
                    driver = Driver.to_JSON(driver)
            connection.close()
            return driver
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_DriverStatus(self, driver):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                print(driver.status)
                cursor.execute('UPDATE public."Driver" SET status= %s WHERE id = %s', (driver.status, driver.id,))
                affected_row = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_row
        except Exception as ex:
            raise Exception(ex)
