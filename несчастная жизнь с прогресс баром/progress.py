# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(418, 100)
        Form.setMinimumSize(QSize(400, 100))
        Form.setMaximumSize(QSize(418, 100))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(9, 12, 400, 75))
        self.progressBar.setMinimumSize(QSize(400, 75))
        self.progressBar.setMaximumSize(QSize(400, 75))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f", None))
    # retranslateUi

