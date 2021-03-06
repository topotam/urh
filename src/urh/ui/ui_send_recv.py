# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SendRecvDialog(object):
    def setupUi(self, SendRecvDialog):
        SendRecvDialog.setObjectName("SendRecvDialog")
        SendRecvDialog.setWindowModality(QtCore.Qt.NonModal)
        SendRecvDialog.resize(850, 886)
        SendRecvDialog.setMouseTracking(False)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(SendRecvDialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinbox_sniff_Noise = QtWidgets.QDoubleSpinBox(SendRecvDialog)
        self.spinbox_sniff_Noise.setDecimals(4)
        self.spinbox_sniff_Noise.setMaximum(1.0)
        self.spinbox_sniff_Noise.setObjectName("spinbox_sniff_Noise")
        self.gridLayout.addWidget(self.spinbox_sniff_Noise, 10, 1, 1, 1)
        self.lineEditIP = QtWidgets.QLineEdit(SendRecvDialog)
        self.lineEditIP.setObjectName("lineEditIP")
        self.gridLayout.addWidget(self.lineEditIP, 1, 1, 1, 1)
        self.spinBoxGain = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinBoxGain.setMinimum(1)
        self.spinBoxGain.setMaximum(500)
        self.spinBoxGain.setProperty("value", 40)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.gridLayout.addWidget(self.spinBoxGain, 6, 1, 1, 1)
        self.labelGain = QtWidgets.QLabel(SendRecvDialog)
        self.labelGain.setObjectName("labelGain")
        self.gridLayout.addWidget(self.labelGain, 6, 0, 1, 1)
        self.labelBandWidth = QtWidgets.QLabel(SendRecvDialog)
        self.labelBandWidth.setObjectName("labelBandWidth")
        self.gridLayout.addWidget(self.labelBandWidth, 5, 0, 1, 1)
        self.cbDevice = QtWidgets.QComboBox(SendRecvDialog)
        self.cbDevice.setObjectName("cbDevice")
        self.cbDevice.addItem("")
        self.cbDevice.addItem("")
        self.gridLayout.addWidget(self.cbDevice, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(SendRecvDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.labelSampleRate = QtWidgets.QLabel(SendRecvDialog)
        self.labelSampleRate.setObjectName("labelSampleRate")
        self.gridLayout.addWidget(self.labelSampleRate, 4, 0, 1, 1)
        self.labelIP = QtWidgets.QLabel(SendRecvDialog)
        self.labelIP.setObjectName("labelIP")
        self.gridLayout.addWidget(self.labelIP, 1, 0, 1, 1)
        self.labelPort = QtWidgets.QLabel(SendRecvDialog)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 2, 0, 1, 1)
        self.spinBoxPort = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinBoxPort.setMinimum(1)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 1234)
        self.spinBoxPort.setObjectName("spinBoxPort")
        self.gridLayout.addWidget(self.spinBoxPort, 2, 1, 1, 1)
        self.spinBoxNRepeat = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinBoxNRepeat.setMaximum(999999999)
        self.spinBoxNRepeat.setObjectName("spinBoxNRepeat")
        self.gridLayout.addWidget(self.spinBoxNRepeat, 7, 1, 1, 1)
        self.labelFreq = QtWidgets.QLabel(SendRecvDialog)
        self.labelFreq.setObjectName("labelFreq")
        self.gridLayout.addWidget(self.labelFreq, 3, 0, 1, 1)
        self.labelNRepeat = QtWidgets.QLabel(SendRecvDialog)
        self.labelNRepeat.setObjectName("labelNRepeat")
        self.gridLayout.addWidget(self.labelNRepeat, 7, 0, 1, 1)
        self.spinBoxFreq = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxFreq.setDecimals(3)
        self.spinBoxFreq.setMinimum(0.001)
        self.spinBoxFreq.setMaximum(1000000000000.0)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.gridLayout.addWidget(self.spinBoxFreq, 3, 1, 1, 1)
        self.spinBoxSampleRate = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxSampleRate.setDecimals(3)
        self.spinBoxSampleRate.setMinimum(0.001)
        self.spinBoxSampleRate.setMaximum(1000000000000.0)
        self.spinBoxSampleRate.setObjectName("spinBoxSampleRate")
        self.gridLayout.addWidget(self.spinBoxSampleRate, 4, 1, 1, 1)
        self.spinBoxBandwidth = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxBandwidth.setDecimals(3)
        self.spinBoxBandwidth.setMinimum(0.001)
        self.spinBoxBandwidth.setMaximum(1000000000000.0)
        self.spinBoxBandwidth.setObjectName("spinBoxBandwidth")
        self.gridLayout.addWidget(self.spinBoxBandwidth, 5, 1, 1, 1)
        self.btnLockBWSR = QtWidgets.QToolButton(SendRecvDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/data/icons/lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLockBWSR.setIcon(icon)
        self.btnLockBWSR.setCheckable(True)
        self.btnLockBWSR.setChecked(True)
        self.btnLockBWSR.setObjectName("btnLockBWSR")
        self.gridLayout.addWidget(self.btnLockBWSR, 4, 2, 2, 1)
        self.spinbox_sniff_Center = QtWidgets.QDoubleSpinBox(SendRecvDialog)
        self.spinbox_sniff_Center.setDecimals(4)
        self.spinbox_sniff_Center.setMinimum(-3.14)
        self.spinbox_sniff_Center.setMaximum(3.14)
        self.spinbox_sniff_Center.setObjectName("spinbox_sniff_Center")
        self.gridLayout.addWidget(self.spinbox_sniff_Center, 9, 1, 1, 1)
        self.label_sniff_Noise = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_Noise.setObjectName("label_sniff_Noise")
        self.gridLayout.addWidget(self.label_sniff_Noise, 10, 0, 1, 1)
        self.label_sniff_Center = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_Center.setObjectName("label_sniff_Center")
        self.gridLayout.addWidget(self.label_sniff_Center, 9, 0, 1, 1)
        self.label_sniff_Modulation = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_Modulation.setObjectName("label_sniff_Modulation")
        self.gridLayout.addWidget(self.label_sniff_Modulation, 12, 0, 1, 1)
        self.combox_sniff_Modulation = QtWidgets.QComboBox(SendRecvDialog)
        self.combox_sniff_Modulation.setObjectName("combox_sniff_Modulation")
        self.combox_sniff_Modulation.addItem("")
        self.combox_sniff_Modulation.addItem("")
        self.combox_sniff_Modulation.addItem("")
        self.gridLayout.addWidget(self.combox_sniff_Modulation, 12, 1, 1, 1)
        self.label_sniff_OutputFile = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_OutputFile.setObjectName("label_sniff_OutputFile")
        self.gridLayout.addWidget(self.label_sniff_OutputFile, 14, 0, 1, 1)
        self.lineEdit_sniff_OutputFile = QtWidgets.QLineEdit(SendRecvDialog)
        self.lineEdit_sniff_OutputFile.setReadOnly(False)
        self.lineEdit_sniff_OutputFile.setProperty("clearButtonEnabled", True)
        self.lineEdit_sniff_OutputFile.setObjectName("lineEdit_sniff_OutputFile")
        self.gridLayout.addWidget(self.lineEdit_sniff_OutputFile, 14, 1, 1, 1)
        self.label_sniff_BitLength = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_BitLength.setObjectName("label_sniff_BitLength")
        self.gridLayout.addWidget(self.label_sniff_BitLength, 8, 0, 1, 1)
        self.spinbox_sniff_BitLen = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinbox_sniff_BitLen.setMinimum(1)
        self.spinbox_sniff_BitLen.setMaximum(999999999)
        self.spinbox_sniff_BitLen.setObjectName("spinbox_sniff_BitLen")
        self.gridLayout.addWidget(self.spinbox_sniff_BitLen, 8, 1, 1, 1)
        self.label_sniff_Tolerance = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_Tolerance.setObjectName("label_sniff_Tolerance")
        self.gridLayout.addWidget(self.label_sniff_Tolerance, 11, 0, 1, 1)
        self.spinbox_sniff_ErrorTolerance = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinbox_sniff_ErrorTolerance.setMaximum(999999)
        self.spinbox_sniff_ErrorTolerance.setProperty("value", 5)
        self.spinbox_sniff_ErrorTolerance.setObjectName("spinbox_sniff_ErrorTolerance")
        self.gridLayout.addWidget(self.spinbox_sniff_ErrorTolerance, 11, 1, 1, 1)
        self.comboBox_sniff_viewtype = QtWidgets.QComboBox(SendRecvDialog)
        self.comboBox_sniff_viewtype.setObjectName("comboBox_sniff_viewtype")
        self.comboBox_sniff_viewtype.addItem("")
        self.comboBox_sniff_viewtype.addItem("")
        self.comboBox_sniff_viewtype.addItem("")
        self.gridLayout.addWidget(self.comboBox_sniff_viewtype, 12, 1, 1, 1)
        self.label_sniff_viewtype = QtWidgets.QLabel(SendRecvDialog)
        self.label_sniff_viewtype.setObjectName("label_sniff_viewtype")
        self.gridLayout.addWidget(self.label_sniff_viewtype, 12, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(SendRecvDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 14, 0, 1, 1)
        self.lSamplesSentText = QtWidgets.QLabel(self.groupBox)
        self.lSamplesSentText.setObjectName("lSamplesSentText")
        self.gridLayout_2.addWidget(self.lSamplesSentText, 13, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.lTimeText = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lTimeText.setFont(font)
        self.lTimeText.setObjectName("lTimeText")
        self.gridLayout_2.addWidget(self.lTimeText, 7, 0, 1, 1)
        self.lSamplesCapturedText = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSamplesCapturedText.sizePolicy().hasHeightForWidth())
        self.lSamplesCapturedText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lSamplesCapturedText.setFont(font)
        self.lSamplesCapturedText.setObjectName("lSamplesCapturedText")
        self.gridLayout_2.addWidget(self.lSamplesCapturedText, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnStart = QtWidgets.QToolButton(self.groupBox)
        self.btnStart.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStart.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStart.setText("")
        icon = QtGui.QIcon.fromTheme("media-record")
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QtCore.QSize(32, 32))
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QToolButton(self.groupBox)
        self.btnStop.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStop.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStop.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.btnStop.setIcon(icon)
        self.btnStop.setIconSize(QtCore.QSize(32, 32))
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnSave = QtWidgets.QToolButton(self.groupBox)
        self.btnSave.setMinimumSize(QtCore.QSize(42, 42))
        self.btnSave.setMaximumSize(QtCore.QSize(42, 42))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QtCore.QSize(32, 32))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnClear = QtWidgets.QToolButton(self.groupBox)
        self.btnClear.setMinimumSize(QtCore.QSize(42, 42))
        self.btnClear.setMaximumSize(QtCore.QSize(42, 42))
        self.btnClear.setText("")
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnClear.setIcon(icon)
        self.btnClear.setIconSize(QtCore.QSize(32, 32))
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.lSignalSizeText = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalSizeText.sizePolicy().hasHeightForWidth())
        self.lSignalSizeText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lSignalSizeText.setFont(font)
        self.lSignalSizeText.setObjectName("lSignalSizeText")
        self.gridLayout_2.addWidget(self.lSignalSizeText, 5, 0, 1, 1)
        self.lSamplesCaptured = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSamplesCaptured.sizePolicy().hasHeightForWidth())
        self.lSamplesCaptured.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lSamplesCaptured.setFont(font)
        self.lSamplesCaptured.setAlignment(QtCore.Qt.AlignCenter)
        self.lSamplesCaptured.setObjectName("lSamplesCaptured")
        self.gridLayout_2.addWidget(self.lSamplesCaptured, 4, 0, 1, 2)
        self.lTime = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lTime.setFont(font)
        self.lTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lTime.setObjectName("lTime")
        self.gridLayout_2.addWidget(self.lTime, 10, 0, 1, 2)
        self.lSignalSize = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalSize.sizePolicy().hasHeightForWidth())
        self.lSignalSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lSignalSize.setFont(font)
        self.lSignalSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lSignalSize.setObjectName("lSignalSize")
        self.gridLayout_2.addWidget(self.lSignalSize, 6, 0, 1, 2)
        self.lblRepeatText = QtWidgets.QLabel(self.groupBox)
        self.lblRepeatText.setObjectName("lblRepeatText")
        self.gridLayout_2.addWidget(self.lblRepeatText, 11, 0, 1, 1)
        self.lblCurrentRepeatValue = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrentRepeatValue.setFont(font)
        self.lblCurrentRepeatValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentRepeatValue.setObjectName("lblCurrentRepeatValue")
        self.gridLayout_2.addWidget(self.lblCurrentRepeatValue, 12, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.txtEditErrors = QtWidgets.QTextEdit(SendRecvDialog)
        self.txtEditErrors.setReadOnly(True)
        self.txtEditErrors.setObjectName("txtEditErrors")
        self.verticalLayout.addWidget(self.txtEditErrors)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(SendRecvDialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_receive = QtWidgets.QWidget()
        self.page_receive.setObjectName("page_receive")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_receive)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsViewReceive = LiveGraphicView(self.page_receive)
        self.graphicsViewReceive.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsViewReceive.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsViewReceive.setObjectName("graphicsViewReceive")
        self.verticalLayout_2.addWidget(self.graphicsViewReceive)
        self.stackedWidget.addWidget(self.page_receive)
        self.page_send = QtWidgets.QWidget()
        self.page_send.setObjectName("page_send")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_send)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsViewSend = EditableGraphicView(self.page_send)
        self.graphicsViewSend.setMouseTracking(True)
        self.graphicsViewSend.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.graphicsViewSend.setTransformationAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsViewSend.setResizeAnchor(QtWidgets.QGraphicsView.NoAnchor)
        self.graphicsViewSend.setObjectName("graphicsViewSend")
        self.verticalLayout_3.addWidget(self.graphicsViewSend)
        self.label_7 = QtWidgets.QLabel(self.page_send)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page_send)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txtEd_sniff_Preview = QtWidgets.QPlainTextEdit(self.page)
        self.txtEd_sniff_Preview.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.txtEd_sniff_Preview.setReadOnly(True)
        self.txtEd_sniff_Preview.setMaximumBlockCount(100)
        self.txtEd_sniff_Preview.setObjectName("txtEd_sniff_Preview")
        self.verticalLayout_4.addWidget(self.txtEd_sniff_Preview)
        self.btnAccept = QtWidgets.QPushButton(self.page)
        self.btnAccept.setAutoDefault(False)
        self.btnAccept.setObjectName("btnAccept")
        self.verticalLayout_4.addWidget(self.btnAccept)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_y_scale = QtWidgets.QLabel(SendRecvDialog)
        self.label_y_scale.setObjectName("label_y_scale")
        self.verticalLayout_5.addWidget(self.label_y_scale)
        self.sliderYscale = QtWidgets.QSlider(SendRecvDialog)
        self.sliderYscale.setMinimum(1)
        self.sliderYscale.setMaximum(1000)
        self.sliderYscale.setProperty("value", 1)
        self.sliderYscale.setOrientation(QtCore.Qt.Vertical)
        self.sliderYscale.setTickInterval(1)
        self.sliderYscale.setObjectName("sliderYscale")
        self.verticalLayout_5.addWidget(self.sliderYscale)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(SendRecvDialog)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SendRecvDialog)
        SendRecvDialog.setTabOrder(self.cbDevice, self.lineEditIP)
        SendRecvDialog.setTabOrder(self.lineEditIP, self.spinBoxFreq)
        SendRecvDialog.setTabOrder(self.spinBoxFreq, self.spinBoxSampleRate)
        SendRecvDialog.setTabOrder(self.spinBoxSampleRate, self.spinBoxBandwidth)
        SendRecvDialog.setTabOrder(self.spinBoxBandwidth, self.spinBoxGain)
        SendRecvDialog.setTabOrder(self.spinBoxGain, self.spinBoxNRepeat)
        SendRecvDialog.setTabOrder(self.spinBoxNRepeat, self.btnStart)
        SendRecvDialog.setTabOrder(self.btnStart, self.btnStop)
        SendRecvDialog.setTabOrder(self.btnStop, self.btnSave)
        SendRecvDialog.setTabOrder(self.btnSave, self.btnClear)
        SendRecvDialog.setTabOrder(self.btnClear, self.sliderYscale)
        SendRecvDialog.setTabOrder(self.sliderYscale, self.txtEditErrors)

    def retranslateUi(self, SendRecvDialog):
        _translate = QtCore.QCoreApplication.translate
        SendRecvDialog.setWindowTitle(_translate("SendRecvDialog", "Record Signal"))
        self.lineEditIP.setText(_translate("SendRecvDialog", "192.168.10.2"))
        self.labelGain.setText(_translate("SendRecvDialog", "Gain:"))
        self.labelBandWidth.setText(_translate("SendRecvDialog", "Bandwidth (Hz):"))
        self.cbDevice.setItemText(0, _translate("SendRecvDialog", "USRP"))
        self.cbDevice.setItemText(1, _translate("SendRecvDialog", "HackRF"))
        self.label_3.setText(_translate("SendRecvDialog", "Device:"))
        self.labelSampleRate.setText(_translate("SendRecvDialog", "Sample rate (Sps):"))
        self.labelIP.setText(_translate("SendRecvDialog", "IP address:"))
        self.labelPort.setText(_translate("SendRecvDialog", "Port number:"))
        self.spinBoxNRepeat.setSpecialValueText(_translate("SendRecvDialog", "Infinite"))
        self.labelFreq.setText(_translate("SendRecvDialog", "Frequency (Hz):"))
        self.labelNRepeat.setText(_translate("SendRecvDialog", "Repeat:"))
        self.btnLockBWSR.setText(_translate("SendRecvDialog", "..."))
        self.label_sniff_Noise.setText(_translate("SendRecvDialog", "Noise:"))
        self.label_sniff_Center.setText(_translate("SendRecvDialog", "Center:"))
        self.label_sniff_Modulation.setText(_translate("SendRecvDialog", "Modulation:"))
        self.combox_sniff_Modulation.setItemText(0, _translate("SendRecvDialog", "ASK"))
        self.combox_sniff_Modulation.setItemText(1, _translate("SendRecvDialog", "FSK"))
        self.combox_sniff_Modulation.setItemText(2, _translate("SendRecvDialog", "PSK"))
        self.label_sniff_OutputFile.setText(_translate("SendRecvDialog", "Output file:"))
        self.lineEdit_sniff_OutputFile.setPlaceholderText(_translate("SendRecvDialog", "None"))
        self.label_sniff_BitLength.setText(_translate("SendRecvDialog", "Bit Length:"))
        self.label_sniff_Tolerance.setText(_translate("SendRecvDialog", "Error Tolerance:"))
        self.comboBox_sniff_viewtype.setItemText(0, _translate("SendRecvDialog", "Bit"))
        self.comboBox_sniff_viewtype.setItemText(1, _translate("SendRecvDialog", "Hex"))
        self.comboBox_sniff_viewtype.setItemText(2, _translate("SendRecvDialog", "ASCII"))
        self.label_sniff_viewtype.setText(_translate("SendRecvDialog", "View:"))
        self.progressBar.setFormat(_translate("SendRecvDialog", "%v/%m"))
        self.lSamplesSentText.setText(_translate("SendRecvDialog", "Samples sent:"))
        self.lTimeText.setText(_translate("SendRecvDialog", "Time (in seconds):"))
        self.lSamplesCapturedText.setText(_translate("SendRecvDialog", "Samples captured:"))
        self.btnStart.setToolTip(_translate("SendRecvDialog", "Record signal"))
        self.btnStop.setToolTip(_translate("SendRecvDialog", "Stop recording"))
        self.btnSave.setText(_translate("SendRecvDialog", "Save..."))
        self.btnClear.setToolTip(_translate("SendRecvDialog", "Clear"))
        self.lSignalSizeText.setText(_translate("SendRecvDialog", "Signal size (in MiB):"))
        self.lSamplesCaptured.setText(_translate("SendRecvDialog", "0"))
        self.lTime.setText(_translate("SendRecvDialog", "0"))
        self.lSignalSize.setText(_translate("SendRecvDialog", "0"))
        self.lblRepeatText.setText(_translate("SendRecvDialog", "Current iteration:"))
        self.lblCurrentRepeatValue.setText(_translate("SendRecvDialog", "0"))
        self.label_7.setText(_translate("SendRecvDialog", "Hint: You can edit the raw signal before sending."))
        self.btnAccept.setText(_translate("SendRecvDialog", "Accept data"))
        self.label_y_scale.setText(_translate("SendRecvDialog", "Y-Scale"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
from urh.ui.views.EditableGraphicView import EditableGraphicView
from urh.ui.views.LiveGraphicView import LiveGraphicView
from . import urh_rc
