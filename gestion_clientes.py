from datetime import datetime, timedelta
import re

from PyQt6.QtCore import QDate, Qt, QRect, QCoreApplication
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QPushButton
from PyQt6 import QtCore, QtGui, QtWidgets
#from reserva_habitaciones import Ui_ReserHabi
import conexion


class Ui_GestClie(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 629)
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
        self.label.setGeometry(QtCore.QRect(290, 20, 451, 21))
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
        self.label_2.setGeometry(QtCore.QRect(30, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtNombres = QtWidgets.QLineEdit(parent=self.widget)
        self.txtNombres.setGeometry(QtCore.QRect(140, 90, 211, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNombres.setFont(font)
        self.txtNombres.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtNombres.setText("")
        self.txtNombres.setObjectName("txtNombres")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(360, 70, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtApellidos = QtWidgets.QLineEdit(parent=self.widget)
        self.txtApellidos.setGeometry(QtCore.QRect(360, 90, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtApellidos.setFont(font)
        self.txtApellidos.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtApellidos.setText("")
        self.txtApellidos.setObjectName("txtApellidos")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtCelular = QtWidgets.QLineEdit(parent=self.widget)
        self.txtCelular.setGeometry(QtCore.QRect(30, 150, 101, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCelular.setFont(font)
        self.txtCelular.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtCelular.setText("")
        self.txtCelular.setObjectName("txtCelular")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(140, 130, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cmbSexo = QtWidgets.QComboBox(parent=self.widget)
        self.cmbSexo.setGeometry(QtCore.QRect(370, 150, 121, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbSexo.setFont(font)
        self.cmbSexo.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbSexo.setObjectName("cmbSexo")
        self.cmbSexo.addItem("")
        self.cmbSexo.setItemText(0, "")
        self.cmbSexo.addItem("")
        self.cmbSexo.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(370, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.btnAgregar = QtWidgets.QPushButton(parent=self.widget)
        self.btnAgregar.setGeometry(QtCore.QRect(290, 220, 101, 31))
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
        self.tblCliente = QtWidgets.QTableWidget(parent=self.widget)
        self.tblCliente.setGeometry(QtCore.QRect(20, 320, 931, 291))
        self.tblCliente.setMaximumSize(QtCore.QSize(96100, 16777215))
        self.tblCliente.setStyleSheet("background-color: rgb(226, 245, 255);\n"
"border-radius:8px;\n"
"")
        self.tblCliente.setObjectName("tblCliente")
        self.tblCliente.setColumnCount(8)
        self.tblCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tblCliente.setHorizontalHeaderItem(7, item)
        self.tblCliente.verticalHeader().setMinimumSectionSize(24)
        self.btnEliminar = QtWidgets.QPushButton(parent=self.widget)
        self.btnEliminar.setGeometry(QtCore.QRect(410, 220, 101, 31))
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
        self.txtBuscar.setGeometry(QtCore.QRect(30, 280, 271, 23))
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
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.widget)
        self.btnLimpiar.setGeometry(QtCore.QRect(530, 220, 101, 31))
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
        self.txtDNI = QtWidgets.QLineEdit(parent=self.widget)
        self.txtDNI.setGeometry(QtCore.QRect(30, 90, 101, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDNI.setFont(font)
        self.txtDNI.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtDNI.setText("")
        self.txtDNI.setObjectName("txtDNI")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(620, 70, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtCorreo = QtWidgets.QLineEdit(parent=self.widget)
        self.txtCorreo.setGeometry(QtCore.QRect(620, 90, 301, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCorreo.setFont(font)
        self.txtCorreo.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtCorreo.setText("")
        self.txtCorreo.setObjectName("txtCorreo")
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.widget)
        self.txtDireccion.setGeometry(QtCore.QRect(140, 150, 221, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtDireccion.setFont(font)
        self.txtDireccion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtDireccion.setText("")
        self.txtDireccion.setObjectName("txtDireccion")
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setGeometry(QtCore.QRect(510, 130, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.dtFechaNacimiento = QtWidgets.QDateEdit(self)
        self.dtFechaNacimiento.setGeometry(QtCore.QRect(510, 150, 151, 22))
        self.dtFechaNacimiento.setObjectName("dtFechaNacimiento")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.btnRegresar = QPushButton(self.widget)
        self.btnRegresar.setObjectName(u"btnRegresar")
        self.btnRegresar.setGeometry(QRect(150, 220, 121, 31))
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
        self.tblCliente.setColumnWidth(0, 60)
        self.tblCliente.setColumnWidth(1, 140)
        self.tblCliente.setColumnWidth(2, 150)
        self.tblCliente.setColumnWidth(3, 70)
        self.tblCliente.setColumnWidth(4, 160)
        self.tblCliente.setColumnWidth(5, 160)
        self.tblCliente.setColumnWidth(6, 70)
        self.tblCliente.setColumnWidth(7, 110)

        self.llenaTblCliente(False,"")
        self.tblCliente.verticalHeader().setVisible(False)
        #self.btnBuscar.clicked.connect(self.busqueda)
        self.filtro_busqueda = False
        self.cadBuscar = ""
        self.txtBuscar.textChanged.connect(self.busqueda)
        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaNacimiento.setDate(fecha_especifica)
        self.dtFechaNacimiento.setCalendarPopup(True)

        self.btnAgregar.clicked.connect(self.registrarCliente)
        self.tblCliente.itemSelectionChanged.connect(self.selRegistroTabla)
        self.dni_seleccionado = None
        self.fila_seleccionada = None
        self.btnEliminar.clicked.connect(self.eliminaCliente)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.btnRegresar.clicked.connect(self.open_regresar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label.setText(_translate("MainWindow", "GESTION DE CLIENTES"))
        self.label_2.setText(_translate("MainWindow", "DNI"))
        self.label_3.setText(_translate("MainWindow", "Nombres"))
        self.label_5.setText(_translate("MainWindow", "Apellidos"))
        self.label_6.setText(_translate("MainWindow", "Celular"))
        self.label_8.setText(_translate("MainWindow", "Dirección"))
        self.cmbSexo.setItemText(1, _translate("MainWindow", "Masculino"))
        self.cmbSexo.setItemText(2, _translate("MainWindow", "Femenino"))
        self.label_10.setText(_translate("MainWindow", "Sexo"))
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
        item = self.tblCliente.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tblCliente.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombres"))
        item = self.tblCliente.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tblCliente.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Celular"))
        item = self.tblCliente.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Correo"))
        item = self.tblCliente.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dirección"))
        item = self.tblCliente.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sexo"))
        item = self.tblCliente.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Fecha nacimiento"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnBuscar.setText(_translate("MainWindow", "Buscar"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))
        self.label_7.setText(_translate("MainWindow", "Correo electrónico"))
        self.label_11.setText(_translate("MainWindow", "Fecha de nacimiento"))


    def llenaTblCliente(self,filtro_busqueda,cadBuscar):
        try:
            sql = "SELECT DNI_Cliente, Nombres, Apellidos, Celular, Correo, Direccion, Sexo,"
            sql+=" CONVERT(DATE, FechaNacimiento) FROM Cliente  "

            if filtro_busqueda:
                sql += (f" WHERE Nombres LIKE '{cadBuscar}%'"
                        f" OR Apellidos LIKE '{cadBuscar}%'"
                        f" OR CONVERT(VARCHAR, DNI_Cliente) LIKE '{cadBuscar}%'")
            list_cliente = conexion.resultadoSQL(sql)
            self.tblCliente.setRowCount(0)

            #número de filas en la tabla
            num_rows = len(list_cliente)
            self.tblCliente.setRowCount(num_rows)

            for row_index, row_data in enumerate(list_cliente):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Desactivar la edición
                    self.tblCliente.setItem(row_index, col_index, item)

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscar.text().strip()
            if cadBuscar=="":
                self.llenaTblCliente(False,"")
            else:
                self.llenaTblCliente(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def valida(self):
        mensajes = ""

        # Validar txtNombres
        nombres = self.txtNombres.text().strip()
        if nombres == "":
            mensajes += "Debe registrar el Nombre\n"

        # Validar txtApellidos
        apellidos = self.txtApellidos.text().strip()
        if apellidos == "":
            mensajes += "Debe registrar el Apellido\n"

        # Validar txtCelular
        celular = self.txtCelular.text().strip()
        if celular == "":
            mensajes += "Debe registrar el Celular\n"
        elif not celular.isdigit():
            mensajes += "El Celular solo debe contener números\n"
        elif len(celular) < 9:
            mensajes += "El Celular debe tener al menos 9 dígitos\n"

        # Validar cmbSexo
        if self.cmbSexo.currentText().strip() == "":
            mensajes += "Debe seleccionar el Sexo\n"

        # Validar txtDNI
        dni = self.txtDNI.text().strip()
        if dni == "":
            mensajes += "Debe registrar el DNI\n"
        elif not dni.isdigit():
            mensajes += "El DNI solo debe contener números\n"
        elif len(dni) != 8:
            mensajes += "El DNI debe tener exactamente 8 dígitos\n"

        # Validar txtCorreo
        correo = self.txtCorreo.text().strip()
        if correo == "":
            mensajes += "Debe registrar el Correo\n"
        elif not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', correo):
            mensajes += "El Correo debe tener un formato válido (ej: ejemplo@dominio.com)\n"

        # Validar txtDireccion
        direccion = self.txtDireccion.text().strip()
        if direccion == "":
            mensajes += "Debe registrar la Dirección\n"

        # Validar txtFechaNacimiento
        fecha_nacimiento = self.dtFechaNacimiento.text().strip()
        if fecha_nacimiento == "":
            mensajes += "Debe registrar la Fecha de Nacimiento\n"
        else:
            try:
                # Intentar parsear la fecha con el formato esperado
                fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

                # Verificar que la fecha no esté en el futuro
                if fecha > datetime.now():
                    mensajes += "La Fecha de Nacimiento no puede ser en el futuro\n"

                # Verificar que la fecha no sea mayor a 100 años desde la actualidad
                fecha_maxima = datetime.now() - timedelta(days=365 * 100)
                if fecha < fecha_maxima:
                    mensajes += "La Fecha de Nacimiento no puede ser mayor a 100 años desde la actualidad\n"

            except ValueError:
                mensajes += "La Fecha de Nacimiento debe tener el formato DD/MM/YYYY\n"

        if mensajes:
            QMessageBox.warning(self, "Validación de Datos", mensajes.strip())
            return False

        return True

    def registrarCliente(self):
        if self.btnAgregar.text() == "Agregar":
            if self.valida():
                try:
                    dni_cliente = self.txtDNI.text().strip()
                    nombres = self.txtNombres.text().strip()
                    apellidos = self.txtApellidos.text().strip()
                    celular = self.txtCelular.text().strip()
                    direccion = self.txtDireccion.text().strip()
                    correo = self.txtCorreo.text().strip()
                    sexo = self.cmbSexo.currentText().strip()
                    fecha_nacimiento = self.dtFechaNacimiento.date().toString("yyyy-MM-dd")
                    fecha_nacimiento+="T00:00:00"
                    sql = f"""
                    INSERT INTO Cliente (DNI_Cliente, Nombres, Apellidos, Celular, Correo, Direccion, Sexo, FechaNacimiento)
                    VALUES ({dni_cliente}, '{nombres}', '{apellidos}', '{celular}', '{correo}', '{direccion}', '{sexo}', '{fecha_nacimiento}');
                    """
                    conexion.ejecutaSQL(sql)
                    # print(sql)

                    self.llenaTblCliente(False, "")
                    QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))

        elif self.btnAgregar.text() == "Actualizar":

            if self.valida():
                try:
                    dni_cliente = self.dni_seleccionado
                    nombres = self.txtNombres.text().strip()
                    apellidos = self.txtApellidos.text().strip()
                    celular = self.txtCelular.text().strip()
                    direccion = self.txtDireccion.text().strip()
                    correo = self.txtCorreo.text().strip()
                    sexo = self.cmbSexo.currentText().strip()
                    fecha_nacimiento = self.dtFechaNacimiento.date().toString("yyyy-MM-dd")
                    fecha_nacimiento += "T00:00:00"
                    sql = f"""
                    UPDATE Cliente
                    SET Nombres = '{nombres}',
                        Apellidos = '{apellidos}',
                        Celular = '{celular}',
                        Correo = '{correo}',
                        Direccion = '{direccion}',
                        Sexo = '{sexo}',
                        FechaNacimiento = '{fecha_nacimiento}'
                    WHERE DNI_Cliente = {dni_cliente};
                    """
                    conexion.ejecutaSQL(sql)
                    # print(sql)

                    self.llenaTblCliente(False, "")
                    QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))

    def selRegistroTabla(self):
        if self.tblCliente.selectedItems():
            self.btnAgregar.setText("Actualizar")

            # Obtener la fila seleccionada
            selected_row = self.tblCliente.currentRow()

            dni = self.tblCliente.item(selected_row, 0).text()
            nombres = self.tblCliente.item(selected_row, 1).text()
            apellidos = self.tblCliente.item(selected_row, 2).text()
            celular = self.tblCliente.item(selected_row, 3).text()
            correo = self.tblCliente.item(selected_row, 4).text()
            direccion = self.tblCliente.item(selected_row, 5).text()
            sexo = self.tblCliente.item(selected_row, 6).text()
            fecha_nacimiento_str = self.tblCliente.item(selected_row, 7).text()

            # Convertir la fecha de nacimiento de string a QDate
            # Ajusta el formato según el formato de la fecha en la tabla
            fecha_nacimiento = QDate.fromString(fecha_nacimiento_str, "yyyy-MM-dd")

            if fecha_nacimiento.isValid():
                self.txtDNI.setText(dni)
                self.txtNombres.setText(nombres)
                self.txtApellidos.setText(apellidos)
                self.txtCelular.setText(celular)
                self.txtDireccion.setText(direccion)
                self.txtCorreo.setText(correo)
                self.cmbSexo.setCurrentText(sexo)
                self.dtFechaNacimiento.setDate(fecha_nacimiento)

                self.dni_seleccionado = dni
                # print(self.dni_seleccionado)
                self.fila_seleccionada = selected_row
            else:
                print("Formato de fecha inválido:", fecha_nacimiento_str)

    def eliminaCliente(self):
        if self.tblCliente.selectedItems():
            try:
                respuesta = QMessageBox.question(
                    self,
                    "Confirmar eliminación",
                    "¿Estás seguro de que deseas eliminar este cliente?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No  # Default button
                )
            except Exception as e:
                print(f"Error mostrando el diálogo: {e}")
                return

            if respuesta == QMessageBox.StandardButton.Yes:
                try:
                    dni_cliente = self.dni_seleccionado
                    sql = f"DELETE FROM Cliente WHERE DNI_Cliente = {dni_cliente};"
                    conexion.ejecutaSQL(sql)
                    # print(sql)
                    self.llenaTblCliente(False, "")
                    QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente.")
                    self.limpia()

                except Exception as e:
                    QMessageBox.warning(self, "Error", str(e))
            else:
                QMessageBox.information(self, "Cancelado", "La eliminación ha sido cancelada.")
        else:
            QMessageBox.warning(self, "Advertencia", "No se ha seleccionado ningún cliente para eliminar.")

    def limpia(self):
        self.txtDNI.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtCelular.clear()
        self.txtDireccion.clear()
        self.txtCorreo.clear()

        self.cmbSexo.setCurrentIndex(-1)
        self.dtFechaNacimiento.setDate(QDate(2000, 1, 1))
        self.tblCliente.clearSelection()

        self.btnAgregar.setText("Agregar")
        self.dni_seleccionado = None

    def __init__(self,dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)
        from reserva_habitaciones import Ui_ReserHabi
        self.ui_reser_habi = Ui_ReserHabi(self.id_user, self)
        self.ui_reser_habi.llenaCmbClientes(False,"")

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()
        self.ui_reser_habi.llenaCmbClientes(False,"")


import sys
class MainWindow(QMainWindow, Ui_GestClie):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
