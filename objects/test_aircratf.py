if __name__ == "__main__":
    from typing import Union
    from copy import deepcopy

    import matplotlib.pyplot as plt

    from aircraft import Aircraft, ChangeSpeed, ChangeHeight
    from coordinates import Vector3D, Coordinates3D, Coordinates, Vector
    from modeling import Scene
    from radar import Radar

    obj = Aircraft("helicopter", Coordinates3D(50, 0, 0),
                   Vector3D(0, 0, 0), 5, Vector3D(0, 0, 0))

    scene = Scene(Radar(), [obj], list(), 100)

    for i in range(scene.duration):
        scene.update()
        print("-", end="")
