# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\17730\Desktop\dsm\DSM_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from generate_dsm import Load_Config, Sat_Cas_RED_Gen_DSM

class EmittingStream(QtCore.QObject):
        textWritten = QtCore.pyqtSignal(str)
        def write(self, text):
            self.textWritten.emit(str(text))
            QApplication.processEvents()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(600, 40, 521, 411))
        self.graphicsView.setObjectName("graphicsView")
        self.label_DSM = QtWidgets.QLabel(self.centralwidget)
        self.label_DSM.setGeometry(QtCore.QRect(600, -1, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_DSM.setFont(font)
        self.label_DSM.setObjectName("label_DSM")
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setGeometry(QtCore.QRect(40, 340, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_Time.setFont(font)
        self.label_Time.setLineWidth(3)
        self.label_Time.setTextFormat(QtCore.Qt.PlainText)
        self.label_Time.setObjectName("label_Time")
        self.lineEdit_Time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Time.setGeometry(QtCore.QRect(110, 340, 113, 20))
        self.lineEdit_Time.setObjectName("lineEdit_Time")
        self.lineEdit_CE90 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_CE90.setGeometry(QtCore.QRect(110, 380, 113, 20))
        self.lineEdit_CE90.setText("")
        self.lineEdit_CE90.setObjectName("lineEdit_CE90")
        self.label_CE90 = QtWidgets.QLabel(self.centralwidget)
        self.label_CE90.setGeometry(QtCore.QRect(40, 380, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_CE90.setFont(font)
        self.label_CE90.setLineWidth(3)
        self.label_CE90.setTextFormat(QtCore.Qt.PlainText)
        self.label_CE90.setObjectName("label_CE90")
        self.lineEdit_LE90 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LE90.setGeometry(QtCore.QRect(110, 420, 113, 20))
        self.lineEdit_LE90.setText("")
        self.lineEdit_LE90.setObjectName("lineEdit_LE90")
        self.label_LE90 = QtWidgets.QLabel(self.centralwidget)
        self.label_LE90.setGeometry(QtCore.QRect(40, 420, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_LE90.setFont(font)
        self.label_LE90.setLineWidth(3)
        self.label_LE90.setTextFormat(QtCore.Qt.PlainText)
        self.label_LE90.setObjectName("label_LE90")
        self.label_min = QtWidgets.QLabel(self.centralwidget)
        self.label_min.setGeometry(QtCore.QRect(230, 340, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_min.setFont(font)
        self.label_min.setLineWidth(3)
        self.label_min.setTextFormat(QtCore.Qt.PlainText)
        self.label_min.setObjectName("label_min")
        self.label_CE90_m = QtWidgets.QLabel(self.centralwidget)
        self.label_CE90_m.setGeometry(QtCore.QRect(230, 380, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_CE90_m.setFont(font)
        self.label_CE90_m.setLineWidth(3)
        self.label_CE90_m.setTextFormat(QtCore.Qt.PlainText)
        self.label_CE90_m.setObjectName("label_CE90_m")
        self.label_LE90_m = QtWidgets.QLabel(self.centralwidget)
        self.label_LE90_m.setGeometry(QtCore.QRect(230, 420, 60, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_LE90_m.setFont(font)
        self.label_LE90_m.setLineWidth(3)
        self.label_LE90_m.setTextFormat(QtCore.Qt.PlainText)
        self.label_LE90_m.setObjectName("label_LE90_m")
        self.assessment = QtWidgets.QLabel(self.centralwidget)
        self.assessment.setGeometry(QtCore.QRect(30, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.assessment.setFont(font)
        self.assessment.setObjectName("assessment")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 40, 241, 411))
        self.textEdit.setObjectName("textEdit")
        self.label_detial = QtWidgets.QLabel(self.centralwidget)
        self.label_detial.setGeometry(QtCore.QRect(340, -1, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_detial.setFont(font)
        self.label_detial.setObjectName("label_detial")
        self.label_model = QtWidgets.QLabel(self.centralwidget)
        self.label_model.setGeometry(QtCore.QRect(30, 60, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_model.setFont(font)
        self.label_model.setLineWidth(3)
        self.label_model.setTextFormat(QtCore.Qt.PlainText)
        self.label_model.setObjectName("label_model")
        self.comboBox_model = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_model.setGeometry(QtCore.QRect(130, 50, 181, 31))
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(30, 110, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_camera.setFont(font)
        self.label_camera.setObjectName("label_camera")
        self.comboBox_camera = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_camera.setGeometry(QtCore.QRect(130, 100, 181, 31))
        self.comboBox_camera.setObjectName("comboBox_camera")
        self.comboBox_camera.addItem("")
        self.comboBox_camera.addItem("")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(30, 160, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.button_path = QtWidgets.QPushButton(self.centralwidget)
        self.button_path.setGeometry(QtCore.QRect(130, 150, 181, 31))
        self.button_path.setObjectName("button_path")
        self.label_config = QtWidgets.QLabel(self.centralwidget)
        self.label_config.setGeometry(QtCore.QRect(30, 210, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_config.setFont(font)
        self.label_config.setObjectName("label_config")
        self.button_config = QtWidgets.QPushButton(self.centralwidget)
        self.button_config.setGeometry(QtCore.QRect(130, 200, 181, 31))
        self.button_config.setObjectName("button_config")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(30, 260, 281, 31))
        self.button_submit.setObjectName("button_submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #重定向输出
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

        # button按钮回调函数
        self.button_path.clicked.connect(self.openSource)
        self.button_config.clicked.connect(self.openconfig)
        self.button_submit.clicked.connect(self.generate_dsm)

    def normalOutputWritten(self, text):
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText(text)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.ensureCursorVisible()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DSM generator"))
        self.label_DSM.setText(_translate("MainWindow", "DSM结果"))
        self.input.setText(_translate("MainWindow", "输入"))
        self.label_Time.setText(_translate("MainWindow", "Time"))
        self.label_CE90.setText(_translate("MainWindow", "CE90"))
        self.label_LE90.setText(_translate("MainWindow", "LE90"))
        self.label_min.setText(_translate("MainWindow", "min"))
        self.label_CE90_m.setText(_translate("MainWindow", "m"))
        self.label_LE90_m.setText(_translate("MainWindow", "m"))
        self.assessment.setText(_translate("MainWindow", "评估指标"))
        self.label_detial.setText(_translate("MainWindow", "生成细节"))
        self.label_model.setText(_translate("MainWindow", "网络模型"))
        self.comboBox_model.setItemText(0, _translate("MainWindow", "fast-8"))
        self.comboBox_model.setItemText(1, _translate("MainWindow", "fast-16"))
        self.comboBox_model.setItemText(2, _translate("MainWindow", "red"))
        self.comboBox_model.setItemText(3, _translate("MainWindow", "cas"))
        self.label_camera.setText(_translate("MainWindow", "成像模型"))
        self.comboBox_camera.setItemText(0, _translate("MainWindow", "rpc"))
        self.comboBox_camera.setItemText(1, _translate("MainWindow", "pinhole"))
        self.label_path.setText(_translate("MainWindow", "影像目录"))
        self.button_path.setText(_translate("MainWindow", "选择目录"))
        self.label_config.setText(_translate("MainWindow", "配置文件"))
        self.button_config.setText(_translate("MainWindow", "选择文件"))
        self.button_submit.setText(_translate("MainWindow", "生成DSM"))

    def openSource(self):
        self.Source = QFileDialog.getExistingDirectory(None, "打开文件夹", "C:/")
           
    def openconfig(self):
        config, _ = QFileDialog.getOpenFileName(None, "打开图片", "C:/", "*.txt")
        self.config = Load_Config(config)

           
    def generate_dsm(self):
        model = self.comboBox_model.currentText()
        camera = self.comboBox_camera.currentText()
        gen_dsm = Sat_Cas_RED_Gen_DSM(self.config, self.Source, model, camera)
        time = gen_dsm.generate_dsm()
        self.lineEdit_Time.setText(time)
        tif = self.Source+"/Output/mosaic_dsm/mosaic_dsm.tif"
        print(tif)
        

if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 