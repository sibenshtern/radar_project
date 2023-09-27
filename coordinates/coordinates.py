from .vectors import Vector, Vector3D


class Coordinates(Vector):
    pass


class Coordinates3D(Coordinates, Vector3D):

    def __abs__(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"Coordinates3D(x: {self.x}, y: {self.y}, z: {self.z})"

    def __repr__(self) -> str:
        return f"Coordinates3D({self.x}, {self.y}, {self.z})"
