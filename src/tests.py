import unittest, requests, random

from database.db import get_connection



class TestAPI(unittest.TestCase):

    ENDPOINT_DRIVER = "http://127.0.0.1:5000/api/driver"
    ENDPOINT_RIDER = "http://127.0.0.1:5000/api/rider"
    
    created_ride = None
    ramdon_rider = random.randint(1, 6)
    
    def test_db_connection(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT 1')
            connection.close()
            return print("test 1 / 3 passed")
        except Exception:
            return print("test 1 / 3 failed")
        
    
    def test_create_ride(self):
        try:
            response = requests.post(self.ENDPOINT_RIDER, json={
                    "rider_id": self.ramdon_rider
            })
            
            self.assertEqual(response.status_code, 200)
            response_json = response.json()
            ride_id = response_json['ride_id'][0]
            print(response_json)
            self.created_ride = ride_id
            print("test 2 / 3 passed")
        except Exception:
            return print("test 2 / 3 failed")
    
    def finish_ride(self):
        try:
            response = requests.post(self.ENDPOINT_DRIVER, json={
                    "ride_id": self.created_ride
            })
            
            self.assertEqual(response.status_code, 200)
            print(response.json())
            print("test 3 / 3 passed")
        except Exception:
            return print("test 3 / 3 failed")
        
        
    


if __name__ == '__main__':
    tester = TestAPI()

    tester.test_db_connection()
    tester.test_create_ride()
    tester.finish_ride()
