import math

from typing import Union


class Vector:

    def __init__(self):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
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

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __rdiv__(self, other):
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

    def __mul__(self, other: Union[int, float]):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: Union[int, float]):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __truediv__(self, other: Union[int, float]):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __div__(self, other: Union[int, float]):
        return Vector3D(self.x / other, self.y / other, self.z / other)

    def __idiv__(self, other: Union[int, float]):
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __str__(self) -> str:
        return f"Vector3D(x: {self.x}, y: {self.y}, z: {self.z})"

    def __repr__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"
