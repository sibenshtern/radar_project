if __name__ == "__main__":
    from typing import Union
    from copy import deepcopy

    import matplotlib.pyplot as plt

    from aircraft import Aircraft, ChangeSpeed, ChangeHeight
    from coordinates import Vector3D, Coordinates3D, Coordinates, Vector
    from modeling import Scene
    from radar import Radar

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


    obj = Aircraft("helicopter", Coordinates3D(50, 0, 0),
                   Vector3D(0, 0, 0), Vector3D(0, 0, 0))

    speeds = [deepcopy(obj.speed)]
    accelerations = [deepcopy(obj.acceleration)]

    scene = Scene(Radar(), [obj], list(), 100)

    for i in range(scene.duration):
        scene.update()
        print("-")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, subplot_kw={"projection": "3d"})
    ax1.scatter(*uncompress(speeds))
    ax1.set_title("Speed")

    ax2.scatter(*uncompress(accelerations))
    ax2.set_title("Acceleration")

    ax3.scatter(*uncompress(obj.get_trajectory()))
    ax3.set_title("Trajectory")

    plt.show()

    print(speeds)
    print(accelerations)
    print(obj.get_trajectory())
