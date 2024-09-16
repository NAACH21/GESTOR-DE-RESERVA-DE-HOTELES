import re
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QCoreApplication, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QFileDialog, QPushButton
import conexion

class Ui_GestHabi(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 626)
        MainWindow.setGeometry(
            (MainWindow.screen().geometry().width() - MainWindow.geometry().width()) // 2,
            (MainWindow.screen().geometry().height() - MainWindow.geometry().height()) // 2,
            MainWindow.geometry().width(),
            MainWindow.geometry().height()
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1101, 681))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(250, 20, 451, 21))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(12, 96, 204);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1091, 20))
        self.line.setStyleSheet("color: rgb(14, 138, 229);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtNPiso = QtWidgets.QLineEdit(parent=self.widget)
        self.txtNPiso.setGeometry(QtCore.QRect(180, 90, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNPiso.setFont(font)
        self.txtNPiso.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtNPiso.setObjectName("txtNPiso")
        self.cmbTipoHabitacion = QtWidgets.QComboBox(parent=self.widget)
        self.cmbTipoHabitacion.setGeometry(QtCore.QRect(20, 90, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbTipoHabitacion.setFont(font)
        self.cmbTipoHabitacion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbTipoHabitacion.setObjectName("cmbTipoHabitacion")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.setItemText(0, "")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.cmbTipoHabitacion.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(180, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 70, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtTamanio = QtWidgets.QLineEdit(parent=self.widget)
        self.txtTamanio.setGeometry(QtCore.QRect(260, 90, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtTamanio.setFont(font)
        self.txtTamanio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtTamanio.setObjectName("txtTamanio")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(360, 70, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtDescripcion = QtWidgets.QLineEdit(parent=self.widget)
        self.txtDescripcion.setGeometry(QtCore.QRect(360, 90, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDescripcion.setFont(font)
        self.txtDescripcion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtNCamas = QtWidgets.QLineEdit(parent=self.widget)
        self.txtNCamas.setGeometry(QtCore.QRect(20, 150, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNCamas.setFont(font)
        self.txtNCamas.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtNCamas.setObjectName("txtNCamas")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(110, 130, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cmbTipoBanio = QtWidgets.QComboBox(parent=self.widget)
        self.cmbTipoBanio.setGeometry(QtCore.QRect(110, 150, 141, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbTipoBanio.setFont(font)
        self.cmbTipoBanio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbTipoBanio.setObjectName("cmbTipoBanio")
        self.cmbTipoBanio.addItem("")
        self.cmbTipoBanio.setItemText(0, "")
        self.cmbTipoBanio.addItem("")
        self.cmbTipoBanio.addItem("")
        self.txtPrecio = QtWidgets.QLineEdit(parent=self.widget)
        self.txtPrecio.setGeometry(QtCore.QRect(260, 150, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPrecio.setFont(font)
        self.txtPrecio.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtPrecio.setObjectName("txtPrecio")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(260, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cmbEstado = QtWidgets.QComboBox(parent=self.widget)
        self.cmbEstado.setGeometry(QtCore.QRect(360, 150, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbEstado.setFont(font)
        self.cmbEstado.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbEstado.setObjectName("cmbEstado")
        self.cmbEstado.addItem("")
        self.cmbEstado.setItemText(0, "")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(360, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.btnAgregar = QtWidgets.QPushButton(parent=self.widget)
        self.btnAgregar.setGeometry(QtCore.QRect(200, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet(u"\n"
                                      "QPushButton {\n"
                                      "    border-radius: 8px;\n"
                                      "    background-color: rgb(15, 121, 255);\n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: normal; \n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(24, 71, 113); \n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: bold; \n"
                                      "}\n"
                                      "")
        self.btnAgregar.setObjectName("btnAgregar")
        self.tblHabitacion = QtWidgets.QTableWidget(parent=self.widget)
        self.tblHabitacion.setGeometry(QtCore.QRect(20, 320, 911, 291))
        self.tblHabitacion.setMaximumSize(QtCore.QSize(96100, 16777215))
        self.tblHabitacion.setStyleSheet("background-color: rgb(226, 245, 255);\n"
"border-radius:8px;\n"
"")
        self.tblHabitacion.setObjectName("tblHabitacion")
        self.tblHabitacion.setColumnCount(9)
        self.tblHabitacion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(8, item)
        self.tblHabitacion.verticalHeader().setMinimumSectionSize(24)
        self.btnEliminar = QtWidgets.QPushButton(parent=self.widget)
        self.btnEliminar.setGeometry(QtCore.QRect(320, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setStyleSheet(u"\n"
                                      "QPushButton {\n"
                                      "    border-radius: 8px;\n"
                                      "    background-color: rgb(15, 121, 255);\n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: normal; \n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(24, 71, 113); \n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: bold; \n"
                                      "}\n"
                                      "")
        self.btnEliminar.setObjectName("btnEliminar")
        self.txtBuscar = QtWidgets.QLineEdit(parent=self.widget)
        self.txtBuscar.setGeometry(QtCore.QRect(20, 280, 281, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:8px;")
        self.txtBuscar.setObjectName("txtBuscar")
        self.btnBuscar = QtWidgets.QPushButton(parent=self.widget)
        self.btnBuscar.setGeometry(QtCore.QRect(320, 280, 101, 24))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setStyleSheet(u"\n"
                                      "QPushButton {\n"
                                      "    border-radius: 8px;\n"
                                      "    background-color: rgb(15, 121, 255);\n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: normal; \n"
                                      "    border: none;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(24, 71, 113); \n"
                                      "    color: rgb(255, 255, 255); \n"
                                      "    font-weight: bold; \n"
                                      "}\n"
                                      "")
        self.btnBuscar.setObjectName("btnBuscar")
        self.txtImagenHabitacion = QtWidgets.QLabel(parent=self.widget)
        self.txtImagenHabitacion.setGeometry(QtCore.QRect(630, 90, 301, 211))
        self.txtImagenHabitacion.setText("")
        self.txtImagenHabitacion.setPixmap(QtGui.QPixmap(":/habitacion1.jpg"))
        self.txtImagenHabitacion.setScaledContents(True)
        self.txtImagenHabitacion.setObjectName("txtImagenHabitacion")
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.widget)
        self.btnLimpiar.setGeometry(QtCore.QRect(440, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setStyleSheet(u"\n"
                                     "QPushButton {\n"
                                     "    border-radius: 8px;\n"
                                     "    background-color: rgb(15, 121, 255);\n"
                                     "    color: rgb(255, 255, 255); \n"
                                     "    font-weight: normal; \n"
                                     "    border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(24, 71, 113); \n"
                                     "    color: rgb(255, 255, 255); \n"
                                     "    font-weight: bold; \n"
                                     "}\n"
                                     "")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.txtLogo = QtWidgets.QLabel(parent=self.widget)
        self.txtLogo.setGeometry(QtCore.QRect(70, 0, 71, 61))
        self.txtLogo.setText("")
        self.txtLogo.setPixmap(QtGui.QPixmap("logo.png"))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.btnRegresar = QPushButton(self.widget)
        self.btnRegresar.setObjectName(u"btnRegresar")
        self.btnRegresar.setGeometry(QRect(50, 230, 121, 31))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.btnRegresar.setFont(font4)
        self.btnRegresar.setStyleSheet(u"QPushButton {\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(24, 71, 113); \n"
                                       "    color: rgb(255, 255, 255); \n"
                                       "    font-weight: normal; \n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(21, 105, 211); \n"
                                       "    color: rgb(255, 255, 255); \n"
                                       "    font-weight: bold; \n"
                                       "}\n"
                                       "")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Ancho de columnas de tablas
        self.tblHabitacion.setColumnWidth(0, 55)
        self.tblHabitacion.setColumnWidth(1, 110)
        self.tblHabitacion.setColumnWidth(2, 60)
        self.tblHabitacion.setColumnWidth(3, 70)
        self.tblHabitacion.setColumnWidth(4, 250)
        self.tblHabitacion.setColumnWidth(5, 60)
        self.tblHabitacion.setColumnWidth(7, 70)
        self.tblHabitacion.setColumnWidth(8, 100)

        self.llenaTblHabitacion(False, "")
        self.tblHabitacion.verticalHeader().setVisible(False)
        self.btnBuscar.clicked.connect(self.busqueda)
        self.filtro_busqueda = False
        self.cadBuscar = ""
        self.txtBuscar.textChanged.connect(self.busqueda)
        self.btnAgregar.clicked.connect(self.registroHabitacion)
        self.tblHabitacion.itemSelectionChanged.connect(self.selRegistroTabla)
        self.id_habitacion_seleccionada = None
        self.fila_seleccionada = None
        self.btnEliminar.clicked.connect(self.eliminaHabitacion)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.cmbTipoHabitacion.currentIndexChanged.connect(self.cambiarImagen)
        self.btnRegresar.clicked.connect(self.open_regresar)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GESTION DE HABITACIONES"))
        self.label_2.setText(_translate("MainWindow", "Tipo de habitación"))
        self.cmbTipoHabitacion.setItemText(1, _translate("MainWindow", "Simple"))
        self.cmbTipoHabitacion.setItemText(2, _translate("MainWindow", "Doble"))
        self.cmbTipoHabitacion.setItemText(3, _translate("MainWindow", "Suite"))
        self.cmbTipoHabitacion.setItemText(4, _translate("MainWindow", "Familiar"))
        self.label_3.setText(_translate("MainWindow", "N° de piso"))
        self.label_4.setText(_translate("MainWindow", "Tamaño en m²"))
        self.txtTamanio.setPlaceholderText(_translate("MainWindow", "00.00"))
        self.label_5.setText(_translate("MainWindow", "Descripción"))
        self.label_6.setText(_translate("MainWindow", "N° de camas"))
        self.label_8.setText(_translate("MainWindow", "Tipo de baño"))
        self.cmbTipoBanio.setItemText(1, _translate("MainWindow", "Privado"))
        self.cmbTipoBanio.setItemText(2, _translate("MainWindow", "Jacuzzi"))
        self.txtPrecio.setPlaceholderText(_translate("MainWindow", "  00.00"))
        self.label_9.setText(_translate("MainWindow", "Precio en S/"))
        self.cmbEstado.setItemText(1, _translate("MainWindow", "Disponible"))
        self.cmbEstado.setItemText(2, _translate("MainWindow", "Ocupado"))
        self.cmbEstado.setItemText(3, _translate("MainWindow", "Mantenimiento"))
        self.label_10.setText(_translate("MainWindow", "Estado"))
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
        item = self.tblHabitacion.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tblHabitacion.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo Habitación"))
        item = self.tblHabitacion.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° piso"))
        item = self.tblHabitacion.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tamaño"))
        item = self.tblHabitacion.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblHabitacion.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "N° camas"))
        item = self.tblHabitacion.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tipo Baño"))
        item = self.tblHabitacion.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tblHabitacion.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Estado"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.btnRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscar.text().strip()
            if cadBuscar=="":
                self.llenaTblHabitacion(False,"")
            else:
                self.llenaTblHabitacion(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def llenaTblHabitacion(self,filtro_busqueda,cadBuscar):
        try:
            sql = "SELECT * FROM Habitacion "

            if filtro_busqueda:
                sql += (f" WHERE Tipo LIKE '{cadBuscar}%'"
                f" OR Descripcion LIKE '{cadBuscar}%'"
                f" OR Tipo_baño LIKE '{cadBuscar}%'"
                f" OR Estado LIKE '{cadBuscar}%'")
            list_habitacion = conexion.resultadoSQL(sql)

            # Limpiar la tabla antes de llenarla
            self.tblHabitacion.setRowCount(0)

            # Obten y Configura el número de filas en la tabla
            num_rows = len(list_habitacion)
            self.tblHabitacion.setRowCount(num_rows)

            # Recorre los datos y llénalos en la tabla
            for row_index, row_data in enumerate(list_habitacion):
                for col_index, col_data in enumerate(row_data):
                    # Crea un item en la tabla para cada celda
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Desactivar la edición
                    self.tblHabitacion.setItem(row_index, col_index, item)

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def id_siguiente(self, nombTbl, nombCamp):
        try:
            sql_count = f"SELECT COUNT({nombCamp}) AS total FROM {nombTbl}"
            result_count = conexion.resultadoSQL(sql_count)

            if result_count:
                countReg = result_count[0][0]

                if countReg > 0:
                    sql_max = f"SELECT MAX({nombCamp}) AS idMax FROM {nombTbl}"
                    result_max = conexion.resultadoSQL(sql_max)

                    if result_max:
                        max_id = result_max[0][0]  # Extraer el valor del máximo ID
                        return max_id + 1  # Retornar el siguiente ID
                else:
                    return 1
            else:
                return 1
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))
            return None

    def valida(self):
        print("llega")
        sw = False
        mensajes = ""

        try:
            # Validar cmbTipoHabitacion
            if self.cmbTipoHabitacion.currentText().strip() == "":
                mensajes += "Debe registrar el Tipo de Habitación\n"

            # Validar txtNPiso
            nPiso = self.txtNPiso.text().strip()
            if nPiso == "":
                mensajes += "Debe registrar el Número de Piso\n"
            elif not nPiso.isdigit():
                mensajes += "El Número de Piso solo debe contener números enteros\n"

            # Validar txtTamanio
            tamanio = self.txtTamanio.text().strip()

            if tamanio == "":
                mensajes += "Debe registrar el Tamaño\n"

            else:
                # Validar formato decimal con 2 decimales
                if not re.fullmatch(r'^\d+\.\d{2}$', tamanio):
                    mensajes += "El Tamaño debe estar en formato decimal con 2 decimales (ej: 15.00)\n"

            # Validar txtDescripcion
            if self.txtDescripcion.text().strip() == "":
                mensajes += "Debe registrar la Descripción\n"

            # Validar txtNCamas
            nCamas = self.txtNCamas.text().strip()
            if nCamas == "":
                mensajes += "Debe registrar el Número de Camas\n"
            elif not nCamas.isdigit():
                mensajes += "El Número de Camas solo debe contener números enteros\n"

            # Validar cmbTipoBanio
            if self.cmbTipoBanio.currentText().strip() == "":
                mensajes += "Debe registrar el Tipo de Baño\n"

            # Validar txtPrecio
            precio = self.txtPrecio.text().strip()
            if precio == "":
                mensajes += "Debe registrar un Precio\n"
            else:
                # Validar formato decimal con 2 decimales
                if not re.fullmatch(r'^\d+\.\d{2}$', precio):
                #if not re.fullmatch(r'^\d+(\.\d{2})?$', precio):
                    mensajes += "El Precio debe estar en formato decimal con 2 decimales (ej: 150.00)\n"

            # Validar cmbEstado
            if self.cmbEstado.currentText().strip() == "":
                mensajes += "Debe registrar un Estado\n"

            # Verificar si hubo errores
            if mensajes == "":
                sw = True
            else:
                QMessageBox.warning(self, "Advertencia", mensajes.strip())
                print("1 vez")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")
            print("2 vez")
        return sw

    def registroHabitacion(self):
        if self.btnAgregar.text() == "Agregar":
            if self.valida() :
                try:
                    id_habitacion = self.id_siguiente("Habitacion", "Habitacion_ID")
                    tipo_habitacion = self.cmbTipoHabitacion.currentText().strip()
                    numero_piso = self.txtNPiso.text().strip()
                    tamanio = self.txtTamanio.text().strip()
                    descripcion = self.txtDescripcion.text().strip()
                    numero_camas = self.txtNCamas.text().strip()
                    tipo_banio = self.cmbTipoBanio.currentText().strip()
                    precio = self.txtPrecio.text().strip()
                    estado = self.cmbEstado.currentText().strip()

                    sql = f"""
                    INSERT INTO Habitacion (Habitacion_ID, Tipo, Piso, Tamaño, Descripcion, N_camas, Tipo_baño, Precio, Estado)
                    VALUES ({id_habitacion}, '{tipo_habitacion}', {numero_piso}, {tamanio}, '{descripcion}', {numero_camas}, '{tipo_banio}', {precio}, '{estado}');
                    """
                    conexion.ejecutaSQL(sql)
                    #print(sql)

                    # Guardar la imagen con el nombre basado en el ID de la habitación
                    #self.guardarImagen(id_habitacion)
                    self.llenaTblHabitacion(False, "")
                    QMessageBox.information(self, "Éxito", "Habitación registrada correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(None, "Error", str(e))

        if self.btnAgregar.text() == "Actualizar":
            if self.valida():  # Verifica si los campos son válidos antes de actualizar
                try:
                    # Obtener el ID de la habitación a actualizar desde la variable global
                    id_habitacion = self.id_habitacion_seleccionada

                    # Obtener los valores actuales de los campos
                    tipo_habitacion = self.cmbTipoHabitacion.currentText().strip()
                    numero_piso = self.txtNPiso.text().strip()
                    tamanio = self.txtTamanio.text().strip()
                    descripcion = self.txtDescripcion.text().strip()
                    numero_camas = self.txtNCamas.text().strip()
                    tipo_banio = self.cmbTipoBanio.currentText().strip()
                    precio = self.txtPrecio.text().strip()
                    estado = self.cmbEstado.currentText().strip()

                    # Crear la sentencia SQL para actualizar los datos
                    sql = f"""
                    UPDATE Habitacion
                    SET Tipo = '{tipo_habitacion}',
                        Piso = {numero_piso},
                        Tamaño = {tamanio},
                        Descripcion = '{descripcion}',
                        N_camas = {numero_camas},
                        Tipo_baño = '{tipo_banio}',
                        Precio = {precio},
                        Estado = '{estado}'
                    WHERE Habitacion_ID = {id_habitacion};
                    """
                    # Ejecutar la sentencia SQL
                    conexion.ejecutaSQL(sql)
                    #print(sql)

                    # Actualizar la tabla y limpiar los campos del formulario
                    self.llenaTblHabitacion(False, "")
                    QMessageBox.information(self, "Éxito", "Habitación actualizada correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(None, "Error", str(e))

    def limpia(self):
        self.txtNPiso.clear()
        self.txtTamanio.clear()
        self.txtDescripcion.clear()
        self.txtNCamas.clear()
        self.txtPrecio.clear()

        self.cmbTipoHabitacion.setCurrentIndex(-1)
        self.cmbTipoBanio.setCurrentIndex(-1)
        self.cmbEstado.setCurrentIndex(-1)
        self.tblHabitacion.clearSelection()
        self.btnAgregar.setText("Agregar")

    def selRegistroTabla(self):
        if self.tblHabitacion.selectedItems():
            # Cambiar el texto del botón a "Actualizar"
            self.btnAgregar.setText("Actualizar")

            # Obtener el registro seleccionado
            selected_row = self.tblHabitacion.currentRow()

            # Extraer los valores de la fila seleccionada
            id_habitacion = self.tblHabitacion.item(selected_row, 0).text()
            tipo_habitacion = self.tblHabitacion.item(selected_row, 1).text()
            numero_piso = self.tblHabitacion.item(selected_row, 2).text()
            tamanio = self.tblHabitacion.item(selected_row, 3).text()
            descripcion = self.tblHabitacion.item(selected_row, 4).text()
            numero_camas = self.tblHabitacion.item(selected_row, 5).text()
            tipo_banio = self.tblHabitacion.item(selected_row, 6).text()
            precio = self.tblHabitacion.item(selected_row, 7).text()
            estado = self.tblHabitacion.item(selected_row, 8).text()

            # Llenar los campos del formulario con los datos seleccionados
            self.cmbTipoHabitacion.setCurrentText(tipo_habitacion)
            self.txtNPiso.setText(numero_piso)
            self.txtTamanio.setText(tamanio)
            self.txtDescripcion.setText(descripcion)
            self.txtNCamas.setText(numero_camas)
            self.cmbTipoBanio.setCurrentText(tipo_banio)
            self.txtPrecio.setText(precio)
            self.cmbEstado.setCurrentText(estado)

            self.id_habitacion_seleccionada = id_habitacion
            #print(self.id_habitacion_seleccionada)
            self.fila_seleccionada= selected_row

    def eliminaHabitacion(self):
        if self.tblHabitacion.selectedItems():
            try:
                respuesta = QMessageBox.question(
                    self,
                    "Confirmar eliminación",
                    "¿Estás seguro de que deseas eliminar esta habitación?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No  # Default button
                )
            except Exception as e:
                print(f"Error mostrando el diálogo: {e}")
                return

            if respuesta == QMessageBox.StandardButton.Yes:
                try:
                    # Obtener el ID de la habitación seleccionada desde la variable global
                    id_habitacion = self.id_habitacion_seleccionada

                    # Crear la sentencia SQL para eliminar el registro
                    sql = f"DELETE FROM Habitacion WHERE Habitacion_ID = {id_habitacion};"

                    # Ejecutar la sentencia SQL
                    conexion.ejecutaSQL(sql)
                    #print(sql)

                    # Actualizar la tabla para reflejar los cambios
                    self.llenaTblHabitacion(False, "")
                    QMessageBox.information(self, "Éxito", "Habitación eliminada correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))
            else:
                QMessageBox.information(self, "Cancelado", "La eliminación ha sido cancelada.")
        else:
            QMessageBox.warning(self, "Advertencia", "No se ha seleccionado ninguna habitación para eliminar.")

    def cambiarImagen(self):
        # Obtener el tipo de habitación seleccionado
        tipo_habitacion = self.cmbTipoHabitacion.currentText()

        # Mapear el tipo de habitación a la imagen correspondiente
        imagen_map = {
            "Simple": "sencilla.jpg",
            "Suite": "suite.jpg",
            "Doble": "doble.jpg",
            "Familiar": "familiar.jpg",
            "Matrimonial": "matrimonial.jpg"
        }

        # Obtener el nombre del archivo de la imagen correspondiente
        imagen_archivo = imagen_map.get(tipo_habitacion, "default.jpg")

        # Establecer la imagen en el QLabel
        pixmap = QtGui.QPixmap(imagen_archivo)
        self.txtImagenHabitacion.setPixmap(pixmap)

    def __init__(self,dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()


import sys
class MainWindow(QMainWindow, Ui_GestHabi):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
