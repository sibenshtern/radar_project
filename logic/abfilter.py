from coordinates import Coordinates
from objects import Tracked


# class for alpha beta filter

class ABFilter:
    def __init__(self, kmax=10):
        self.t = 1  # 1 condition unit
        self.kmax = kmax

    # change filteredValue(add obj.trajectory[-1]), filteredVelocity, extrapolatedValue, extrapolatedVelocity
    def filterAB(self, obj: Tracked, position: Coordinates, time: int):

        k = len(obj.trajectory)
        if k == 0:
            obj.trajectory.append(position)
            return
        if k == 1 or k == 2:  # initialization
            obj.filteredVelocityAB = (position - obj.trajectory[-1]) / (time - obj.last_tracked_time)
            obj.trajectory.append(position)

            obj.extrapolatedValueAB = position + (obj.filteredVelocityAB * self.t)
            obj.extrapolatedVelocityAB = obj.filteredVelocityAB
            return

        if k > self.kmax:
            obj.trajectory.pop(0)

        alpha = 2 * (2 * k - 1) / (k * (k + 1))
        beta = 6 / (k * (k + 1))

        obj.trajectory.append(obj.extrapolatedValueAB + (
                    alpha * (position - obj.extrapolatedValueAB)))
        obj.filteredVelocityAB = obj.extrapolatedVelocityAB + (
                    beta / (time - obj.last_tracked_time) * (position - obj.extrapolatedValueAB))

        obj.extrapolatedValueAB = obj.trajectory[-1] + (
                    obj.filteredVelocityAB * (time - obj.last_tracked_time))
        obj.extrapolatedVelocityAB = obj.filteredVelocityAB

    def filter(self, obj: Tracked, position: Coordinates, time : int):
        obj.extrapolatedVelocityAB = (obj.trajectory[-1]-position) / (time - obj.last_tracked_time)
        obj.extrapolatedValueAB = position + obj.extrapolatedVelocityAB


