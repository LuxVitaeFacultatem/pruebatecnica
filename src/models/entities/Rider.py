class Rider:

    def __init__(self, id, lat_long=None, payment_source_id=None, mail=None) -> None:
        self.id = id
        self.lat_long = lat_long
        self.payment_source_id = payment_source_id
        self.mail = mail
    def to_JSON(self):
        return {
            "id": self.id,
            "lat_long": self.lat_long,
            "payment_source_id": self.payment_source_id,
            "mail": self.mail
        }
