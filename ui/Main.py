# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
        MainWindow.resize(611, 427)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.btn_alphabet = QPushButton(self.centralwidget)
        self.btn_alphabet.setObjectName(u"btn_alphabet")
        self.btn_alphabet.setGeometry(QRect(340, 60, 171, 71))
        self.btn_alphabet.setStyleSheet(u"")
        self.btn_syllables = QPushButton(self.centralwidget)
        self.btn_syllables.setObjectName(u"btn_syllables")
        self.btn_syllables.setGeometry(QRect(390, 170, 181, 71))
        self.btn_reading = QPushButton(self.centralwidget)
        self.btn_reading.setObjectName(u"btn_games")
        self.btn_reading.setGeometry(QRect(330, 280, 171, 71))
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(70, 60, 261, 311))
        self.picture.setPixmap(QPixmap(u"images/boy_with_books.png"))
        self.picture.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u043b\u043a\u0430", None))
        self.btn_alphabet.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0444\u0430\u0432\u0438\u0442", None))
        self.btn_syllables.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043b\u0430\u0434\u044b", None))
        self.btn_reading.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u0435\u043d\u0438\u0435", None))
        self.picture.setText("")
    # retranslateUi

