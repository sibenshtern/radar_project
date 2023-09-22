from typing import Optional

from utils import Coordinates, Maneuver


class AerialObject:

    def __init__(self):
        self.name: str = ""

        self.speed: int = 0
        self.acceleration: int = 0
        self.trajectory: list[Coordinates] = []

        self.current_maneuver: Optional[Maneuver] = Maneuver()

    def make_maneuver(self, maneuver: Maneuver):
        pass

    def __setattr__(self, key, value):
        if key == "speed" and value < 0:
            raise Exception("speed can not be negative")
        elif key == "trajectory" and not all((isinstance(x, Coordinates) for x in value)):
            raise Exception("trajectory must contain only Coordinates type")
        elif key == "current_maneuver" and not isinstance(value, Maneuver):
            raise Exception("current_maneuver must have Maneuver type")
        else:
            self.__dict__[key] = value


if __name__ == '__main__':
    ao = AerialObject()
    ao.speed = 4

