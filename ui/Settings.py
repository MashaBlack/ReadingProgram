# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(439, 346)
        self.wordsTable = QTableWidget(Settings)
        if (self.wordsTable.columnCount() < 3):
            self.wordsTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.wordsTable.setObjectName(u"wordsTable")
        self.wordsTable.setGeometry(QRect(20, 30, 401, 221))
        self.btn_add = QPushButton(Settings)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(20, 260, 210, 70))
        self.btn_clear = QPushButton(Settings)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(230, 260, 200, 70))

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        ___qtablewidgetitem = self.wordsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Settings", u"\u0421\u043b\u043e\u0432\u043e", None));
        ___qtablewidgetitem1 = self.wordsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Settings", u"", None));
        ___qtablewidgetitem2 = self.wordsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Settings", u"", None));
        self.btn_add.setText(QCoreApplication.translate("Settings", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.btn_clear.setText(QCoreApplication.translate("Settings", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
    # retranslateUi

