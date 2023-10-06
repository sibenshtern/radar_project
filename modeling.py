import radar
import aerial_object
import signal

import datetime




class Scene:
    def __init__(self, radar: Radar, objects : list[AerialObject], signals: list[Signal], duration: int):
        self.radar = Radar
        self.objects: list = objects
        self.signals: list = signals
        self.time: int = 0
        self.duration: int = duration

    send_signal(self, angle: int, departure_time: int, direction: Coordinates,
                 speed: Coordinates):

    def update(self):
        self.time += 1
        signal = self.radar.emitter.send_signal(0, self.time, , )

        angle: int, departure_time: int, direction: Coordinates,
                 speed: Coordinates

    def convert_time(time):
        pass