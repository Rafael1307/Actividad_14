# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(594, 502)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPor_ID = QAction(MainWindow)
        self.actionPor_ID.setObjectName(u"actionPor_ID")
        self.actionPor_Distancia = QAction(MainWindow)
        self.actionPor_Distancia.setObjectName(u"actionPor_Distancia")
        self.actionPor_Velocidad = QAction(MainWindow)
        self.actionPor_Velocidad.setObjectName(u"actionPor_Velocidad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoX_spinBox, 3, 2, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")
        self.ID_spinBox.setMaximum(99)

        self.gridLayout_2.addWidget(self.ID_spinBox, 0, 2, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.DestinoY_spinBox, 4, 2, 1, 1)

        self.AgInicio_pushButton = QPushButton(self.groupBox)
        self.AgInicio_pushButton.setObjectName(u"AgInicio_pushButton")

        self.gridLayout_2.addWidget(self.AgInicio_pushButton, 7, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 2)

        self.AgFinal_pushButton = QPushButton(self.groupBox)
        self.AgFinal_pushButton.setObjectName(u"AgFinal_pushButton")

        self.gridLayout_2.addWidget(self.AgFinal_pushButton, 7, 1, 1, 1)

        self.OrigenX_label = QLabel(self.groupBox)
        self.OrigenX_label.setObjectName(u"OrigenX_label")

        self.gridLayout_2.addWidget(self.OrigenX_label, 1, 0, 1, 2)

        self.OrigenY_label = QLabel(self.groupBox)
        self.OrigenY_label.setObjectName(u"OrigenY_label")

        self.gridLayout_2.addWidget(self.OrigenY_label, 2, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 2)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")

        self.gridLayout_2.addWidget(self.Velocidad_spinBox, 5, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.ColorRed_spinBox = QSpinBox(self.groupBox_2)
        self.ColorRed_spinBox.setObjectName(u"ColorRed_spinBox")
        self.ColorRed_spinBox.setMaximum(255)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ColorRed_spinBox)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.ColorGreen_spinBox = QSpinBox(self.groupBox_2)
        self.ColorGreen_spinBox.setObjectName(u"ColorGreen_spinBox")
        self.ColorGreen_spinBox.setMaximum(255)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ColorGreen_spinBox)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.ColorBlue_spinBox = QSpinBox(self.groupBox_2)
        self.ColorBlue_spinBox.setObjectName(u"ColorBlue_spinBox")
        self.ColorBlue_spinBox.setMaximum(255)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ColorBlue_spinBox)


        self.gridLayout_2.addWidget(self.groupBox_2, 6, 0, 1, 2)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.OrigenY_spinBox, 2, 2, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.OrigenX_spinBox, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 2)

        self.ID_label = QLabel(self.groupBox)
        self.ID_label.setObjectName(u"ID_label")

        self.gridLayout_2.addWidget(self.ID_label, 0, 0, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_2.addWidget(self.Mostrar_pushButton, 7, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Buscar_Tabla_PushButton = QPushButton(self.tab_2)
        self.Buscar_Tabla_PushButton.setObjectName(u"Buscar_Tabla_PushButton")

        self.gridLayout_4.addWidget(self.Buscar_Tabla_PushButton, 1, 1, 1, 1)

        self.Mostrar_Tabla_PushButton = QPushButton(self.tab_2)
        self.Mostrar_Tabla_PushButton.setObjectName(u"Mostrar_Tabla_PushButton")

        self.gridLayout_4.addWidget(self.Mostrar_Tabla_PushButton, 1, 2, 1, 1)

        self.Buscar_Tabla_lineEdit = QLineEdit(self.tab_2)
        self.Buscar_Tabla_lineEdit.setObjectName(u"Buscar_Tabla_lineEdit")

        self.gridLayout_4.addWidget(self.Buscar_Tabla_lineEdit, 1, 0, 1, 1)

        self.Tabla = QTableWidget(self.tab_2)
        self.Tabla.setObjectName(u"Tabla")

        self.gridLayout_4.addWidget(self.Tabla, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Grafo_plainTextEdit = QPlainTextEdit(self.tab_4)
        self.Grafo_plainTextEdit.setObjectName(u"Grafo_plainTextEdit")

        self.gridLayout_6.addWidget(self.Grafo_plainTextEdit, 0, 0, 1, 1)

        self.Grafo_graphicsView = QGraphicsView(self.tab_4)
        self.Grafo_graphicsView.setObjectName(u"Grafo_graphicsView")

        self.gridLayout_6.addWidget(self.Grafo_graphicsView, 0, 1, 1, 1)

        self.Grafo_L_pushButton = QPushButton(self.tab_4)
        self.Grafo_L_pushButton.setObjectName(u"Grafo_L_pushButton")

        self.gridLayout_6.addWidget(self.Grafo_L_pushButton, 2, 1, 1, 1)

        self.Grafo_M_pushButton = QPushButton(self.tab_4)
        self.Grafo_M_pushButton.setObjectName(u"Grafo_M_pushButton")

        self.gridLayout_6.addWidget(self.Grafo_M_pushButton, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.Dibujar_dibujo_pushButton = QPushButton(self.tab_3)
        self.Dibujar_dibujo_pushButton.setObjectName(u"Dibujar_dibujo_pushButton")

        self.gridLayout_5.addWidget(self.Dibujar_dibujo_pushButton, 1, 0, 1, 1)

        self.Limpiar_dibujo_pushButton = QPushButton(self.tab_3)
        self.Limpiar_dibujo_pushButton.setObjectName(u"Limpiar_dibujo_pushButton")

        self.gridLayout_5.addWidget(self.Limpiar_dibujo_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 594, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.actionPor_ID)
        self.menuOrdenar.addAction(self.actionPor_Distancia)
        self.menuOrdenar.addAction(self.actionPor_Velocidad)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionPor_ID.setText(QCoreApplication.translate("MainWindow", u"Por ID", None))
        self.actionPor_Distancia.setText(QCoreApplication.translate("MainWindow", u"Por Distancia", None))
        self.actionPor_Velocidad.setText(QCoreApplication.translate("MainWindow", u"Por Velocidad", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.AgInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.AgFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.OrigenX_label.setText(QCoreApplication.translate("MainWindow", u"Origen en X: ", None))
        self.OrigenY_label.setText(QCoreApplication.translate("MainWindow", u"Origen en Y: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color (RGB)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.ID_label.setText(QCoreApplication.translate("MainWindow", u"ID: ", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar_Tabla_PushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Tabla_PushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.Buscar_Tabla_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID particula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Grafo_L_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.Grafo_M_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.Dibujar_dibujo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_dibujo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
    # retranslateUi

