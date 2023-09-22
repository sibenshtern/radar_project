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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QListView, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMaximumSize(QSize(800, 16777215))
        self.addButton = QPushButton(Widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(40, 40, 171, 41))
        self.addButton.setMouseTracking(False)
        self.addButton.setCheckable(False)
        self.addButton.setChecked(False)
        self.addButton.setAutoDefault(False)
        self.addButton.setFlat(False)
        self.modelButton = QPushButton(Widget)
        self.modelButton.setObjectName(u"modelButton")
        self.modelButton.setGeometry(QRect(40, 510, 171, 41))
        self.modelButton.setCheckable(False)
        self.settingsButton = QPushButton(Widget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(40, 410, 171, 41))
        self.settingsButton.setCheckable(False)
        self.openGLWidget = QOpenGLWidget(Widget)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(249, 39, 501, 511))
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 100, 171, 291))
        QWidget.setTabOrder(self.addButton, self.listView)
        QWidget.setTabOrder(self.listView, self.settingsButton)
        QWidget.setTabOrder(self.settingsButton, self.modelButton)

        self.retranslateUi(Widget)

        self.addButton.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.addButton.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
        self.modelButton.setText(QCoreApplication.translate("Widget", u"\u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.settingsButton.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

