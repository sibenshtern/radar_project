# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListView, QPushButton, QSizePolicy,
    QWidget, QDialog)

from ui_dialog import Ui_Dialog
from ui_maneuver import Ui_Maneuver
from ui_settings import Ui_Settings

from myglwidget import MyGLWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMaximumSize(QSize(800, 16777215))

        self.addButton = QPushButton(Widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(40, 40, 171, 41))

        self.modelButton = QPushButton(Widget)
        self.modelButton.setObjectName(u"modelButton")
        self.modelButton.setGeometry(QRect(40, 510, 171, 41))

        self.settingsButton = QPushButton(Widget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(40, 410, 171, 41))

        self.openGLWidget = MyGLWidget(Widget)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(249, 39, 501, 511))

        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 100, 171, 291))

        self.settingsButton_2 = QPushButton(Widget)
        self.settingsButton_2.setObjectName(u"settingsButton_2")
        self.settingsButton_2.setGeometry(QRect(40, 460, 171, 41))

        QWidget.setTabOrder(self.addButton, self.listView)
        QWidget.setTabOrder(self.listView, self.settingsButton)
        QWidget.setTabOrder(self.settingsButton, self.modelButton)

        self.retranslateUi(Widget)

        self.addButton.clicked.connect(self.open_dialog)
        self.settingsButton_2.clicked.connect(self.open_maneuver)
        self.settingsButton.clicked.connect(self.open_settings)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def open_dialog(self):
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def open_maneuver(self):
        Dialog = QDialog()
        ui = Ui_Maneuver()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def open_settings(self):
        Dialog = QDialog()
        ui = Ui_Settings()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.addButton.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
        self.modelButton.setText(QCoreApplication.translate("Widget", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.settingsButton_2.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u043d\u0435\u0432\u0440", None))
    # retranslateUi

