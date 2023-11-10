import matplotlib.pyplot as plt

from objects import Aircraft
from coordinates import Vector3D, Coordinates3D
from modeling import Scene
from radar import Radar

aircraft = Aircraft("helicopter", Coordinates3D(-5, -5, 2),
                    Vector3D(2, 2, 0), Vector3D(0, 0, 0), 1)
radar = Radar()
scene = Scene(radar, [aircraft], [], 5)


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
            pass
            #ax_3d.scatter(*uncompress([scene.trajectories[i][j]]))
        else:
            ax_3d.scatter(*uncompress([scene.trajectories[i][j]]))
ax_3d.set_title("Trajectory")
print(aircraft.get_trajectory())
ax_3d.scatter(*uncompress(aircraft.get_trajectory()), marker='<')
plt.show()
#
# coordinates = uncompress(aircraft.get_trajectory())
# data = {'x': coordinates[0], 'y': coordinates[1], 'z': coordinates[2]}
# data = {'x': [], 'y': [], 'z': []}
#
# print(scene.trajectories)
# print(scene.reflected)
#
# for i in range(scene.duration):
#     for j in range(len(scene.trajectories[i])):
#         if not scene.reflected[i][j]:
#             x, y, z = uncompress([scene.trajectories[i][j]])
#         else:
#             x, y, z = uncompress([scene.trajectories[i][j]])
#
#         data['x'].append(x)
#         data['y'].append(y)
#         data['z'].append(z)
#
# print(len(data['x']))
#
# fig = px.scatter_3d(data, x='x', y='y', z='z')
# fig.show()
