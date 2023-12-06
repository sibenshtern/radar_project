from .vectors import Vector, Vector3D, VectorGCS, VectorLECS


class Coordinates(Vector):
    pass


class Coordinates3D(Coordinates, Vector3D):

    def __str__(self) -> str:
        return f"Coordinates3D(x: {self.x:.3f}, y: {self.y:.3f}, z: {self.z:.3f})"

    def __repr__(self) -> str:
        return f"Coordinates3D({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"


class CoordinatesGCS(Coordinates, VectorGCS):

    def __str__(self) -> str:
        return f"CoordinatesGCS(x: {self.x}, y: {self.y}, z: {self.z})"

    def __repr__(self) -> str:
        return f"CoordinatesGCS({self.x}, {self.y}, {self.z})"


class CoordinatesLECS(Coordinates, VectorLECS):

    def __str__(self) -> str:
        return (f"CoordinatesLEGS(longitude: {self.longitude}, "
                f"latitude: {self.latitude}, height: {self.height})")

    def __repr__(self) -> str:
        return (f"CoordinatesLEGS({self.longitude}, {self.latitude}, "
                f"{self.height})")
