import matplotlib.pyplot as plt

from objects import Aircraft
from coordinates import Vector3D, Coordinates3D
from modeling import Scene
from radar import Radar

obj = Aircraft("helicopter", Coordinates3D(50, 0, 0),
               Vector3D(0, 0, 0), Vector3D(0, 0, 0))

scene = Scene(Radar(), [obj], list(), 3)

for i in range(scene.duration):
    scene.update()


def uncompress(data):
    x = []
    y = []
    z = []
    for i in range(len(data)):
        x.append(data[i].x)
        y.append(data[i].y)
        z.append(data[i].z)
    return x, y, z


fig1 = plt.figure(1, figsize=(3, 3), dpi=500)
ax_3d = fig1.add_subplot(projection='3d')

for i in range(scene.duration):
    for j in range(len(scene.trajectories[i])):
        if not scene.reflected[i][j]:
            ax_3d.scatter(*uncompress([scene.trajectories[i][j]]))
        else:
            ax_3d.scatter(*uncompress([scene.trajectories[i][j]]))
ax_3d.set_title("Trajectory")

plt.show()
