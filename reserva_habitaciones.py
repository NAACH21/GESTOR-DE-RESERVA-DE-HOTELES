import subprocess

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate, QDateTime, Qt, QCoreApplication, QRect
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from pyexpat.errors import messages
import conexion
from gestion_clientes import Ui_GestClie

class Ui_ReserHabi(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 734)
        MainWindow.setGeometry(
            (MainWindow.screen().geometry().width() - MainWindow.geometry().width()) // 2,
            (MainWindow.screen().geometry().height() - MainWindow.geometry().height()) // 2,
            MainWindow.geometry().width(),
            MainWindow.geometry().height()
        )
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1131, 771))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1131, 20))
        self.line.setStyleSheet("color: rgb(14, 138, 229);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(170, 20, 451, 21))
        font = QtGui.QFont()
        font.setFamily("News701 BT")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(12, 96, 204);")
        self.label.setObjectName("label")
        self.txtLogo = QtWidgets.QLabel(parent=self.widget)
        self.txtLogo.setGeometry(QtCore.QRect(60, 10, 71, 61))
        self.txtLogo.setText("")
        self.txtLogo.setPixmap(QtGui.QPixmap("logo.png"))
        self.txtLogo.setScaledContents(True)
        self.txtLogo.setObjectName("txtLogo")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmbClientes = QtWidgets.QComboBox(parent=self.widget)
        self.cmbClientes.setGeometry(QtCore.QRect(30, 110, 431, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbClientes.setFont(font)
        self.cmbClientes.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbClientes.setObjectName("cmbClientes")
        self.cmbClientes.addItem("")
        self.cmbClientes.setItemText(0, "")
        self.txtBuscarCliente = QtWidgets.QLineEdit(parent=self.widget)
        self.txtBuscarCliente.setGeometry(QtCore.QRect(200, 80, 261, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtBuscarCliente.setFont(font)
        self.txtBuscarCliente.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:8px;")
        self.txtBuscarCliente.setText("")
        self.txtBuscarCliente.setObjectName("txtBuscarCliente")
        self.txtNDiasHospedar = QtWidgets.QLineEdit(parent=self.widget)
        self.txtNDiasHospedar.setGeometry(QtCore.QRect(170, 490, 31, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNDiasHospedar.setFont(font)
        self.txtNDiasHospedar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtNDiasHospedar.setText("")
        self.txtNDiasHospedar.setObjectName("txtNDiasHospedar")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 150, 711, 201))
        self.widget_2.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 8px;")
        self.widget_2.setObjectName("widget_2")
        self.tblHabitacion = QtWidgets.QTableWidget(parent=self.widget_2)
        self.tblHabitacion.setGeometry(QtCore.QRect(10, 40, 471, 151))
        self.tblHabitacion.setMaximumSize(QtCore.QSize(96100, 16777215))
        self.tblHabitacion.setStyleSheet("background-color: rgb(226, 245, 255);\n"
"border-radius:8px;\n"
"")
        self.tblHabitacion.setObjectName("tblHabitacion")
        self.tblHabitacion.setColumnCount(8)
        self.tblHabitacion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        item.setFont(font)
        self.tblHabitacion.setHorizontalHeaderItem(7, item)
        self.tblHabitacion.verticalHeader().setMinimumSectionSize(24)
        self.txtImagenHabitacion = QtWidgets.QLabel(parent=self.widget_2)
        self.txtImagenHabitacion.setGeometry(QtCore.QRect(500, 50, 201, 141))
        self.txtImagenHabitacion.setText("")
        self.txtImagenHabitacion.setPixmap(QtGui.QPixmap(":/habitacion1.jpg"))
        self.txtImagenHabitacion.setScaledContents(True)
        self.txtImagenHabitacion.setObjectName("txtImagenHabitacion")
        self.txtBuscarHabitacion = QtWidgets.QLineEdit(parent=self.widget_2)
        self.txtBuscarHabitacion.setGeometry(QtCore.QRect(220, 10, 251, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtBuscarHabitacion.setFont(font)
        self.txtBuscarHabitacion.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:8px;")
        self.txtBuscarHabitacion.setObjectName("txtBuscarHabitacion")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtIdHabitacionSele = QtWidgets.QLineEdit(parent=self.widget_2)
        self.txtIdHabitacionSele.setEnabled(True)
        self.txtIdHabitacionSele.setGeometry(QtCore.QRect(610, 10, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIdHabitacionSele.setFont(font)
        self.txtIdHabitacionSele.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtIdHabitacionSele.setObjectName("txtIdHabitacionSele")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(500, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_22.setGeometry(QtCore.QRect(500, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(30, 490, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setGeometry(QtCore.QRect(30, 520, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.dtFechaEntrada = QtWidgets.QDateTimeEdit(self)
        self.dtFechaEntrada.setGeometry(QtCore.QRect(180, 520, 141, 22))
        self.dtFechaEntrada.setObjectName("dtFechaEntrada")
        self.label_13 = QtWidgets.QLabel(parent=self.widget)
        self.label_13.setGeometry(QtCore.QRect(30, 560, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.txtMontoTotal = QtWidgets.QLineEdit(parent=self.widget)
        self.txtMontoTotal.setEnabled(False)
        self.txtMontoTotal.setGeometry(QtCore.QRect(200, 560, 91, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtMontoTotal.setFont(font)
        self.txtMontoTotal.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtMontoTotal.setText("")
        self.txtMontoTotal.setObjectName("txtMontoTotal")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 70, 711, 71))
        self.widget_3.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 8px;")
        self.widget_3.setObjectName("widget_3")
        self.btnNuevoCliente = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnNuevoCliente.setGeometry(QtCore.QRect(490, 30, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnNuevoCliente.setFont(font)
        self.btnNuevoCliente.setStyleSheet(u"\n"
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
        self.btnNuevoCliente.setObjectName("btnNuevoCliente")
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.widget)
        self.btnLimpiar.setGeometry(QtCore.QRect(240, 690, 121, 31))
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
        self.btnRegistrar = QtWidgets.QPushButton(parent=self.widget)
        self.btnRegistrar.setGeometry(QtCore.QRect(380, 690, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet(u"\n"
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
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setGeometry(QtCore.QRect(20, 360, 711, 111))
        self.widget_5.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 8px;")
        self.widget_5.setObjectName("widget_5")
        self.label_16 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.cmbServiciosExtra = QtWidgets.QComboBox(parent=self.widget_5)
        self.cmbServiciosExtra.setGeometry(QtCore.QRect(10, 40, 431, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbServiciosExtra.setFont(font)
        self.cmbServiciosExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.cmbServiciosExtra.setPlaceholderText("")
        self.cmbServiciosExtra.setObjectName("cmbServiciosExtra")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.setItemText(0, "")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.cmbServiciosExtra.addItem("")
        self.txtCantidadServicioExtra = QtWidgets.QLineEdit(parent=self.widget_5)
        self.txtCantidadServicioExtra.setEnabled(True)
        self.txtCantidadServicioExtra.setGeometry(QtCore.QRect(200, 80, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtCantidadServicioExtra.setFont(font)
        self.txtCantidadServicioExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtCantidadServicioExtra.setObjectName("txtCantidadServicioExtra")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(460, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.txtPrecioServicioExtra = QtWidgets.QLineEdit(parent=self.widget_5)
        self.txtPrecioServicioExtra.setEnabled(False)
        self.txtPrecioServicioExtra.setGeometry(QtCore.QRect(550, 40, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPrecioServicioExtra.setFont(font)
        self.txtPrecioServicioExtra.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtPrecioServicioExtra.setPlaceholderText("")
        self.txtPrecioServicioExtra.setObjectName("txtPrecioServicioExtra")
        self.dtFechaSalida = QtWidgets.QDateTimeEdit(self)
        self.dtFechaSalida.setGeometry(QtCore.QRect(510, 520, 141, 22))
        self.dtFechaSalida.setObjectName("dtFechaSalida")
        self.label_12 = QtWidgets.QLabel(parent=self.widget)
        self.label_12.setGeometry(QtCore.QRect(360, 520, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setGeometry(QtCore.QRect(20, 480, 711, 201))
        self.widget_4.setStyleSheet("border: 1px solid rgb(239, 239, 239);\n"
"border-radius: 8px;")
        self.widget_4.setObjectName("widget_4")
        self.rbtTarjeta = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtTarjeta.setGeometry(QtCore.QRect(420, 110, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtTarjeta.setFont(font)
        self.rbtTarjeta.setObjectName("rbtTarjeta")
        self.rbtYape = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtYape.setGeometry(QtCore.QRect(290, 110, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtYape.setFont(font)
        self.rbtYape.setObjectName("rbtYape")
        self.rbtEfectivo = QtWidgets.QRadioButton(parent=self.widget_4)
        self.rbtEfectivo.setGeometry(QtCore.QRect(170, 110, 89, 20))
        self.rbtEfectivo.setObjectName("rbtEfectivo")
        self.label_15 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.txtObservacionFactura = QtWidgets.QLineEdit(parent=self.widget_4)
        self.txtObservacionFactura.setEnabled(True)
        self.txtObservacionFactura.setGeometry(QtCore.QRect(10, 170, 431, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtObservacionFactura.setFont(font)
        self.txtObservacionFactura.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"border-radius:4px;")
        self.txtObservacionFactura.setObjectName("txtObservacionFactura")
        self.label_18 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.widget_4.raise_()
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.line.raise_()
        self.label.raise_()
        self.txtLogo.raise_()
        self.label_2.raise_()
        self.cmbClientes.raise_()
        self.txtBuscarCliente.raise_()
        self.txtNDiasHospedar.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.dtFechaEntrada.raise_()
        self.label_13.raise_()
        self.txtMontoTotal.raise_()
        self.btnLimpiar.raise_()
        self.btnRegistrar.raise_()
        self.widget_5.raise_()
        self.dtFechaSalida.raise_()
        self.label_12.raise_()
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.btnRegresar = QPushButton(self.widget)
        self.btnRegresar.setObjectName(u"btnRegresar")
        self.btnRegresar.setGeometry(QRect(110, 690, 121, 31))
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
        self.btnRegresar.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Ancho de columnas de tablas
        self.tblHabitacion.setColumnWidth(0, 35) # ID
        self.tblHabitacion.setColumnWidth(1, 80) #Tipo
        self.tblHabitacion.setColumnWidth(2, 38) #Piso
        self.tblHabitacion.setColumnWidth(3, 40) # tamaño
        self.tblHabitacion.setColumnWidth(4, 100)# descripcion
        self.tblHabitacion.setColumnWidth(5, 40) # camas
        self.tblHabitacion.setColumnWidth(6, 60) # baño
        self.tblHabitacion.setColumnWidth(7, 50)  # bprecio

        self.tblHabitacion.verticalHeader().setVisible(False)
        self.llenaTblHabitacion(False,"")
        self.tblHabitacion.selectionModel().selectionChanged.connect(self.selRegistroTabla)
        self.txtBuscarHabitacion.textChanged.connect(self.busquedaHabi)

        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaEntrada.setDate(fecha_especifica)
        self.dtFechaEntrada.setCalendarPopup(True)
        fecha_especifica = QDate(2000, 1, 1)
        self.dtFechaSalida.setDate(fecha_especifica)
        self.dtFechaSalida.setCalendarPopup(True)
        self.btnNuevoCliente.clicked.connect(self.openGestionClientes)
        self.filtro_busqueda = None
        self.cadBuscar = ""
        self.llenaCmbClientes(False, "")
        self.txtBuscarCliente.textChanged.connect(self.busqueda)

        self.cmbServiciosExtra.currentIndexChanged.connect(self.actualizaPrecioServicioExtra)
        self.txtCantidadServicioExtra.setEnabled(False)
        fecha_hora_actual = QDateTime.currentDateTime()
        self.dtFechaEntrada.setDateTime(fecha_hora_actual)
        self.dtFechaSalida.setDateTime(fecha_hora_actual.addDays(1))
        self.dtFechaSalida.dateTimeChanged.connect(self.actualizaNDiasHospedar)
        self.dtFechaEntrada.dateTimeChanged.connect(self.actualizaNDiasHospedar)
        self.txtNDiasHospedar.textChanged.connect(self.calculaFechaSalida)
        fecha_actual = QDateTime.currentDateTime()
        self.dtFechaEntrada.setMinimumDateTime(fecha_actual)
        self.dtFechaSalida.setMinimumDateTime(fecha_actual)

        self.tblHabitacion.selectionModel().selectionChanged.connect(self.calculaMontoTotal)
        self.txtPrecioServicioExtra.textChanged.connect(self.calculaMontoTotal)
        self.txtCantidadServicioExtra.textChanged.connect(self.calculaMontoTotal)
        self.btnLimpiar.clicked.connect(self.limpia)
        self.dni_clienteSele = None
        self.dni_empleadoSele= self.id_user
        print(self.dni_empleadoSele)
        self.btnRegistrar.clicked.connect(self.valida)
        self.cmbServiciosExtra.currentIndexChanged.connect(self.actualizaCantServicio)
        self.txtCantidadServicioExtra.textChanged.connect(self.actualizaCantServicio2)
        self.btnRegistrar.clicked.connect(self.registraReserva)
        self.cmbClientes.currentIndexChanged.connect(self.obtenerDNICliente)
        self.btnRegresar.clicked.connect(self.open_regresar)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RESERVA DE HABITACIONES"))
        self.label_2.setText(_translate("MainWindow", "Nombre del cliente"))
        self.cmbClientes.setPlaceholderText(_translate("MainWindow", " Seleccione un cliente"))
        self.txtBuscarCliente.setPlaceholderText(_translate("MainWindow", " Buscar cliente"))
        item = self.tblHabitacion.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tblHabitacion.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tblHabitacion.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "N° piso"))
        item = self.tblHabitacion.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tamaño"))
        item = self.tblHabitacion.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblHabitacion.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Camas"))
        item = self.tblHabitacion.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Tipo Baño"))
        item = self.tblHabitacion.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Precio"))
        self.txtBuscarHabitacion.setPlaceholderText(_translate("MainWindow", "Buscar habitación por campos"))
        self.label_5.setText(_translate("MainWindow", "Seleccione una habitación"))
        self.label_21.setText(_translate("MainWindow", "ID habitación"))
        self.label_22.setText(_translate("MainWindow", "seleccionada"))
        self.label_10.setText(_translate("MainWindow", "N° de dias a hospedar"))
        self.label_11.setText(_translate("MainWindow", "Fecha/hora de entrada"))
        self.label_13.setText(_translate("MainWindow", "Monto total a pagar en S/"))
        self.btnNuevoCliente.setText(_translate("MainWindow", "Nuevo cliente"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar datos"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.label_16.setText(_translate("MainWindow", "Servicios extra"))
        self.cmbServiciosExtra.setItemText(1, _translate("MainWindow", "Bebidas (Cóctel, vino, cerveza)"))
        self.cmbServiciosExtra.setItemText(2, _translate("MainWindow", "Comida Gourmet (Cena gourmet, plato especial)"))
        self.cmbServiciosExtra.setItemText(3, _translate("MainWindow", "Decoración Especial para Eventos (Floral,temática)"))
        self.cmbServiciosExtra.setItemText(4, _translate("MainWindow", "Masaje Relajante (Piedras calientes, aromaterapia)"))
        self.cmbServiciosExtra.setItemText(5, _translate("MainWindow", "Cuidado de Mascotas (Cuidado completo)"))
        self.label_14.setText(_translate("MainWindow", "Cantidad de veces de servicio"))
        self.label_17.setText(_translate("MainWindow", "Precio en S/"))
        self.label_12.setText(_translate("MainWindow", "Fecha/hora de salida"))
        self.rbtTarjeta.setText(_translate("MainWindow", "Trans. Bancaria"))
        self.rbtYape.setText(_translate("MainWindow", "Yape/Plin"))
        self.rbtEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.label_15.setText(_translate("MainWindow", "Métodos de pago"))
        self.label_18.setText(_translate("MainWindow", "Observación"))
        self.btnRegresar.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))

    def llenaTblHabitacion(self, filtro_busqueda, cadBuscar):
        try:
            sql = "SELECT * FROM Habitacion WHERE Estado = 'Disponible'"
            if filtro_busqueda:
                sql += (f" AND (Tipo LIKE '{cadBuscar}%'"
                        f" OR Descripcion LIKE '{cadBuscar}%'"
                        f" OR Tipo_baño LIKE '{cadBuscar}%' "
                        f" OR CAST(Piso AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(Tamaño AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(N_camas AS NVARCHAR) LIKE '{cadBuscar}%'"
                        f" OR CAST(Precio AS NVARCHAR) LIKE '{cadBuscar}%')")

            list_habitacion = conexion.resultadoSQL(sql)
            self.tblHabitacion.setRowCount(0)

            num_rows = len(list_habitacion)
            self.tblHabitacion.setRowCount(num_rows)
            font = QFont()
            font.setPointSize(8)
            for row_index, row_data in enumerate(list_habitacion):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Desactivar la edición
                    item.setFont(font)
                    self.tblHabitacion.setItem(row_index, col_index, item)

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def busquedaHabi(self):
        try:
            cadBuscar = self.txtBuscarHabitacion.text().strip()
            if cadBuscar=="":
                self.llenaTblHabitacion(False,"")
            else:
                self.llenaTblHabitacion(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def ventanaNuevoCliente(self):
        subprocess.Popen(['python', 'gestion_clientes.py'])
        self.llenaCmbClientes(False,"")

    def llenaCmbClientes(self, filtro_busqueda, cadBuscar):
        sql = ("SELECT DNI_Cliente, CONCAT(Nombres, ' ', Apellidos) AS nombre_completo "
               "FROM Cliente ")
        if filtro_busqueda:
            sql += (f" WHERE Nombres LIKE '{cadBuscar}%'"
                    f" OR Apellidos LIKE '{cadBuscar}%'")

        try:
            list_cliente = conexion.resultadoSQL(sql)
            self.cmbClientes.clear()
            self.cmbClientes.addItem("")

            if len(list_cliente) == 1:
                dni_cliente = list_cliente[0][0]
                nombre_completo = list_cliente[0][1]
                # Añadir el nombre y asociar el DNI como dato extra
                self.cmbClientes.addItem(nombre_completo, dni_cliente)
                self.cmbClientes.setCurrentText(nombre_completo)
            else:
                for cliente in list_cliente:
                    dni_cliente = cliente[0]
                    nombre_completo = cliente[1]
                    self.cmbClientes.addItem(nombre_completo, dni_cliente)
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    def obtenerDNICliente(self):
        try:
            indice_seleccionado = self.cmbClientes.currentIndex()

            if indice_seleccionado > 0:
                dni_cliente = self.cmbClientes.itemData(indice_seleccionado)
                if dni_cliente:
                    print(f"DNI del cliente seleccionado: {dni_cliente}")
                    self.dni_clienteSele = dni_cliente
                else:
                    pass
                    #print("No hay DNI asociado al cliente seleccionado.")
            else:
                pass
                #print("No se ha seleccionado un cliente válido.")
        except Exception as e:
            print(f"Error al obtener el DNI del cliente: {e}")

    def selRegistroTabla(self):
        if self.tblHabitacion.selectedItems():
            selected_row = self.tblHabitacion.currentRow()
            id_habitacion = self.tblHabitacion.item(selected_row, 0).text()
            tipo_habitacion = self.tblHabitacion.item(selected_row, 1).text()
            self.txtIdHabitacionSele.setText(id_habitacion)
            imagen_map = {
                    "Simple": "sencilla.jpg",
                    "Suite": "suite.jpg",
                    "Doble": "doble.jpg",
                    "Familiar": "familiar.jpg",
                    "Matrimonial": "matrimonial.jpg"
            }

            imagen_archivo = imagen_map.get(tipo_habitacion, "default.jpg")
            pixmap = QtGui.QPixmap(imagen_archivo)
            self.txtImagenHabitacion.setPixmap(pixmap)

    def busqueda(self):
        try:
            cadBuscar = self.txtBuscarCliente.text().strip()
            if cadBuscar=="":
                self.llenaCmbClientes(False,"")
            else:
                self.llenaCmbClientes(True, cadBuscar)
        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))

    def actualizaPrecioServicioExtra(self):
        precios_servicios = {
            "Bebidas (Cóctel, vino, cerveza)": 25.00,
            "Comida Gourmet (Cena gourmet, plato especial)": 30.00,
            "Decoración Especial para Eventos (Floral,temática)": 40.00,
            "Masaje Relajante (Piedras calientes, aromaterapia)": 35.00,
            "Cuidado de Mascotas (Cuidado completo)": 30.00
        }
        servicio_seleccionado = self.cmbServiciosExtra.currentText()

        if servicio_seleccionado in precios_servicios:
            precio = precios_servicios[servicio_seleccionado]
            self.txtPrecioServicioExtra.setText(f"{precio:.2f}")
            self.txtCantidadServicioExtra.setEnabled(True)
        else:
            self.txtPrecioServicioExtra.clear()
            self.txtCantidadServicioExtra.setEnabled(False)

    def calculaFechaSalida(self):
        try:
            texto_dias = self.txtNDiasHospedar.text().strip()
            if texto_dias:
                n_dias = int(texto_dias)
                if n_dias < 1:
                    self.txtNDiasHospedar.setText("1")
                    self.mostrarMensajeError("El número de días debe ser al menos 1.")
                    return
            else:
                n_dias = 1
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = fecha_entrada.addDays(n_dias)
            self.dtFechaSalida.setDateTime(fecha_salida)

        except ValueError:
            self.mostrarMensajeError("El número de días debe ser un valor entero.")

    def actualizaNDiasHospedar(self):
        try:
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = self.dtFechaSalida.dateTime()
            if fecha_salida < fecha_entrada:
                if self.txtNDiasHospedar.text():
                    self.mostrarMensajeError("La fecha de salida debe ser posterior a la fecha de entrada.")
                self.dtFechaSalida.setDateTime(fecha_entrada.addDays(1))
                return
            diferencia_dias = fecha_entrada.daysTo(fecha_salida)
            if diferencia_dias >= 1:
                self.txtNDiasHospedar.setText(str(diferencia_dias))
            self.calculaMontoTotal()

        except ValueError as e:
            self.mostrarMensajeError(f"Error: {e}")

    def calculaMontoTotal(self):
        try:
            # Verifica si hay una fila seleccionada
            selected_row = self.tblHabitacion.currentRow()
            if selected_row == -1:
                # No hay fila seleccionada, así que simplemente vacía el campo de monto total
                self.txtMontoTotal.clear()
                return

            # Obtiene el precio de la habitación y verifica si es numérico
            precio_item = self.tblHabitacion.item(selected_row, 7)
            if precio_item is None or not precio_item.text().replace('.', '', 1).isdigit():
                # El precio no es válido, así que vacía el campo de monto total
                self.txtMontoTotal.clear()
                return

            precio_habitacion = float(precio_item.text())

            # Obtiene la cantidad de servicios extra y el precio del servicio extra
            cantidad_servicio_extra = int(self.txtCantidadServicioExtra.text() or 1)
            precio_servicio_extra = float(self.txtPrecioServicioExtra.text() or 0)

            # Calcula el monto de la habitación
            fecha_entrada = self.dtFechaEntrada.dateTime()
            fecha_salida = self.dtFechaSalida.dateTime()
            diferencia_dias = fecha_entrada.daysTo(fecha_salida)
            if diferencia_dias < 1:
                diferencia_dias = 1
            monto_habitacion = precio_habitacion * diferencia_dias

            # Calcula el monto de los servicios extra
            monto_servicios_extra = precio_servicio_extra * cantidad_servicio_extra

            # Calcula el monto total
            monto_total = monto_habitacion + monto_servicios_extra

            # Muestra el monto total en el campo correspondiente
            self.txtMontoTotal.setText(f"{monto_total:.2f}")

        except ValueError as e:
            # Si ocurre una excepción, vacía el campo de monto total
            self.txtMontoTotal.clear()

    def mostrarMensajeError(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje, QMessageBox.StandardButton.Ok)

    def limpia(self):
        self.txtNDiasHospedar.clear()
        self.txtCantidadServicioExtra.clear()
        self.txtPrecioServicioExtra.clear()
        self.txtMontoTotal.clear()
        self.txtObservacionFactura.clear()
        self.txtMontoTotal.clear()
        self.txtIdHabitacionSele.clear()
        self.dtFechaEntrada.setDateTime(QDateTime.currentDateTime())  # Fecha y hora actual
        self.dtFechaSalida.setDateTime(QDateTime.currentDateTime().addDays(1))  # Fecha y hora actual

        self.cmbClientes.setCurrentIndex(0)
        self.cmbServiciosExtra.setCurrentIndex(0)

        self.rbtEfectivo.setAutoExclusive(False)
        self.rbtEfectivo.setChecked(False)

        self.rbtYape.setAutoExclusive(False)
        self.rbtYape.setChecked(False)

        self.rbtTarjeta.setAutoExclusive(False)
        self.rbtTarjeta.setChecked(False)

        # Volver a activar la exclusividad para el comportamiento normal
        self.rbtEfectivo.setAutoExclusive(True)
        self.rbtYape.setAutoExclusive(True)
        self.rbtTarjeta.setAutoExclusive(True)
        self.tblHabitacion.clearSelection()
        self.txtImagenHabitacion.clear()
        self.txtMontoTotal.setText("")

    def valida(self):
        mensajes = ""
        if self.cmbClientes.currentText().strip() == "":
            mensajes +="Debe seleccionar un cliente\n"
        if self.txtIdHabitacionSele.text().strip() == "":
            mensajes += "Debe seleccionar unn habitación\n"
        if not (self.rbtEfectivo.isChecked() or self.rbtYape.isChecked() or self.rbtTarjeta.isChecked()):
            mensajes +="Debe seleccionar un método de pago\n"
        if not self.txtObservacionFactura.text().strip():
            mensajes +="Debe ingresar una observación en la factura\n"
        if mensajes =="":
            return True
        else:
            self.mostrarMensajeError(mensajes)

    def actualizaCantServicio(self):
        if not self.cmbServiciosExtra.currentText().strip() == "" and len(self.txtCantidadServicioExtra.text().strip())<1:
            textCan = self.txtCantidadServicioExtra.text().strip()
            if textCan:
                cant = int(textCan)
                if cant < 1:
                    self.txtCantidadServicioExtra.setText("1")
        else:
            self.txtCantidadServicioExtra.setText("")

    def actualizaCantServicio2(self):
        if self.txtCantidadServicioExtra.text().strip() =="0":
            self.txtCantidadServicioExtra.setText("1")

    def registraReserva(self):
        if self.valida():
            id_reserva = self.id_siguiente("Reserva", "Reserva_ID")
            if id_reserva is None:
                self.mostrarMensajeError("No se pudo obtener el ID de la reserva.")
                return
            dni_empleado = self.dni_empleadoSele
            dni_cliente = self.dni_clienteSele
            id_habitacion = self.txtIdHabitacionSele.text().strip()
            fecha_entrada = self.dtFechaEntrada.dateTime().toPyDateTime().strftime('%Y-%m-%dT%H:%M:%S')
            fecha_salida = self.dtFechaSalida.dateTime().toPyDateTime().strftime('%Y-%m-%dT%H:%M:%S')
            estado_reserva = "Confirmado"
            sql_reserva = f"""
            INSERT INTO Reserva (Reserva_ID, DNI_Empleado, DNI_Cliente, Habitacion_ID, Fech_Entrada, Fech_Salida, Estado)
            VALUES ({id_reserva}, {dni_empleado}, {dni_cliente}, {id_habitacion}, '{fecha_entrada}', '{fecha_salida}', '{estado_reserva}')
            """
            try:
                #print(sql_reserva)
                conexion.ejecutaSQL(sql_reserva)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar la reserva: {e}")
                return
            # Registrar servicios extra si se han seleccionado
            servicio_extra = self.cmbServiciosExtra.currentText().strip()
            if servicio_extra:
                id_servicioExtra = self.id_siguiente("ServiciosExtra", "ServiciosExtra_ID")
                precio_servicio_extra = float(self.txtPrecioServicioExtra.text().strip())
                estado_servicio_extra = "Registrado"  # Puedes ajustar esto según tus necesidades

                sql_servicios_extra = f"""
                INSERT INTO ServiciosExtra (Reserva_ID, Descripcion, Precio, Estado)
                VALUES ({id_reserva}, '{servicio_extra}', {precio_servicio_extra}, '{estado_servicio_extra}')
                """
                try:
                    #print(sql_servicios_extra)
                    conexion.ejecutaSQL(sql_servicios_extra)
                except Exception as e:
                    self.mostrarMensajeError(f"Error al registrar los servicios extra: {e}")
            # Registrar la factura
            id_factura = self.id_siguiente("Factura", "Factura_ID")
            monto_total = float(self.txtMontoTotal.text().strip())
            metodo_pago = "Efectivo" if self.rbtEfectivo.isChecked() else \
                "Yape" if self.rbtYape.isChecked() else \
                    "Tarjeta"
            observacion = self.txtObservacionFactura.text().strip()

            sql_factura = f"""
            INSERT INTO Factura (Factura_ID, Monto, Reserva_ID, Fecha, Metodo_Pago, Observacion)
            VALUES ({id_factura}, {monto_total}, {id_reserva}, '{fecha_entrada}', '{metodo_pago}', '{observacion}')
            """
            try:
                #print(sql_factura)
                conexion.ejecutaSQL(sql_factura)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar la factura: {e}")
            # Registrar en el historial de cambios de reserva
            id_cambio = self.id_siguiente("HistorialCambiosReserva", "Cambio_ID")
            descripcion_cambio = "Reserva creada"
            sql_historial = f"""
            INSERT INTO HistorialCambiosReserva (Cambio_ID, Reserva_ID, FechaCambio, Descripcion)
            VALUES ({id_cambio}, {id_reserva}, '{fecha_entrada}', '{descripcion_cambio}')
            """
            try:
                #print(sql_historial)
                conexion.ejecutaSQL(sql_historial)
            except Exception as e:
                self.mostrarMensajeError(f"Error al registrar el historial de cambios: {e}")
            self.limpia()
            self.mostrarMensajeError("Reserva registrada exitosamente.")

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

    def __init__(self, dato,ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)

    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def openGestionClientes(self):
        #se pasa el id usuario y la ventana
        self.gesClie = Ui_GestClie(self.id_user, self)
        self.gesClie.show()
        self.close()

import sys
class MainWindow(QMainWindow, Ui_ReserHabi):
        def __init__(self):
                super().__init__()
                self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())