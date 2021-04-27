# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_5.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 723)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 541, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.line_train_folder = QtWidgets.QLineEdit(self.groupBox_4)
        self.line_train_folder.setGeometry(QtCore.QRect(60, 40, 201, 21))
        self.line_train_folder.setObjectName("line_train_folder")
        self.btn_train_browse = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_train_browse.setGeometry(QtCore.QRect(270, 30, 81, 31))
        self.btn_train_browse.setObjectName("btn_train_browse")
        self.btn_train_load = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_train_load.setGeometry(QtCore.QRect(360, 30, 81, 31))
        self.btn_train_load.setObjectName("btn_train_load")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 511, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(450, 40, 21, 21))
        self.label_4.setObjectName("label_4")
        self.spin_train_n = QtWidgets.QSpinBox(self.groupBox_4)
        self.spin_train_n.setGeometry(QtCore.QRect(470, 30, 61, 31))
        self.spin_train_n.setMinimum(1)
        self.spin_train_n.setMaximum(9999)
        self.spin_train_n.setProperty("value", 100)
        self.spin_train_n.setObjectName("spin_train_n")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 130, 541, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_7.setObjectName("label_7")
        self.line_test_folder = QtWidgets.QLineEdit(self.groupBox_5)
        self.line_test_folder.setGeometry(QtCore.QRect(60, 40, 201, 21))
        self.line_test_folder.setObjectName("line_test_folder")
        self.btn_test_browse = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_test_browse.setGeometry(QtCore.QRect(270, 30, 81, 31))
        self.btn_test_browse.setObjectName("btn_test_browse")
        self.btn_test_load = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_test_load.setGeometry(QtCore.QRect(360, 30, 81, 31))
        self.btn_test_load.setObjectName("btn_test_load")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 511, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(450, 40, 21, 21))
        self.label_10.setObjectName("label_10")
        self.spin_test_n = QtWidgets.QSpinBox(self.groupBox_5)
        self.spin_test_n.setGeometry(QtCore.QRect(470, 30, 61, 31))
        self.spin_test_n.setMinimum(1)
        self.spin_test_n.setMaximum(9999)
        self.spin_test_n.setProperty("value", 100)
        self.spin_test_n.setObjectName("spin_test_n")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 541, 81))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.label_6.setObjectName("label_6")
        self.spin_tfn_epochs = QtWidgets.QSpinBox(self.groupBox)
        self.spin_tfn_epochs.setGeometry(QtCore.QRect(140, 30, 61, 31))
        self.spin_tfn_epochs.setMinimum(1)
        self.spin_tfn_epochs.setMaximum(9999)
        self.spin_tfn_epochs.setProperty("value", 10)
        self.spin_tfn_epochs.setObjectName("spin_tfn_epochs")
        self.btn_tfn_train = QtWidgets.QPushButton(self.groupBox)
        self.btn_tfn_train.setGeometry(QtCore.QRect(230, 30, 81, 31))
        self.btn_tfn_train.setObjectName("btn_tfn_train")
        self.btn_tfn_save = QtWidgets.QPushButton(self.groupBox)
        self.btn_tfn_save.setGeometry(QtCore.QRect(340, 30, 81, 31))
        self.btn_tfn_save.setObjectName("btn_tfn_save")
        self.btn_tfn_load = QtWidgets.QPushButton(self.groupBox)
        self.btn_tfn_load.setGeometry(QtCore.QRect(430, 30, 81, 31))
        self.btn_tfn_load.setObjectName("btn_tfn_load")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 340, 541, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cvl_image = QtWidgets.QLabel(self.groupBox_2)
        self.cvl_image.setGeometry(QtCore.QRect(170, 80, 320, 240))
        self.cvl_image.setText("")
        self.cvl_image.setObjectName("cvl_image")
        self.btn_tfn_predict = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_tfn_predict.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.btn_tfn_predict.setObjectName("btn_tfn_predict")
        self.label_tfn_result = QtWidgets.QLabel(self.groupBox_2)
        self.label_tfn_result.setGeometry(QtCore.QRect(200, 40, 311, 20))
        self.label_tfn_result.setObjectName("label_tfn_result")
        self.btn_tfn_predict_camera = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_tfn_predict_camera.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.btn_tfn_predict_camera.setObjectName("btn_tfn_predict_camera")
        self.camera_id = QtWidgets.QSpinBox(self.groupBox_2)
        self.camera_id.setGeometry(QtCore.QRect(130, 90, 41, 31))
        self.camera_id.setMinimum(0)
        self.camera_id.setMaximum(9999)
        self.camera_id.setProperty("value", 0)
        self.camera_id.setObjectName("camera_id")
        self.btn_tfn_predict_camera_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_tfn_predict_camera_stop.setGeometry(QtCore.QRect(10, 120, 121, 31))
        self.btn_tfn_predict_camera_stop.setObjectName("btn_tfn_predict_camera_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LR5 TF"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Train dataset"))
        self.label_2.setText(_translate("MainWindow", "Folder:"))
        self.line_train_folder.setText(_translate("MainWindow", "LR5_data\\Train"))
        self.btn_train_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_train_load.setText(_translate("MainWindow", "Load"))
        self.label_3.setText(_translate("MainWindow", "Note: The folder should contain files of all 4 classes in the {0-3}_{0-N}.png format."))
        self.label_4.setText(_translate("MainWindow", "N:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Test dataset"))
        self.label_7.setText(_translate("MainWindow", "Folder:"))
        self.line_test_folder.setText(_translate("MainWindow", "LR5_data\\Test"))
        self.btn_test_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_test_load.setText(_translate("MainWindow", "Load"))
        self.label_8.setText(_translate("MainWindow", "Note: The folder should contain files of all 4 classes in the {0-3}_{0-N}.png format."))
        self.label_10.setText(_translate("MainWindow", "N:"))
        self.groupBox.setTitle(_translate("MainWindow", "Network"))
        self.label_6.setText(_translate("MainWindow", "Number of epochs:"))
        self.btn_tfn_train.setText(_translate("MainWindow", "Train"))
        self.btn_tfn_save.setText(_translate("MainWindow", "Save"))
        self.btn_tfn_load.setText(_translate("MainWindow", "Load"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Network tester"))
        self.btn_tfn_predict.setText(_translate("MainWindow", "Predict random image"))
        self.label_tfn_result.setText(_translate("MainWindow", "NOTHING TO SAY"))
        self.btn_tfn_predict_camera.setText(_translate("MainWindow", "Camera predict"))
        self.btn_tfn_predict_camera_stop.setText(_translate("MainWindow", "Stop"))

