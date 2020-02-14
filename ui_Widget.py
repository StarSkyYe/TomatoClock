# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(305, 331)
        font = QtGui.QFont()
        font.setPointSize(9)
        Widget.setFont(font)
        Widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_2 = QtWidgets.QGridLayout(Widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdMinutes = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdMinutes.setSmallDecimalPoint(False)
        self.lcdMinutes.setDigitCount(2)
        self.lcdMinutes.setProperty("intValue", 25)
        self.lcdMinutes.setObjectName("lcdMinutes")
        self.horizontalLayout.addWidget(self.lcdMinutes)
        self.lcdSecond = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdSecond.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdSecond.setLineWidth(1)
        self.lcdSecond.setMidLineWidth(0)
        self.lcdSecond.setSmallDecimalPoint(False)
        self.lcdSecond.setDigitCount(2)
        self.lcdSecond.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdSecond.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdSecond.setProperty("intValue", 0)
        self.lcdSecond.setObjectName("lcdSecond")
        self.horizontalLayout.addWidget(self.lcdSecond)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.btnStop = QtWidgets.QPushButton(Widget)
        self.btnStop.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/stop.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout_2.addWidget(self.btnStop, 3, 1, 1, 1)
        self.groupBoxSettings = QtWidgets.QGroupBox(Widget)
        self.groupBoxSettings.setEnabled(True)
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBoxSettings)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.spinBoxWork = QtWidgets.QSpinBox(self.groupBoxSettings)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.spinBoxWork.setFont(font)
        self.spinBoxWork.setToolTipDuration(-1)
        self.spinBoxWork.setMinimum(1)
        self.spinBoxWork.setMaximum(50)
        self.spinBoxWork.setProperty("value", 25)
        self.spinBoxWork.setObjectName("spinBoxWork")
        self.gridLayout.addWidget(self.spinBoxWork, 0, 1, 1, 1)
        self.spinBoxRest = QtWidgets.QSpinBox(self.groupBoxSettings)
        self.spinBoxRest.setToolTipDuration(-1)
        self.spinBoxRest.setMinimum(1)
        self.spinBoxRest.setMaximum(10)
        self.spinBoxRest.setProperty("value", 5)
        self.spinBoxRest.setObjectName("spinBoxRest")
        self.gridLayout.addWidget(self.spinBoxRest, 1, 1, 1, 1)
        self.lineEditAudioFile = QtWidgets.QLineEdit(self.groupBoxSettings)
        self.lineEditAudioFile.setObjectName("lineEditAudioFile")
        self.gridLayout.addWidget(self.lineEditAudioFile, 3, 1, 1, 1)
        self.checkBoxAudio = QtWidgets.QCheckBox(self.groupBoxSettings)
        self.checkBoxAudio.setChecked(True)
        self.checkBoxAudio.setObjectName("checkBoxAudio")
        self.gridLayout.addWidget(self.checkBoxAudio, 2, 0, 1, 1)
        self.labWork = QtWidgets.QLabel(self.groupBoxSettings)
        self.labWork.setObjectName("labWork")
        self.gridLayout.addWidget(self.labWork, 0, 0, 1, 1)
        self.labRest = QtWidgets.QLabel(self.groupBoxSettings)
        self.labRest.setObjectName("labRest")
        self.gridLayout.addWidget(self.labRest, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxSettings, 0, 0, 1, 2)
        self.btnStart = QtWidgets.QPushButton(Widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/start.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout_2.addWidget(self.btnStart, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.labState = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labState.setFont(font)
        self.labState.setObjectName("labState")
        self.horizontalLayout_2.addWidget(self.labState)
        spacerItem = QtWidgets.QSpacerItem(228, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "简易番茄时钟"))
        self.groupBox_2.setTitle(_translate("Widget", "剩余时长（分钟：秒数）"))
        self.btnStop.setText(_translate("Widget", "停止"))
        self.groupBoxSettings.setTitle(_translate("Widget", "模式设置"))
        self.label_2.setText(_translate("Widget", "音频文件名(mp3)"))
        self.spinBoxWork.setToolTip(_translate("Widget", "时长范围15-45分钟"))
        self.spinBoxRest.setToolTip(_translate("Widget", "时长范围1-10分钟"))
        self.lineEditAudioFile.setToolTip(_translate("Widget", "mp3文件路径，默认在当前目录下的media文件夹"))
        self.lineEditAudioFile.setText(_translate("Widget", "./media/fish.mp3"))
        self.checkBoxAudio.setText(_translate("Widget", "休息时播放音乐"))
        self.labWork.setText(_translate("Widget", "工作时长"))
        self.labRest.setText(_translate("Widget", "休息时长"))
        self.btnStart.setText(_translate("Widget", "启动"))
        self.label.setText(_translate("Widget", "当前状态: "))
        self.labState.setText(_translate("Widget", "未启动..."))
import res_rc
