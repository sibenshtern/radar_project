import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QTimer

from ui.window import Window
from modeling.model import AircraftModel


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.graphic_window = Window()
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_all)

        self.button = QPushButton("Create object")
        self.button.clicked.connect(self.add_object)
        self.setCentralWidget(self.button)

        self.timer.start()

    def add_object(self):
        self.graphic_window.scene.add_object(
            AircraftModel(self.graphic_window, pos=(5, 0, 10), rot=(-90, 180, 0),
                          scale=(0.05, 0.05, 0.05),
                          name=f'aircraft #{self.graphic_window.aircraft_index}')
        )
        self.graphic_window.aircraft_index += 1

    def update_all(self):
        self.graphic_window.get_time()
        self.graphic_window.check_events()

        for obj in self.graphic_window.scene.objects:
            obj.update()

        self.graphic_window.camera.update()
        self.graphic_window.render()
        self.graphic_window.delta_time = self.graphic_window.clock.tick(24)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
