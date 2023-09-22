import radar
import aerial_object
import signal

import datetime




class Scene:
    def __init__(self, radar: Radar, objects : list[AerialObject], signals: list[Signal]):
        self.radar = Radar
        self.objects: list = objects
        self.signals: list = signals

    def update(self):
        signal = self.radar.emitter.send_signal(0, self.convert_time(now.time()), , )

        angle: int, departure_time: int, direction: Coordinates,
                 speed: Coordinates

    def convert_time(time):
        pass