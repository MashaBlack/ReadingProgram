# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditForm.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_EditForm(object):
    def setupUi(self, EditForm):
        if not EditForm.objectName():
            EditForm.setObjectName(u"EditForm")
        EditForm.resize(489, 448)
        self.lineEdit = QLineEdit(EditForm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 50, 151, 21))
        self.image = QLabel(EditForm)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(130, 110, 211, 201))
        self.image.setScaledContents(True)
        self.btn_save = QPushButton(EditForm)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(150, 350, 181, 71))

        self.retranslateUi(EditForm)

        QMetaObject.connectSlotsByName(EditForm)
    # setupUi

    def retranslateUi(self, EditForm):
        EditForm.setWindowTitle(QCoreApplication.translate("EditForm", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit.setText("")
        self.image.setText("")
        self.btn_save.setText(QCoreApplication.translate("EditForm", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

