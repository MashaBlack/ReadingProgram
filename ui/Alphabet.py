# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alphabet.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Alphabet(object):
    def setupUi(self, Alphabet):
        if not Alphabet.objectName():
            Alphabet.setObjectName(u"Alphabet")
        Alphabet.resize(650, 500)
        Alphabet.setMinimumSize(QSize(650, 500))
        Alphabet.setMaximumSize(QSize(650, 500))
        self.letter = QLabel(Alphabet)
        self.letter.setObjectName(u"letter")
        self.letter.setGeometry(QRect(170, 40, 291, 331))
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(288)
        self.letter.setFont(font)
        self.letter.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.btn_sound = QPushButton(Alphabet)
        self.btn_sound.setObjectName(u"btn_sound")
        self.btn_sound.setGeometry(QRect(130, 360, 91, 81))
        icon = QIcon()
        icon.addFile(u"images/sound.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sound.setIcon(icon)
        self.btn_sound.setIconSize(QSize(30, 30))
        self.btn_record = QPushButton(Alphabet)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setGeometry(QRect(430, 360, 91, 81))
        icon1 = QIcon()
        icon1.addFile(u"images/recorder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record.setIcon(icon1)
        self.btn_record.setIconSize(QSize(30, 30))
        self.btn_back = QPushButton(Alphabet)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(20, 170, 91, 81))
        icon2 = QIcon()
        icon2.addFile(u"images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon2)
        self.btn_back.setIconSize(QSize(40, 40))
        self.btn_next = QPushButton(Alphabet)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(520, 170, 91, 81))
        self.btn_next.setToolTipDuration(0)
        icon3 = QIcon()
        icon3.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QSize(40, 40))
        self.btn_menu = QPushButton(Alphabet)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setGeometry(QRect(0, 0, 71, 61))
        icon4 = QIcon()
        icon4.addFile(u"images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon4)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.retranslateUi(Alphabet)

        QMetaObject.connectSlotsByName(Alphabet)
    # setupUi

    def retranslateUi(self, Alphabet):
        Alphabet.setWindowTitle(QCoreApplication.translate("Alphabet", u"\u0410\u043b\u0444\u0430\u0432\u0438\u0442", None))
        self.letter.setText("")
        self.btn_sound.setText("")
        self.btn_record.setText("")
        self.btn_back.setText("")
        self.btn_next.setText("")
        self.btn_menu.setText("")
    # retranslateUi

