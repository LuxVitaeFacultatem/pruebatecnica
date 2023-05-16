class Payment:
    def __init__(self, amount_in_cents=None,customer_email=None, reference=None, payment_source_id=None) -> None:
        self.amount_in_cents = amount_in_cents
        self.customer_email = customer_email
        self.reference = reference
        self.payment_source_id = payment_source_id

    def to_JSON(self):
        return {

            "amount_in_cents": self.amount_in_cents,  # Monto en centavos
            "currency": "COP",  # Moneda
            "customer_email": str(self.customer_email),  # Email del usuario
            "payment_method": {
                # Número de cuotas si la fuente de pago representa una tarjeta de lo contrario el campo payment_method puede ser ignorado.
                "installments": 1
            },
            "reference": str(self.reference),  # Referencia única de pago
            "payment_source_id": self.payment_source_id,  # ID de la fuente de pago (obligatorio)
            "recurrent": True  # Recurrente
        }
