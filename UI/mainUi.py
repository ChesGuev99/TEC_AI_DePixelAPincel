# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Del Píxel al Pincel - Propiedades.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_properties_Dialog(object):
    def setupUi(self, properties_Dialog):
        properties_Dialog.setObjectName("properties_Dialog")
        properties_Dialog.resize(404, 360)
        self.imageSelection_Box = QtWidgets.QGroupBox(properties_Dialog)
        self.imageSelection_Box.setGeometry(QtCore.QRect(10, 10, 381, 61))
        self.imageSelection_Box.setObjectName("imageSelection_Box")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.imageSelection_Box)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imagePath_textInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.imagePath_textInput.setObjectName("imagePath_textInput")
        self.horizontalLayout.addWidget(self.imagePath_textInput)
        self.imageSearch_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.imageSearch_Button.setObjectName("imageSearch_Button")
        self.horizontalLayout.addWidget(self.imageSearch_Button)
        self.iteration_Box = QtWidgets.QGroupBox(properties_Dialog)
        self.iteration_Box.setGeometry(QtCore.QRect(10, 80, 181, 61))
        self.iteration_Box.setObjectName("iteration_Box")
        self.iteration_spinBox = QtWidgets.QSpinBox(self.iteration_Box)
        self.iteration_spinBox.setGeometry(QtCore.QRect(10, 20, 159, 24))
        self.iteration_spinBox.setObjectName("iteration_spinBox")
        self.population_Box = QtWidgets.QGroupBox(properties_Dialog)
        self.population_Box.setGeometry(QtCore.QRect(210, 80, 181, 61))
        self.population_Box.setObjectName("population_Box")
        self.population_spinBox = QtWidgets.QSpinBox(self.population_Box)
        self.population_spinBox.setGeometry(QtCore.QRect(10, 20, 159, 24))
        self.population_spinBox.setObjectName("population_spinBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(properties_Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 150, 361, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imagePreview_View = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.imagePreview_View.setText("")
        self.imagePreview_View.setScaledContents(True)
        self.imagePreview_View.setObjectName("imagePreview_View")
        self.horizontalLayout_2.addWidget(self.imagePreview_View)
        self.generate_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.generate_Button.setObjectName("generate_Button")
        self.horizontalLayout_2.addWidget(self.generate_Button)

        self.retranslateUi(properties_Dialog)
        QtCore.QMetaObject.connectSlotsByName(properties_Dialog)

    def retranslateUi(self, properties_Dialog):
        _translate = QtCore.QCoreApplication.translate
        properties_Dialog.setWindowTitle(_translate("properties_Dialog", "Dialog"))
        self.imageSelection_Box.setTitle(_translate("properties_Dialog", "Selección de Imagen"))
        self.imageSearch_Button.setText(_translate("properties_Dialog", "Buscar imagen"))
        self.iteration_Box.setTitle(_translate("properties_Dialog", "Cantidad de Iteraciones"))
        self.population_Box.setTitle(_translate("properties_Dialog", "Tamaño de Población"))
        self.generate_Button.setText(_translate("properties_Dialog", "Transformar \n"
"Imagen"))