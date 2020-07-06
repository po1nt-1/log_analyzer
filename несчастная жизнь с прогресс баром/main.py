# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1165, 581)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(980, 581))
        MainWindow.setMaximumSize(QSize(1600, 581))
        MainWindow.setBaseSize(QSize(980, 581))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionqsqs = QAction(MainWindow)
        self.actionqsqs.setObjectName(u"actionqsqs")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.menu_exit_button = QAction(MainWindow)
        self.menu_exit_button.setObjectName(u"menu_exit_button")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font2 = QFont()
        font2.setPointSize(11)
        self.frame.setFont(font2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(185, 42))
        self.label_6.setMaximumSize(QSize(185, 42))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.verticalLayout_3.addWidget(self.label)

        self.begin_date = QDateTimeEdit(self.frame)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setMinimumSize(QSize(185, 28))
        self.begin_date.setMaximumSize(QSize(185, 28))
        self.begin_date.setFont(font3)
        self.begin_date.setProperty("showGroupSeparator", False)
        self.begin_date.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.begin_date.setMaximumDateTime(QDateTime(QDate(5000, 1, 1), QTime(10, 0, 0)))
        self.begin_date.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(10, 0, 0)))
        self.begin_date.setMaximumDate(QDate(5000, 1, 1))
        self.begin_date.setCalendarPopup(True)
        self.begin_date.setCurrentSectionIndex(0)
        self.begin_date.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_3.addWidget(self.begin_date)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_2)

        self.end_date = QDateTimeEdit(self.frame)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setMinimumSize(QSize(185, 28))
        self.end_date.setMaximumSize(QSize(185, 28))
        self.end_date.setFont(font3)
        self.end_date.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.end_date.setMaximumDateTime(QDateTime(QDate(5000, 1, 1), QTime(11, 0, 0)))
        self.end_date.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(11, 0, 0)))
        self.end_date.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.end_date)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(185, 56))
        self.label_5.setMaximumSize(QSize(185, 56))
        self.label_5.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_5)

        self.login_line = QLineEdit(self.frame)
        self.login_line.setObjectName(u"login_line")
        self.login_line.setMinimumSize(QSize(185, 28))
        self.login_line.setMaximumSize(QSize(185, 28))
        font4 = QFont()
        font4.setFamily(u"Carlito")
        font4.setPointSize(11)
        self.login_line.setFont(font4)

        self.verticalLayout_3.addWidget(self.login_line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.select_folder_button = QPushButton(self.frame)
        self.select_folder_button.setObjectName(u"select_folder_button")
        self.select_folder_button.setMinimumSize(QSize(185, 42))
        self.select_folder_button.setMaximumSize(QSize(185, 42))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.select_folder_button.setFont(font5)

        self.verticalLayout_3.addWidget(self.select_folder_button)

        self.show_csv_button = QPushButton(self.frame)
        self.show_csv_button.setObjectName(u"show_csv_button")
        self.show_csv_button.setMinimumSize(QSize(185, 28))
        self.show_csv_button.setMaximumSize(QSize(185, 28))
        self.show_csv_button.setFont(font5)

        self.verticalLayout_3.addWidget(self.show_csv_button)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_csv = QTableWidget(self.frame_4)
        self.table_csv.setObjectName(u"table_csv")
        self.table_csv.setMinimumSize(QSize(375, 360))
        self.table_csv.setMaximumSize(QSize(16777215, 360))
        font6 = QFont()
        font6.setFamily(u"Carlito")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.table_csv.setFont(font6)
        self.table_csv.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.table_csv.setMouseTracking(False)
        self.table_csv.setTabletTracking(False)
        self.table_csv.setFocusPolicy(Qt.NoFocus)
        self.table_csv.setContextMenuPolicy(Qt.NoContextMenu)
        self.table_csv.setAutoScroll(True)
        self.table_csv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_csv.setTabKeyNavigation(False)
        self.table_csv.setProperty("showDropIndicator", False)
        self.table_csv.setDragDropOverwriteMode(False)
        self.table_csv.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_csv.setTextElideMode(Qt.ElideMiddle)
        self.table_csv.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.table_csv.setShowGrid(True)
        self.table_csv.setGridStyle(Qt.DotLine)
        self.table_csv.setSortingEnabled(True)
        self.table_csv.setWordWrap(False)
        self.table_csv.setCornerButtonEnabled(False)
        self.table_csv.horizontalHeader().setVisible(True)
        self.table_csv.horizontalHeader().setCascadingSectionResizes(False)
        self.table_csv.horizontalHeader().setMinimumSectionSize(40)
        self.table_csv.horizontalHeader().setDefaultSectionSize(55)
        self.table_csv.horizontalHeader().setHighlightSections(False)
        self.table_csv.horizontalHeader().setProperty("showSortIndicator", True)
        self.table_csv.verticalHeader().setVisible(False)
        self.table_csv.verticalHeader().setCascadingSectionResizes(False)
        self.table_csv.verticalHeader().setMinimumSectionSize(20)
        self.table_csv.verticalHeader().setDefaultSectionSize(20)
        self.table_csv.verticalHeader().setHighlightSections(False)
        self.table_csv.verticalHeader().setProperty("showSortIndicator", False)
        self.table_csv.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.table_csv, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.page_back_button = QPushButton(self.frame_4)
        self.page_back_button.setObjectName(u"page_back_button")
        self.page_back_button.setMinimumSize(QSize(102, 28))
        self.page_back_button.setMaximumSize(QSize(102, 28))
        self.page_back_button.setFont(font5)

        self.horizontalLayout.addWidget(self.page_back_button)

        self.current_page_num = QPlainTextEdit(self.frame_4)
        self.current_page_num.setObjectName(u"current_page_num")
        self.current_page_num.setMinimumSize(QSize(102, 28))
        self.current_page_num.setMaximumSize(QSize(102, 28))
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(True)
        font7.setWeight(75)
        self.current_page_num.setFont(font7)
        self.current_page_num.setAcceptDrops(False)
        self.current_page_num.setToolTipDuration(0)
        self.current_page_num.setLayoutDirection(Qt.LeftToRight)
        self.current_page_num.setAutoFillBackground(True)
        self.current_page_num.setInputMethodHints(Qt.ImhNone)
        self.current_page_num.setFrameShape(QFrame.Box)
        self.current_page_num.setFrameShadow(QFrame.Plain)
        self.current_page_num.setLineWidth(0)
        self.current_page_num.setMidLineWidth(0)
        self.current_page_num.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.current_page_num.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.current_page_num.setUndoRedoEnabled(False)
        self.current_page_num.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.current_page_num.setReadOnly(True)
        self.current_page_num.setOverwriteMode(False)
        self.current_page_num.setTabStopWidth(80)
        self.current_page_num.setCursorWidth(1)
        self.current_page_num.setCenterOnScroll(True)

        self.horizontalLayout.addWidget(self.current_page_num)

        self.__plain_label = QLabel(self.frame_4)
        self.__plain_label.setObjectName(u"__plain_label")
        self.__plain_label.setMinimumSize(QSize(42, 28))
        self.__plain_label.setMaximumSize(QSize(42, 28))
        self.__plain_label.setFont(font7)
        self.__plain_label.setFrameShadow(QFrame.Plain)
        self.__plain_label.setLineWidth(0)

        self.horizontalLayout.addWidget(self.__plain_label)

        self.last_page_num = QPlainTextEdit(self.frame_4)
        self.last_page_num.setObjectName(u"last_page_num")
        self.last_page_num.setMinimumSize(QSize(102, 28))
        self.last_page_num.setMaximumSize(QSize(102, 28))
        self.last_page_num.setFont(font7)
        self.last_page_num.setAcceptDrops(False)
        self.last_page_num.setToolTipDuration(0)
        self.last_page_num.setLayoutDirection(Qt.LeftToRight)
        self.last_page_num.setAutoFillBackground(True)
        self.last_page_num.setInputMethodHints(Qt.ImhNone)
        self.last_page_num.setFrameShape(QFrame.Box)
        self.last_page_num.setFrameShadow(QFrame.Plain)
        self.last_page_num.setLineWidth(0)
        self.last_page_num.setMidLineWidth(0)
        self.last_page_num.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.last_page_num.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.last_page_num.setUndoRedoEnabled(False)
        self.last_page_num.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.last_page_num.setReadOnly(True)
        self.last_page_num.setOverwriteMode(False)
        self.last_page_num.setTabStopWidth(80)
        self.last_page_num.setCursorWidth(1)
        self.last_page_num.setCenterOnScroll(True)

        self.horizontalLayout.addWidget(self.last_page_num)

        self.page_forward_button = QPushButton(self.frame_4)
        self.page_forward_button.setObjectName(u"page_forward_button")
        self.page_forward_button.setMinimumSize(QSize(102, 28))
        self.page_forward_button.setMaximumSize(QSize(102, 28))
        self.page_forward_button.setFont(font3)
        self.page_forward_button.setAutoDefault(False)
        self.page_forward_button.setFlat(False)

        self.horizontalLayout.addWidget(self.page_forward_button)

        self.horizontalSpacer = QSpacerItem(334, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(180, 28))
        self.progressBar.setMaximumSize(QSize(180, 28))
        self.progressBar.setFont(font3)
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(32, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_4)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.show_csv_button, self.page_back_button)
        QWidget.setTabOrder(self.page_back_button, self.page_forward_button)

        self.retranslateUi(MainWindow)

        self.page_forward_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Log Analyzer by po1nt&Qt", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.actionqsqs.setText(QCoreApplication.translate("MainWindow", u"qsqs", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu_exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"         \u0424\u0438\u043b\u044c\u0442\u0440\u044b:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0438\u0442\u043e\u0433\u043e\u0432\u043e\u0433\u043e csv:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"                       \u041e\u0442", None))
        self.begin_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd HH:mm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                       \u0414\u043e", None))
        self.end_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy.MM.dd HH:mm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"                   \u041b\u043e\u0433\u0438\u043d:", None))
        self.login_line.setText("")
        self.select_folder_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0441 csv\n"
"\u0438 \u043e\u0442\u0444\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.show_csv_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c csv", None))
        self.page_back_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.current_page_num.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.__plain_label.setText(QCoreApplication.translate("MainWindow", u"   \u0438\u0437", None))
        self.last_page_num.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.page_forward_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0451\u0434", None))
    # retranslateUi

