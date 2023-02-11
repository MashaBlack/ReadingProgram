# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMinimumSize(QSize(650, 500))
        MainWindow.setMaximumSize(QSize(650, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_syllables = QPushButton(self.centralwidget)
        self.btn_syllables.setObjectName(u"btn_syllables")
        self.btn_syllables.setGeometry(QRect(350, 80, 181, 71))
        self.btn_reading = QPushButton(self.centralwidget)
        self.btn_reading.setObjectName(u"btn_reading")
        self.btn_reading.setGeometry(QRect(430, 200, 171, 71))
        self.btn_alphabet = QPushButton(self.centralwidget)
        self.btn_alphabet.setObjectName(u"btn_alphabet")
        self.btn_alphabet.setGeometry(QRect(360, 320, 171, 71))
        self.btn_alphabet.setStyleSheet(u"")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(70, 70, 257, 350))
        self.picture.setPixmap(QPixmap(u"images/boy_with_books.png"))
        self.picture.setScaledContents(True)
        self.btn_settings = QPushButton(self.centralwidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(580, 430, 60, 60))
        icon = QIcon()
        icon.addFile(u"images/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(40, 40))
        self.btn_about = QPushButton(self.centralwidget)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setGeometry(QRect(10, 430, 60, 60))
        icon1 = QIcon()
        icon1.addFile(u"images/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon1)
        self.btn_about.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0438\u0442\u0435\u043b\u044c", None))
        self.btn_syllables.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043b\u0430\u0434\u044b", None))
        self.btn_reading.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u0435\u043d\u0438\u0435", None))
        self.btn_alphabet.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0444\u0430\u0432\u0438\u0442", None))
        self.picture.setText("")
        self.btn_settings.setText("")
        self.btn_about.setText("")
    # retranslateUi

