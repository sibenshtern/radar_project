from typing import Optional


class Coordinates:

    def __sub__(self, other):
        pass

    def __abs__(self):
        pass


class CartesianCoordinates(Coordinates):
    pass


class Maneuver:
    pass


class Centerfold(Maneuver):
    pass


class ChangeSpeed(Maneuver):
    pass


class ChangeHeight(Maneuver):
    pass
