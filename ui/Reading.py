# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reading.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QWidget, QGraphicsDropShadowEffect)

class Ui_Reading(object):
    def setupUi(self, Reading):
        if not Reading.objectName():
            Reading.setObjectName(u"Reading")
        Reading.resize(900, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Reading.sizePolicy().hasHeightForWidth())
        Reading.setSizePolicy(sizePolicy)
        Reading.setMinimumSize(QSize(900, 700))
        Reading.setMaximumSize(QSize(901, 700))
        self.horizontalLayoutWidget = QWidget(Reading)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(210, 350, 471, 151))
        self.layout_word = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_word.setSpacing(0)
        self.layout_word.setObjectName(u"layout_word")
        self.layout_word.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_word.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_word.addItem(self.horizontalSpacer)

        self.btn_start = QPushButton(self.horizontalLayoutWidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(200, 80))
        self.btn_start.setMaximumSize(QSize(200, 80))

        self.layout_word.addWidget(self.btn_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_word.addItem(self.horizontalSpacer_2)

        self.btn_divide = QPushButton(Reading)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setGeometry(QRect(210, 540, 110, 110))
        icon = QIcon()
        icon.addFile(u"images/divide.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_divide.setIcon(icon)
        self.btn_divide.setIconSize(QSize(60, 60))
        self.btn_next = QPushButton(Reading)
        self.btn_next.setObjectName(u"btn_next")
        self.btn_next.setGeometry(QRect(820, 390, 70, 70))
        icon1 = QIcon()
        icon1.addFile(u"images/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next.setIcon(icon1)
        self.btn_next.setIconSize(QSize(40, 40))
        self.btn_record = QPushButton(Reading)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setGeometry(QRect(570, 540, 110, 110))
        icon2 = QIcon()
        icon2.addFile(u"images/recorder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_record.setIcon(icon2)
        self.btn_record.setIconSize(QSize(60, 60))
        self.btn_menu = QPushButton(Reading)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setGeometry(QRect(20, 20, 70, 70))
        icon3 = QIcon()
        icon3.addFile(u"images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon3)
        self.btn_menu.setIconSize(QSize(30, 30))
        self.btn_back = QPushButton(Reading)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(10, 390, 70, 70))
        icon4 = QIcon()
        icon4.addFile(u"images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon4)
        self.btn_back.setIconSize(QSize(40, 40))
        self.image = QLabel(Reading)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(290, 20, 300, 300))
        self.image.setScaledContents(True)

        self.retranslateUi(Reading)

        QMetaObject.connectSlotsByName(Reading)
    # setupUi

    def retranslateUi(self, Reading):
        Reading.setWindowTitle(QCoreApplication.translate("Reading", u"\u0427\u0442\u0435\u043d\u0438\u0435", None))
        self.btn_start.setText(QCoreApplication.translate("Reading", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.btn_divide.setText("")
        self.btn_next.setText("")
        self.btn_record.setText("")
        self.btn_menu.setText("")
        self.btn_back.setText("")
        self.image.setText("")
    # retranslateUi

