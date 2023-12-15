import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QStatusBar, QListWidget,
                             QListWidgetItem, QPushButton)
from PyQt5 import uic
from PyQt5.QtCore import QTimer

from ui.window import Window
from modeling.model import AircraftModel
from ui.windows import CreateObjectWindow, SettingsWindow, CenterfoldWindow, \
    ChangeSpeedWindow, ChangeHeightWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.graphic_window = Window(self)
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_all)

        uic.loadUi('ui/main.ui', self)

        self.createObjectButton.clicked.connect(self.create_object_dialog)
        self.stopButton: QPushButton
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stop_simulation)
        self.startButton.clicked.connect(self.start_simulation)
        self.settingButton.clicked.connect(self.open_settings)
        self.centerfoldButton.clicked.connect(self.open_centerfold)
        self.changeSpeedButton.clicked.connect(self.open_change_speed)
        self.changeHeightButton.clicked.connect(self.open_change_height)

        self.aircraft: QListWidget
        self.aircraft.currentItemChanged.connect(self.change_item)

        self.setStatusBar(QStatusBar())
        self.statusBar().setStyleSheet("color: red")

        self.timer.start()

    def change_item(self, previous: QListWidgetItem, current: QListWidgetItem):
        if current is None:
            for obj in self.graphic_window.scene.objects:
                if obj.tex_id == 'selected_aircraft':
                    obj.tex_id = 'aircraft'
        else:
            self.graphic_window.scene.objects[
                int(current.text().split('#')[-1]) - 1].tex_id = 'aircraft'

        self.graphic_window.scene.objects[
            int(previous.text().split('#')[-1]) - 1].tex_id = 'selected_aircraft'
        self.graphic_window.aircraft_index = int(previous.text().split('#')[-1]) - 1

    def open_change_height(self):
        if len(self.graphic_window.scene.objects) == 0:
            self.statusBar().showMessage("Ошибка: Нет объектов")
        else:
            ChangeHeightWindow(self)

    def start_simulation(self):
        self.graphic_window.scene.is_simulation = True
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def stop_simulation(self):
        self.graphic_window.scene.is_simulation = False
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def create_object_dialog(self):
        CreateObjectWindow(self)

    def open_settings(self):
        SettingsWindow(self)

    def open_centerfold(self):
        if len(self.graphic_window.scene.objects) == 0:
            self.statusBar().showMessage("Нет объектов!")
        else:
            CenterfoldWindow(self)

    def open_change_speed(self):
        if len(self.graphic_window.scene.objects) == 0:
            self.statusBar().showMessage("Нет объектов!")
        else:
            ChangeSpeedWindow(self)

    def add_object(self, position, velocity):
        aircraft = AircraftModel(
            self.graphic_window, pos=position, rot=(0, 0, -90),
            scale=(0.2, 0.2, 0.2),
            name=f'aircraft #{len(self.graphic_window.scene.objects)}')
        if len(self.graphic_window.scene.objects) == 0:
            aircraft.tex_id = 'selected_aircraft'
        aircraft.speed.x = velocity[0]
        aircraft.speed.y = velocity[1]
        aircraft.speed.z = velocity[2]
        self.graphic_window.scene.add_object(aircraft)
        self.aircraft: QListWidget

        self.aircraft.addItem(QListWidgetItem(f"Aircraft #{len(self.graphic_window.scene.objects)}"))

    def update_all(self):
        self.graphic_window.get_time()
        self.graphic_window.check_events()

        self.graphic_window.scene.update()
        self.graphic_window.camera.update()
        self.graphic_window.render()
        self.graphic_window.delta_time = self.graphic_window.clock.tick(24)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
