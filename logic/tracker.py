from typing import TypeVar
import math

from cluster.mean_shift import MeanShift
import matplotlib.pyplot as plt

from objects import Tracked
from coordinates.coordinates import Coordinates3D, CoordinatesGCS
from logic.radar import Signal

C = TypeVar('C', Coordinates3D, CoordinatesGCS)

EPSILON = 1
REQUIRED_MINIMUM_TIME = 3 * 24
STOP_TRACKING_TIME = 10 * 24

PULSE_POWER_OF_EMITTED_SIGNAL = 150000  # w
TRANSMITTING_ANTENNA_GAINS = 40
RECEIVING_ANTENNA_GAINS = 40
WAVELENGTH = 0.035  # meters
EPR_TARGET = 10  # meters ^ 2
TOTAL_LOSS_FACTOR = 1.5 * 1.5 * 1
RECEIVER_NOISE_FACTOR = 5  # decibel
BOLTZMANN_CONSTANT = 1.38 * (10 ** -23)
STANDARD_TEMPERATURE = 290


class Tracker:

    def __init__(self):
        self.objects: list[Tracked] = []
        self.archive_objects: list[Tracked] = []

    def calculate_coordinate(self, signals: list[Signal], time) -> list[C]:
        coordinates: list[C] = []

        for signal in signals:
            r = (signal.init_power * 2 * math.pi / signal.power) ** (1 / 4)
            if self.get_signal_noise(signal, r, time) > 13:
                coordinates.append(-signal.speed * r)

        return coordinates

    def process_signals(self, signals: list[Signal], current_time: int):
        coordinates: list[C] = self.calculate_coordinate(signals, current_time)

        ms = MeanShift()
        mean_shift_result = ms.cluster(coordinates, kernel_bandwidth=1)

        calculated = []
        for point in mean_shift_result.shifted_points:
            coordinate = Coordinates3D(point[0], point[1], point[2])
            calculated.append(coordinate)
            for obj in self.objects:
                if abs(obj.trajectory[-1] - coordinate) < EPSILON:
                    obj.trajectory.append(coordinate)
                    obj.last_tracked_time = current_time
                    break
            else:
                self.objects.append(Tracked(current_time))
                self.objects[-1].trajectory.append(coordinate)

        self.update_objects(current_time)
        return coordinates

    def update_objects(self, current_time: int):
        for obj in self.objects:
            if current_time - obj.last_tracked_time < STOP_TRACKING_TIME:
                continue

            if obj.tracked_time >= REQUIRED_MINIMUM_TIME:
                self.archive_objects.append(obj)
            self.objects.remove(obj)

    # get signal noise ratio
    def get_signal_noise(self, signal: Signal, radius: int, time: int):
        return 2 * PULSE_POWER_OF_EMITTED_SIGNAL * time * \
            TRANSMITTING_ANTENNA_GAINS * RECEIVING_ANTENNA_GAINS * \
            (WAVELENGTH ** 2) * EPR_TARGET * TOTAL_LOSS_FACTOR / \
            (((4 * math.pi) ** 3) * radius ** 4 * RECEIVER_NOISE_FACTOR *
             BOLTZMANN_CONSTANT * STANDARD_TEMPERATURE)

# if len(mean_shift_result.original_points):
        #     original_points = mean_shift_result.original_points
        #     shifted_points = mean_shift_result.shifted_points
        #     cluster_assignments = mean_shift_result.cluster_ids
        #
        #     x = original_points[:, 0]
        #     y = original_points[:, 1]
        #     z = original_points[:, 2]
        #     Cluster = cluster_assignments
        #     centers = shifted_points
        #
        #     print(x, y, z, centers)
        #
        #     fig = plt.figure()
        #     ax = fig.add_subplot(projection='3d')
        #     scatter = ax.scatter(x, y, z, c=Cluster, s=50)
        #     for i, j, k in centers:
        #         ax.scatter(i, j, k, s=50, c='red', marker='+')
        #     plt.colorbar(scatter)
        #     plt.show()