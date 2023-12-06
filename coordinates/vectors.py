import math

from typing import Union


class Vector:

    def __init__(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __abs__(self):
        pass

    def __mul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Vector3D(Vector):

    def __init__(self, x, y, z):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return self / abs(self)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __rsub__(self, other):
        return Vector3D(other.x - self.x, other.y - self.y, other.z - self.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __mul__(self, other: Union[int, float, tuple, 'Vector3D']):
        if isinstance(other, tuple):
            other = Vector3D(other[0], other[1], other[2])
        if isinstance(other, Vector3D):
            return Vector3D(self.x * other.x, self.y * other.y,
                            self.z * other.z)
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: Union[int, float]):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __rmul__(self, other: Union[int, float]):
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float]):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __div__(self, other: Union[int, float]):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __idiv__(self, other: Union[int, float]):
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __iter__(self):
        for coordinate in (self.x, self.y, self.z):
            yield coordinate

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self) -> str:
        return f"Vector3D(x: {self.x:.3f}, y: {self.y:.3f}, z: {self.z:.3f})"

    def __repr__(self) -> str:
        return f"Vector3D({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"


class VectorGCS(Vector3D):

    def __init__(self, x: float, y: float, z: float):
        super().__init__(x * Vector3D(1, 0, 0),
                         y * Vector3D(0, 1, 0),
                         z * Vector3D(0, 0, 1))

    def __str__(self) -> str:
        return (f"VectorGCS(x: {str(self.x)}, y: {str(self.y)}, "
                f"z: {str(self.z)})")

    def __repr__(self) -> str:
        result = self.x + self.y + self.z
        return f"VectorGCS({result.x}, {result.y}, {result.z})"


class VectorLECS(Vector):

    def __init__(self, longitude: float, latitude: float, height: float):
        super().__init__()
        if not (-180 < longitude <= 180 and -90 < latitude <= 90):
            raise ValueError("Wrong values of longitude and latitude.")

        self.longitude: float = longitude
        self.latitude: float = latitude
        self.height: float = height
