# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownLinkMain.ui'
#
# Created: Wed Sep  9 20:58:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(460, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(460, 480))
        Form.setMaximumSize(QtCore.QSize(460, 880))
        self.cmd_exit = QtGui.QPushButton(Form)
        self.cmd_exit.setGeometry(QtCore.QRect(320, 410, 121, 27))
        self.cmd_exit.setObjectName(_fromUtf8("cmd_exit"))
        self.txt_Name = QtGui.QLineEdit(Form)
        self.txt_Name.setGeometry(QtCore.QRect(30, 60, 181, 27))
        self.txt_Name.setMaxLength(15)
        self.txt_Name.setObjectName(_fromUtf8("txt_Name"))
        self.txt_Lon = QtGui.QLineEdit(Form)
        self.txt_Lon.setGeometry(QtCore.QRect(280, 60, 151, 27))
        self.txt_Lon.setMaxLength(15)
        self.txt_Lon.setObjectName(_fromUtf8("txt_Lon"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 91, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txt_Port = QtGui.QLineEdit(Form)
        self.txt_Port.setGeometry(QtCore.QRect(250, 180, 181, 27))
        self.txt_Port.setMaxLength(15)
        self.txt_Port.setObjectName(_fromUtf8("txt_Port"))
        self.txt_URL = QtGui.QLineEdit(Form)
        self.txt_URL.setGeometry(QtCore.QRect(30, 180, 181, 27))
        self.txt_URL.setMaxLength(128)
        self.txt_URL.setObjectName(_fromUtf8("txt_URL"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 60, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cmd_StartProxy = QtGui.QPushButton(Form)
        self.cmd_StartProxy.setGeometry(QtCore.QRect(30, 410, 98, 27))
        self.cmd_StartProxy.setObjectName(_fromUtf8("cmd_StartProxy"))
        self.txt_Lat = QtGui.QLineEdit(Form)
        self.txt_Lat.setGeometry(QtCore.QRect(280, 90, 151, 27))
        self.txt_Lat.setMaxLength(15)
        self.txt_Lat.setObjectName(_fromUtf8("txt_Lat"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(250, 160, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 171, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cmd_StartGNURadio = QtGui.QPushButton(Form)
        self.cmd_StartGNURadio.setGeometry(QtCore.QRect(160, 410, 121, 27))
        self.cmd_StartGNURadio.setObjectName(_fromUtf8("cmd_StartGNURadio"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 40, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(250, 90, 91, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 310, 171, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lbl_status_server = QtGui.QLabel(Form)
        self.lbl_status_server.setGeometry(QtCore.QRect(30, 330, 161, 17))
        self.lbl_status_server.setObjectName(_fromUtf8("lbl_status_server"))
        self.lbl_status_gnu_A = QtGui.QLabel(Form)
        self.lbl_status_gnu_A.setGeometry(QtCore.QRect(30, 370, 251, 17))
        self.lbl_status_gnu_A.setObjectName(_fromUtf8("lbl_status_gnu_A"))
        self.cmd_SaveSettings = QtGui.QPushButton(Form)
        self.cmd_SaveSettings.setGeometry(QtCore.QRect(330, 220, 98, 27))
        self.cmd_SaveSettings.setObjectName(_fromUtf8("cmd_SaveSettings"))
        self.link_BY2HIT = QtGui.QCommandLinkButton(Form)
        self.link_BY2HIT.setGeometry(QtCore.QRect(20, 450, 111, 81))
        self.link_BY2HIT.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/by2hit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.link_BY2HIT.setIcon(icon)
        self.link_BY2HIT.setIconSize(QtCore.QSize(100, 96))
        self.link_BY2HIT.setShortcut(_fromUtf8(""))
        self.link_BY2HIT.setCheckable(False)
        self.link_BY2HIT.setObjectName(_fromUtf8("link_BY2HIT"))
        self.link_HIT = QtGui.QCommandLinkButton(Form)
        self.link_HIT.setGeometry(QtCore.QRect(170, 440, 101, 101))
        self.link_HIT.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/hit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.link_HIT.setIcon(icon1)
        self.link_HIT.setIconSize(QtCore.QSize(96, 96))
        self.link_HIT.setShortcut(_fromUtf8(""))
        self.link_HIT.setCheckable(False)
        self.link_HIT.setObjectName(_fromUtf8("link_HIT"))
        self.link_Lilac = QtGui.QCommandLinkButton(Form)
        self.link_Lilac.setGeometry(QtCore.QRect(320, 430, 111, 111))
        self.link_Lilac.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/LILACSAT1.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.link_Lilac.setIcon(icon2)
        self.link_Lilac.setIconSize(QtCore.QSize(96, 96))
        self.link_Lilac.setShortcut(_fromUtf8(""))
        self.link_Lilac.setCheckable(False)
        self.link_Lilac.setObjectName(_fromUtf8("link_Lilac"))
        self.txt_log = QtGui.QTextEdit(Form)
        self.txt_log.setGeometry(QtCore.QRect(0, 540, 451, 171))
        self.txt_log.setReadOnly(True)
        self.txt_log.setObjectName(_fromUtf8("txt_log"))
        self.txt_URL_Back = QtGui.QLineEdit(Form)
        self.txt_URL_Back.setGeometry(QtCore.QRect(30, 230, 111, 27))
        self.txt_URL_Back.setMaxLength(128)
        self.txt_URL_Back.setObjectName(_fromUtf8("txt_URL_Back"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 161, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.BackUrlEnable = QtGui.QCheckBox(Form)
        self.BackUrlEnable.setGeometry(QtCore.QRect(140, 230, 97, 22))
        self.BackUrlEnable.setObjectName(_fromUtf8("BackUrlEnable"))
        self.lbl_status_server_back = QtGui.QLabel(Form)
        self.lbl_status_server_back.setGeometry(QtCore.QRect(30, 350, 251, 17))
        self.lbl_status_server_back.setObjectName(_fromUtf8("lbl_status_server_back"))
        self.lbl_status_gnu_B = QtGui.QLabel(Form)
        self.lbl_status_gnu_B.setGeometry(QtCore.QRect(30, 390, 251, 17))
        self.lbl_status_gnu_B.setObjectName(_fromUtf8("lbl_status_gnu_B"))
        self.txt_Alt = QtGui.QLineEdit(Form)
        self.txt_Alt.setGeometry(QtCore.QRect(280, 120, 151, 27))
        self.txt_Alt.setMaxLength(15)
        self.txt_Alt.setObjectName(_fromUtf8("txt_Alt"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(250, 120, 91, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 260, 161, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.txt_TLE = QtGui.QLineEdit(Form)
        self.txt_TLE.setGeometry(QtCore.QRect(30, 280, 271, 27))
        self.txt_TLE.setMaxLength(128)
        self.txt_TLE.setObjectName(_fromUtf8("txt_TLE"))
        self.cmd_update_orbit = QtGui.QPushButton(Form)
        self.cmd_update_orbit.setGeometry(QtCore.QRect(330, 280, 98, 27))
        self.cmd_update_orbit.setObjectName(_fromUtf8("cmd_update_orbit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "LilacSat1 Downlink Proxy", None))
        self.cmd_exit.setText(_translate("Form", "Exit", None))
        self.txt_Name.setText(_translate("Form", "anonymous", None))
        self.txt_Lon.setText(_translate("Form", "126.6402290000", None))
        self.label_2.setText(_translate("Form", "Nick Name:", None))
        self.label_7.setText(_translate("Form", "Server URL:", None))
        self.txt_Port.setText(_translate("Form", "61161", None))
        self.txt_URL.setText(_translate("Form", "lilacsat.hit.edu.cn", None))
        self.label.setText(_translate("Form", "User Information", None))
        self.label_4.setText(_translate("Form", "Lon:", None))
        self.cmd_StartProxy.setText(_translate("Form", "Start Proxy", None))
        self.txt_Lat.setText(_translate("Form", "45.7404070000", None))
        self.label_8.setText(_translate("Form", "Server Port:", None))
        self.label_6.setText(_translate("Form", "Server Information", None))
        self.cmd_StartGNURadio.setText(_translate("Form", "Start GNU Radio", None))
        self.label_3.setText(_translate("Form", "Position:", None))
        self.label_5.setText(_translate("Form", "Lat:", None))
        self.label_9.setText(_translate("Form", "Status", None))
        self.lbl_status_server.setText(_translate("Form", "Server: Not Connected", None))
        self.lbl_status_gnu_A.setText(_translate("Form", "Receiver A: Not Connected", None))
        self.cmd_SaveSettings.setText(_translate("Form", "Save Settings", None))
        self.txt_URL_Back.setText(_translate("Form", "localhost", None))
        self.label_10.setText(_translate("Form", "BackUp Server URL:", None))
        self.BackUrlEnable.setText(_translate("Form", "Enable", None))
        self.lbl_status_server_back.setText(_translate("Form", "BackUp Server: Not Connected", None))
        self.lbl_status_gnu_B.setText(_translate("Form", "Receiver B: Not Connected", None))
        self.txt_Alt.setText(_translate("Form", "45.7404070000", None))
        self.label_11.setText(_translate("Form", "Alt:", None))
        self.label_12.setText(_translate("Form", "TLE URL:", None))
        self.txt_TLE.setText(_translate("Form", "http://lilacsat.hit.edu.cn/tle/TLE.txt", None))
        self.cmd_update_orbit.setText(_translate("Form", "Update Orbit", None))

import Images_rc
