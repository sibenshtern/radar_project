from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox
from PyQt5 import uic


def is_digit(line):
    if len(line) == 0:
        return False

    if line[0] != '-' and not line[0].isdigit():
        return False

    for symbol in line[1:]:
        if symbol != '.' and not symbol.isdigit():
            return False
    return True


class CreateObjectWindow(QMainWindow):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent: QMainWindow = parent
        self.widget = QWidget(self)
        uic.loadUi('ui/createObject.ui', self.widget)
        self.setCentralWidget(self.widget)

        self.widget.confirm_object.clicked.connect(self.create_object)
        self.show()

    def create_object(self):
        coordinate_edits = [
            self.widget.coordinateXLineEdit.text(),
            self.widget.coordinateYLineEdit.text(),
            self.widget.coordinateZLineEdit.text()
        ]

        velocity_edits = [
            self.widget.velocityXLineEdit.text(),
            self.widget.velocityYLineEdit.text(),
            self.widget.velocityZLineEdit.text()
        ]

        for i, axis in enumerate(['X', 'Y', 'Z']):
            if not is_digit(coordinate_edits[i]):
                self.parent.statusBar().showMessage(
                    f"Координата {axis} не число!")
                self.close()
            if not is_digit(velocity_edits[i]):
                self.parent.statusBar().showMessage(
                    f"Скорость по {axis} не число!")
                self.close()

        if float(coordinate_edits[2]) < 5:
            self.parent.statusBar().showMessage(
                "Координата Z не может быть меньше 5")
            self.close()

        coordinates = tuple(map(float, coordinate_edits))
        velocities = tuple(map(float, velocity_edits))

        self.parent.add_object(coordinates, velocities)
        self.close()


class SettingsWindow(QMainWindow):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.widget = QWidget(self)
        uic.loadUi('ui/settings.ui', self.widget)
        self.setCentralWidget(self.widget)

        self.widget.confirm_button.clicked.connect(self.save_settings)
        self.widget.close_button.clicked.connect(self.close_settings)

        self.widget.showSignal.setChecked(
            self.parent.graphic_window.scene.show_signals)
        self.widget.showTrajectory.setChecked(
            self.parent.graphic_window.scene.show_trajectories)
        self.show()

    def save_settings(self):
        self.widget.showSignal: QCheckBox
        self.widget.showTrajectory: QCheckBox
        self.widget.showPredictTrajectory: QCheckBox

        self.parent.graphic_window.scene.show_signals = self.widget.showSignal.isChecked()
        self.parent.graphic_window.scene.show_trajectories = self.widget.showTrajectory.isChecked()
        self.parent.graphic_window.scene.show_predicted = self.widget.showPredictTrajectory.isChecked()
        self.close()

    def close_settings(self):
        self.close()


class CenterfoldWindow(QMainWindow):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.widget = QWidget(self)
        uic.loadUi('ui/centerfold.ui', self.widget)
        self.setCentralWidget(self.widget)
        self.widget.confirm_button.clicked.connect(self.make_maneuver)
        self.show()

    def make_maneuver(self):
        duration_s = self.widget.durationLineEdit.text()

        if len(self.parent.graphic_window.scene.objects) == 0:
            self.parent.statusBar().showMessage("Нет текущего объекта!")
            self.close()

        if not is_digit(duration_s):
            self.parent.statusBar().showMessage(
                "Длительность разворота не число!")
        else:
            duration = float(duration_s)
            if duration < 10:
                self.parent.statusBar().showMessage(
                    "Длительность разворота не может быть меньше 10!")
                self.close()

            self.parent.graphic_window.scene.objects[
                self.parent.graphic_window.aircraft_index].centerfold(
                duration * 24)
        self.close()


class ChangeSpeedWindow(QMainWindow):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.widget = QWidget(self)
        uic.loadUi('ui/changeSpeed.ui', self.widget)
        self.setCentralWidget(self.widget)
        self.widget.confirm_button.clicked.connect(self.make_maneuver)
        self.show()

    def make_maneuver(self):
        velocity_edits = [
            self.widget.velocityXLineEdit.text(),
            self.widget.velocityYLineEdit.text(),
            self.widget.velocityZLineEdit.text()
        ]

        for i, axis in enumerate(['X', 'Y', 'Z']):
            if not is_digit(velocity_edits[i]):
                self.parent.statusBar().showMessage(
                    f"Скорость по {axis} не число!")
                self.close()

        velocity = tuple(map(float, velocity_edits))

        duration_s = self.widget.durationLineEdit.text()

        if not is_digit(duration_s):
            self.parent.statusBar().showMessage(
                "Длительность разворота не число!")
        else:
            duration = float(duration_s)
            if duration < 10:
                self.parent.statusBar().showMessage(
                    "Длительность разворота не может быть меньше 10!")
                self.close()

            self.parent.graphic_window.scene.objects[
                self.parent.graphic_window.aircraft_index].change_speed(
                duration * 24, velocity)

        self.close()


class ChangeHeightWindow(QMainWindow):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.widget = QWidget(self)
        uic.loadUi('ui/changeHeight.ui', self.widget)
        self.setCentralWidget(self.widget)
        self.widget.confirm_button.clicked.connect(self.make_maneuver)
        self.show()

    def make_maneuver(self):
        duration_s = self.widget.durationLineEdit.text()

        if not is_digit(duration_s):
            self.parent.statusBar().showMessage(
                "Длительность разворота не число!")
            self.close()

        duration = float(duration_s)
        if duration < 10:
            self.parent.statusBar().showMessage(
                "Длительность разворота не может быть меньше 10!")
            self.close()

        delta_height_s = self.widget.heightLineEdit.text()

        if not is_digit(delta_height_s):
            self.parent.statusBar().showMessage(
                "Разницы высоты - не число"
            )
            self.close()

        new_height = self.parent.graphic_window.scene.objects[
                         self.parent.graphic_window.aircraft_index
                     ].position.z + float(delta_height_s)

        if new_height < 5:
            self.parent.statusBar().showMessage(
                "Ошибка: итоговая высота меньше 5!"
            )
            self.close()

        self.parent.graphic_window.scene.objects[
            self.parent.graphic_window.aircraft_index
        ].change_height(duration * 24, new_height)
        self.close()
