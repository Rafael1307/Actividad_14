from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from ui_mainwindow2 import Ui_MainWindow
from particula import Particula
from admin import Administrador
from pprint import pprint, pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administra = Administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.AgFinal_pushButton.clicked.connect(self.click_capturar)
        self.ui.AgInicio_pushButton.clicked.connect(self.click_capturar_Inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.actio_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.actio_guardar_archivo)
        self.ui.actionPor_ID.triggered.connect(self.Ordenar_ID)
        self.ui.actionPor_Distancia.triggered.connect(self.Ordenar_Distancia)
        self.ui.actionPor_Velocidad.triggered.connect(self.Ordenar_Velocida)
        self.ui.Mostrar_Tabla_PushButton.clicked.connect(self.mostrar_tabla)
        self.ui.Buscar_Tabla_PushButton.clicked.connect(self.buscar_id)
        self.ui.Dibujar_dibujo_pushButton.clicked.connect(self.Dibujar_part)
        self.ui.Limpiar_dibujo_pushButton.clicked.connect(self.Limpiar_part)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.sceneG = QGraphicsScene()
        self.ui.Grafo_graphicsView.setScene(self.sceneG)

        self.ui.Grafo_L_pushButton.clicked.connect(self.Limpiar_Grafo)
        self.ui.Grafo_M_pushButton.clicked.connect(self.Mostrar_Grafo)

    @Slot()
    def Mostrar_Grafo(self):
        grafo = dict()
        for particula in self.administra:
            o_x = str(particula.origen_x).upper()
            o_y = str(particula.origen_y).upper()
            d_x = str(particula.destino_x).upper()
            d_y = str(particula.destino_y).upper()
            peso = int(particula.distancia)
            origen = o_x, o_y
            destino = d_x, d_y

            arista_o_d = (d_x, d_y, peso)
            arista_d_o = (o_x, o_y, peso)

            if origen in grafo:
                grafo[origen].append(arista_o_d)
            else:
                grafo[origen] = [arista_o_d]
            if destino in grafo:
                grafo[destino].append(arista_d_o)
            else:
                grafo[destino] = [arista_d_o]
        strn = pformat(grafo, width=40, indent=1)
        pprint(grafo, width=40)
        for particula in self.administra:
            pen = QPen()
            pen.setWidth(2)
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)
            self.sceneG.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen)
            self.sceneG.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)
            self.sceneG.addLine(particula.origen_x + 3, particula.origen_y + 3, particula.destino_x, particula.destino_y, pen)
        self.ui.Grafo_plainTextEdit.clear()
        self.ui.Grafo_plainTextEdit.insertPlainText(strn)

    @Slot()
    def Limpiar_Grafo(self):
        self.sceneG.clear()
        self.ui.Grafo_plainTextEdit.clear()

    @Slot()
    def Dibujar_part(self):
        for particula in self.administra:
            pen = QPen()
            pen.setWidth(2)
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)
            self.scene.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)
            self.scene.addLine(particula.origen_x + 3, particula.origen_y + 3, particula.destino_x, particula.destino_y, pen)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
        if event.delta() > 0:
            self.ui.Grafo_graphicsView.scale(1.2, 1.2)
        else:
            self.ui.Grafo_graphicsView.scale(0.8, 0.8)

    @Slot()
    def Limpiar_part(self):
        self.scene.clear()


    @Slot()
    def buscar_id(self):
        identificador = self.ui.Buscar_Tabla_lineEdit.text()
        Encontrado = False
        for particula in self.administra:
            if identificador == str(particula.ide):
                self.ui.Tabla.clear()
                self.ui.Tabla.setRowCount(1)
                ide_widget = QTableWidgetItem(str(particula.ide))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                self.ui.Tabla.setItem(0, 0, ide_widget)
                self.ui.Tabla.setItem(0, 1, origen_x_widget)
                self.ui.Tabla.setItem(0, 2, origen_y_widget)
                self.ui.Tabla.setItem(0, 3, destino_x_widget)
                self.ui.Tabla.setItem(0, 4, destino_y_widget)
                self.ui.Tabla.setItem(0, 5, velocidad_widget)
                self.ui.Tabla.setItem(0, 6, distancia_widget)
                self.ui.Tabla.setItem(0, 7, red_widget)
                self.ui.Tabla.setItem(0, 8, green_widget)
                self.ui.Tabla.setItem(0, 9, blue_widget)
                Encontrado = True
                return
        if not Encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                "La particula con identificador " + identificador + " no fue encontrada"
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.Tabla.setColumnCount(10)
        headers = ["ID","Origen_X","Origen_Y","Destino_X","Destino_Y","Velocidad","Distancia","Red","Green","Blue"]
        self.ui.Tabla.setHorizontalHeaderLabels(headers)
        self.ui.Tabla.setRowCount(len(self.administra))
        row = 0
        for particula in self.administra:
            ide_widget = QTableWidgetItem(str(particula.ide))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            self.ui.Tabla.setItem(row, 0, ide_widget)
            self.ui.Tabla.setItem(row, 1, origen_x_widget)
            self.ui.Tabla.setItem(row, 2, origen_y_widget)
            self.ui.Tabla.setItem(row, 3, destino_x_widget)
            self.ui.Tabla.setItem(row, 4, destino_y_widget)
            self.ui.Tabla.setItem(row, 5, velocidad_widget)
            self.ui.Tabla.setItem(row, 6, distancia_widget)
            self.ui.Tabla.setItem(row, 7, red_widget)
            self.ui.Tabla.setItem(row, 8, green_widget)
            self.ui.Tabla.setItem(row, 9, blue_widget)
            row += 1

    @Slot()
    def actio_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administra.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def actio_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.administra.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pud crear el archivo " + ubicacion
            )

    @Slot()
    def Ordenar_ID(self):
        self.administra.ordenar()

    @Slot()
    def Ordenar_Distancia(self):
        self.administra.ordenar_distancia()

    @Slot()
    def Ordenar_Velocida(self):
        self.administra.ordenar_velocidad()

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.administra))

    @Slot()
    def click_capturar(self):
        Ide = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.ColorRed_spinBox.value()
        Green = self.ui.ColorGreen_spinBox.value()
        Blue = self.ui.ColorBlue_spinBox.value()
        particula = Particula(Ide, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.administra.agregar_final(particula)

    @Slot()
    def click_capturar_Inicio(self):
        Ide = self.ui.ID_spinBox.value()
        OrigenX = self.ui.OrigenX_spinBox.value()
        OrigenY = self.ui.OrigenY_spinBox.value()
        DestinoX = self.ui.DestinoX_spinBox.value()
        DestinoY = self.ui.DestinoY_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.ColorRed_spinBox.value()
        Green = self.ui.ColorGreen_spinBox.value()
        Blue = self.ui.ColorBlue_spinBox.value()
        particula = Particula(Ide, OrigenX, OrigenY, DestinoX, DestinoY, Velocidad, Red, Green, Blue)
        self.administra.agregar_inicio(particula)