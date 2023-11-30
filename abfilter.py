from objects import Tracked
from coordinates import Coordinates


class ABFilter:
    def __init__(self, kmax=10):
        self.t = 1  # 1 condition unit
        self.kmax = kmax

    def filter(self, obj: Tracked, position: Coordinates):

        k = len(obj.trajectory)
        if k == 0:
            obj.trajectory.append(position)
            return
        if k == 1 or k == 2:  # initialization
            obj.filteredVelocity = (position - obj.trajectory[-1]) / self.t
            obj.trajectory.append(position)

            obj.extrapolatedValue = position + (obj.filteredVelocity * self.t)
            obj.extrapolatedVelocity = obj.filteredVelocity
            return

        if k > self.kmax:
            obj.trajectory.pop(0)

        alpha = 2 * (2 * k - 1) / (k * (k + 1))
        beta = 6 / (k * (k + 1))

        obj.trajectory.append(obj.extrapolatedValue + (
                    alpha * (position - obj.extrapolatedValue)))
        obj.filteredVelocity = obj.extrapolatedVelocity + (
                    beta / self.t * (position - obj.extrapolatedValue))

        obj.extrapolatedValue = obj.trajectory[-1] + (
                    obj.filteredVelocity * self.t)
        obj.extrapolatedVelocity = obj.filteredVelocity
