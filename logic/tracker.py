import math
from typing import TypeVar

import matplotlib.pyplot as plt

from cluster.mean_shift import MeanShift, MeanShiftResult
from coordinates.coordinates import Coordinates3D, CoordinatesGCS
from logic.abfilter import ABFilter
from logic.radar import Signal
from objects import Tracked

C = TypeVar('C', Coordinates3D, CoordinatesGCS)

EPSILON = 2
REQUIRED_MINIMUM_TIME = 3 * 24
STOP_TRACKING_TIME = 100

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
        self.filter = ABFilter()
        self.mean_shift = MeanShift()

    def calculate_coordinate(self, signals: list[Signal], time) -> list[C]:
        coordinates: list[C] = []

        for signal in signals:
            r = (signal.init_power / signal.power) ** (1 / 4)

            if self.get_signal_noise(signal, r, time) > 13:
                coordinates.append(-signal.speed * r)

        return coordinates

    def __calculate_real_coordinates(self, signals: list[Signal], time) \
            -> list[C]:
        coordinates: list[C] = []

        for signal in signals:
            r = abs(signal.direction)

            if self.get_signal_noise(signal, r, time) > 13:
                coordinates.append(signal.direction)

        return coordinates

    @staticmethod
    def calculate_cluster_centers(result: MeanShiftResult) -> list:
        clusters = {}
        clusters_count = {}
        for i in range(len(result.shifted_points)):
            if result.cluster_ids[i] not in clusters:
                clusters[result.cluster_ids[i]] = result.shifted_points[i]
                clusters_count[result.cluster_ids[i]] = 1
            else:
                clusters[result.cluster_ids[i]] += result.shifted_points[i]
                clusters_count[result.cluster_ids[i]] += 1

        for cluster in clusters.keys():
            clusters[cluster] /= clusters_count[cluster]

        aircraft = []
        for key in clusters.keys():
            aircraft.append(clusters[key])

        return aircraft

    def process_signals(self, signals: list[Signal], current_time: int):
        coordinates: list[C] = self.calculate_coordinate(signals, current_time)

        aircraft = self.calculate_cluster_centers(
            self.mean_shift.cluster(coordinates, kernel_bandwidth=1))

        calculated = []
        for i, plane in enumerate(aircraft):
            coordinate = Coordinates3D(plane[0], plane[1], plane[2])
            for obj in self.objects:
                if abs(obj.trajectory[-1] - coordinate) < EPSILON:
                    obj.mse += abs(coordinate - obj.extrapolatedValueAB) ** 2
                    self.filter.filterAB(obj, coordinate, current_time + 1)
                    calculated.append(obj.trajectory[-1])
                    obj.last_tracked_time = current_time
                    break
            else:
                self.objects.append(Tracked(current_time))
                self.filter.filterAB(self.objects[-1], coordinate, current_time)

        self.update_objects(current_time)
        return calculated

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

    @staticmethod
    def show_clusters(self, result, current_time):
        if len(result.original_points):
            original_points = result.original_points
            shifted_points = result.shifted_points
            cluster_assignments = result.cluster_ids

            x = original_points[:, 0]
            y = original_points[:, 1]
            z = original_points[:, 2]
            Cluster = cluster_assignments
            centers = shifted_points

            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            scatter = ax.scatter(x, y, z, c=Cluster, s=50)
            for i, j, k in centers:
                ax.scatter(i, j, k, s=50, c='red', marker='+')
            plt.colorbar(scatter)
            fig.savefig(f"log/image_{current_time}.jpg")

