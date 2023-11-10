from objects import Tracked
from coordinates import Coordinates

class ABFilter:
     def __init__(self, kmin = 5, kmax = 10):
        self.t = 1  # 1 condition unit


    def filter(self, obj:Tracked, position:Coordinates):

        k = len(obj.trajectory)
        if k == 1:
            obj.trajectory.append(position)
            return
        if k < self.kmin: # initialization
            self.filteredVelocity = (position - self.filteredValue) / self.t
            obj.trajectory.append(position)

            self.extrapolatedValue = position + (self.filteredVelocity * self.t)
            self.extrapolatedVelocity = self.filteredVelocity
            return

        if k > self.kmax:
            obj.trajectory.pop(0)

        alpha = 2 * (2 * k - 1) / (k * (k +1))
        beta = 6 / (k * (k + 1))

        obj.trajectory.append(self.extrapolatedValue + (alpha * (position - self.extrapolatedValue)))
        self.filteredVelocity = self.extrapolatedVelocity + (beta / self.t * (position - self.extrapolatedValue))

        self.extrapolatedValue = obj.trajectory[-1] + (self.filteredVelocity * self.t)
        self.extrapolatedVelocity = self.filteredVelocity

