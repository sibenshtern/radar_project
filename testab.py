import abfilter
import objects
from coordinates import Coordinates3D

ab = abfilter.ABFilter()


obj = objects.tracked.Tracked(0)
ab.filter(obj, Coordinates3D(1, 1, 1))
ab.filter(obj, Coordinates3D(2, 2, 2))
ab.filter(obj, Coordinates3D(3, 3, 3))


#ab.filter(obj, Coordinates3D(1, 1, 1))
#ab.filter(obj, Coordinates3D(1, 1, 1))
#ab.filter(obj, Coordinates3D(1, 1, 1))

print(obj.extrapolatedValue)

ab.filter(obj, Coordinates3D(4.1, 3.9, 4))

print(obj.trajectory)