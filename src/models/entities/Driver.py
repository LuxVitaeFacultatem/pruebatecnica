class Driver:

    def __init__(self, id, lat_long=None, status = None) -> None:
        self.id = id
        self.lat_long = lat_long
        self.status = status

    def to_JSON(self):
        return {
            "id": self.id,
            "lat_long": self.lat_long,
            "status": self.status
        }
