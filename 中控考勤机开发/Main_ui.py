# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1175, 869)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1151, 831))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.DateEdit_Start = QDateEdit(self.groupBox)
        self.DateEdit_Start.setObjectName(u"DateEdit_Start")
        self.DateEdit_Start.setMinimumSize(QSize(150, 0))
        self.DateEdit_Start.setFont(font)
        self.DateEdit_Start.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout.addWidget(self.DateEdit_Start)

        self.DateEdit_End = QDateEdit(self.groupBox)
        self.DateEdit_End.setObjectName(u"DateEdit_End")
        self.DateEdit_End.setMinimumSize(QSize(150, 0))
        self.DateEdit_End.setFont(font)

        self.horizontalLayout.addWidget(self.DateEdit_End)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.LineEdit_ID = QLineEdit(self.groupBox)
        self.LineEdit_ID.setObjectName(u"LineEdit_ID")
        self.LineEdit_ID.setMinimumSize(QSize(100, 0))
        self.LineEdit_ID.setFont(font)

        self.horizontalLayout.addWidget(self.LineEdit_ID)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.ComboBox_IP = QComboBox(self.groupBox)
        self.ComboBox_IP.setObjectName(u"ComboBox_IP")
        self.ComboBox_IP.setMinimumSize(QSize(150, 0))
        self.ComboBox_IP.setFont(font)
        self.ComboBox_IP.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ComboBox_IP)

        self.Button_Query = QPushButton(self.groupBox)
        self.Button_Query.setObjectName(u"Button_Query")
        self.Button_Query.setFont(font)

        self.horizontalLayout.addWidget(self.Button_Query)

        self.Button_Catch = QPushButton(self.groupBox)
        self.Button_Catch.setObjectName(u"Button_Catch")
        self.Button_Catch.setFont(font)

        self.horizontalLayout.addWidget(self.Button_Catch)

        self.Button_Ana = QPushButton(self.groupBox)
        self.Button_Ana.setObjectName(u"Button_Ana")
        self.Button_Ana.setFont(font)

        self.horizontalLayout.addWidget(self.Button_Ana)

        self.Button_Export = QPushButton(self.groupBox)
        self.Button_Export.setObjectName(u"Button_Export")
        self.Button_Export.setFont(font)

        self.horizontalLayout.addWidget(self.Button_Export)

        self.Button_Clear = QPushButton(self.groupBox)
        self.Button_Clear.setObjectName(u"Button_Clear")
        self.Button_Clear.setFont(font)

        self.horizontalLayout.addWidget(self.Button_Clear)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.groupBox)

        self.TableView_Data = QTableView(self.layoutWidget)
        self.TableView_Data.setObjectName(u"TableView_Data")
        self.TableView_Data.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.TableView_Data)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u5c31\u9910\u6570\u636e\u5206\u6790", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u671f", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u5de5\u53f7:", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"IP:", None))
        self.Button_Query.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u8be2", None))
        self.Button_Catch.setText(QCoreApplication.translate("mainWindow", u"\u83b7\u53d6\u6570\u636e", None))
        self.Button_Ana.setText(QCoreApplication.translate("mainWindow", u"\u5206\u6790", None))
        self.Button_Export.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa", None))
        self.Button_Clear.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u9664\u6570\u636e", None))
    # retranslateUi

