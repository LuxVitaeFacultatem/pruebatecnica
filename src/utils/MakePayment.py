import requests
from flask import jsonify

#entities
from models.entities.Payment import Payment
class PaymentModel:
    @classmethod
    def make_Payment(self, content):
        # Datos que deseas enviar en la solicitud POST
        body = Payment.to_JSON(content)
        
        # URL de la API
        url = 'https://sandbox.wompi.co/v1/transactions'
        
        # Encabezados de la solicitud
        headers = {
            'Authorization': 'Bearer prv_test_pUyxGIZpZPDGSCLgt2V18Eu3iCa59Hbb'
        }
        
        # Hacer la solicitud POST con el encabezado de autorización
        response = requests.post(url, headers=headers, json=body )
        
        # Obtener la respuesta de la API
        response_data = response.json()
        
        # Procesar la respuesta y devolverla como JSON
        return jsonify(response_data)