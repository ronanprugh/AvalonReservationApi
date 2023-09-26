from enum import Enum

class Amenity(Enum):
    BASKETBALL = 1
    PLAYROOM = 2
    RACQUETBALL = 3
    TENNIS_1 = 4
    TENNIS_2 = 5

    amenityMap = {
        "Basketball": BASKETBALL,
        "Playroom": PLAYROOM,
        "Tennis1": TENNIS_1,
        "Tennis2": TENNIS_2
    }
