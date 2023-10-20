from typing import Union
from copy import deepcopy

import matplotlib.pyplot as plt

import objects.aircraft as aircraft
import objects.maneuvers as maneuvers
from coordinates import Vector3D, Coordinates3D, Coordinates, Vector

Aircraft = aircraft.Aircraft
ChangeHeight = maneuvers.ChangeHeight
ChangeSpeed = maneuvers.ChangeSpeed


def uncompress(data: list[Union[Vector, Coordinates]]) -> \
        tuple[list, list, list]:
    data: list[Union[Vector3D, Coordinates3D]]

    x = []
    y = []
    z = []
    for i in range(len(data)):
        x.append(data[i].x)
        y.append(data[i].y)
        z.append(data[i].z)

    return x, y, z


obj = Aircraft("helicopter", Coordinates3D(0, 0, 0),
               Vector3D(1, 1, 0), Vector3D(0, 0, 0))
change_speed = ChangeSpeed(10, obj, Vector3D(10, 10, 0))
change_height = ChangeHeight(10, obj, 15)
centerfold = maneuvers.CenterFold(60, obj)

speeds = [deepcopy(obj.speed)]
accelerations = [deepcopy(obj.acceleration)]

CHANGE_SPEED_TIME = 5
CHANGE_HEIGHT_TIME = 10
CENTERFOLD_TIME = 25

DURATION = 100

for time in range(DURATION):
    obj.update()
    speeds.append(deepcopy(obj.speed))
    accelerations.append(deepcopy(obj.acceleration))

    # if time == CHANGE_SPEED_TIME:
    #     object.make_maneuver(change_speed)
    # if time == CHANGE_HEIGHT_TIME:
    #     object.make_maneuver(change_height)
    if time == CENTERFOLD_TIME:
        obj.make_maneuver(centerfold)

fig1 = plt.figure(1, figsize=(3, 3), dpi=500)
ax_3d = fig1.add_subplot(projection='3d')

fig2 = plt.figure(2, figsize=(3, 3), dpi=500)
ax_speed = fig2.add_subplot()

fig3 = plt.figure(3, figsize=(3, 3), dpi=500)
ax_acceleration = fig3.add_subplot()

ax_speed.plot(range(DURATION + 1), [abs(x) for x in speeds])
ax_speed.set_title("Speed")

ax_acceleration.plot(range(DURATION + 1), [abs(x) for x in accelerations])
ax_acceleration.set_title("Acceleration")

ax_3d.plot(*uncompress(obj.get_trajectory()))
ax_3d.set_title("Trajectory")

plt.show()

print("Speeds:", speeds)
print("Accelerations:", accelerations)
print("Trajectory:", obj.get_trajectory())
