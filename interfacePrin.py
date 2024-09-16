from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
import conexion
from modificacion_reserva import Ui_Form4
from reserva_habitaciones import Ui_ReserHabi
from gestion_habitacion import  Ui_GestHabi
from factura import Ui_Form2
class Ui_Form(QtWidgets.QWidget):
    def open_reserva(self):
        self.reserva = Ui_Form4(self.id_user,self)
        self.reserva.show()
        self.close()

    def openGestionReserva(self):
        #se pasa el id usuario y la ventana
        self.gesReserva = Ui_ReserHabi(self.id_user,self)
        self.gesReserva.show()
        self.close()

    def openGestionHabi(self):
        #se pasa el id usuario y la ventana
        self.gesHabi = Ui_GestHabi(self.id_user,self)
        self.gesHabi.show()
        self.close()

    def open_factura(self):
        self.reserva = Ui_Form2(self.id_user, self)
        self.reserva.show()
        self.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1482, 784)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 891))
        self.label.setStyleSheet("background-color: rgba(24, 70, 112, 0.7);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 361, 351))
        self.label_4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label_4.setMidLineWidth(-2)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("OIP.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(48)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color:rgb(24, 71, 113);\n"
"background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(-170, -180, 2121, 1101))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("luxury-classic-modern-bedroom-suite-hotel.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("pngwing.com.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 361, 71))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(80, 20, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(370, 650, 1031, 131))
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 520, 321, 191))
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                   "background-image: url(factura.jpg);")
        self.label_9.setPixmap(QPixmap(u"factura.jpg"))
        self.label_9.setScaledContents(True)
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(1130, 520, 351, 261))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(1130, 260, 351, 251))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(1130, 0, 351, 251))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=Form)
        self.label_13.setGeometry(QtCore.QRect(1140, 270, 331, 171))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("type-entertainment-complex-popular-resort-with-pools-water-parks-turkey-with-more-than-5-million-visitors-year-amara-dolce-vita-luxury-hotel-resort-tekirova-kemer.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=Form)
        self.label_14.setGeometry(QtCore.QRect(1140, 530, 331, 181))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("modern-luxury-hotel-office-reception-lounge-with-meeting-room.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=Form)
        self.label_15.setGeometry(QtCore.QRect(1140, 10, 331, 171))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("female-receptionist-elegant-suit-work-hours.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.bnt_gest_hab = QtWidgets.QPushButton(parent=Form)
        self.bnt_gest_hab.setGeometry(QtCore.QRect(1140, 730, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        self.bnt_gest_hab.setFont(font)
        self.bnt_gest_hab.setStyleSheet(u"QPushButton {\n"
                                          "    border-radius: 8px;\n"
                                          "    background-color: rgb(24, 71, 113); /* Fondo original */\n"
                                          "    color: rgb(255, 255, 255); /* Letras en blanco */\n"
                                          "    font-weight: normal; /* Peso normal de la letra */\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(21, 105, 211); /* Fondo celeste */\n"
                                          "    color: rgb(255, 255, 255); /* Letras negras */\n"
                                          "    font-weight: bold; /* Letras m\u00e1s gruesas */\n"
                                          "}\n"
                                          "")
        self.bnt_gest_hab.setObjectName("bnt_gest_hab")
        self.bnt_mod_reserv = QtWidgets.QPushButton(parent=Form)
        self.bnt_mod_reserv.setGeometry(QtCore.QRect(1140, 450, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        self.bnt_mod_reserv.setFont(font)
        self.bnt_mod_reserv.setStyleSheet(u"QPushButton {\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(24, 71, 113); /* Fondo original */\n"
                                       "    color: rgb(255, 255, 255); /* Letras en blanco */\n"
                                       "    font-weight: normal; /* Peso normal de la letra */\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(21, 105, 211); /* Fondo celeste */\n"
                                       "    color: rgb(255, 255, 255); /* Letras negras */\n"
                                       "    font-weight: bold; /* Letras m\u00e1s gruesas */\n"
                                       "}\n"
                                       "")
        self.bnt_mod_reserv.setObjectName("bnt_mod_reserv")
        self.bnt_reserva = QtWidgets.QPushButton(parent=Form)
        self.bnt_reserva.setGeometry(QtCore.QRect(1140, 190, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        self.bnt_reserva.setFont(font)
        self.bnt_reserva.setStyleSheet(u"QPushButton {\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(24, 71, 113); /* Fondo original */\n"
                                       "    color: rgb(255, 255, 255); /* Letras en blanco */\n"
                                       "    font-weight: normal; /* Peso normal de la letra */\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(21, 105, 211); /* Fondo celeste */\n"
                                       "    color: rgb(255, 255, 255); /* Letras negras */\n"
                                       "    font-weight: bold; /* Letras m\u00e1s gruesas */\n"
                                       "}\n"
                                       "")
        self.bnt_reserva.setObjectName("bnt_reserva")
        self.bnt_factura = QtWidgets.QPushButton(parent=Form)
        self.bnt_factura.setGeometry(QtCore.QRect(20, 720, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        self.bnt_factura.setFont(font)
        self.bnt_factura.setStyleSheet(u"QPushButton {\n"
                                       "    border-radius: 8px;\n"
                                       "    background-color: rgb(24, 71, 113); /* Fondo original */\n"
                                       "    color: rgb(255, 255, 255); /* Letras en blanco */\n"
                                       "    font-weight: normal; /* Peso normal de la letra */\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(21, 105, 211); /* Fondo celeste */\n"
                                       "    color: rgb(255, 255, 255); /* Letras negras */\n"
                                       "    font-weight: bold; /* Letras m\u00e1s gruesas */\n"
                                       "}\n"
                                       "")
        self.bnt_factura.setObjectName("bnt_factura")
        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 510, 341, 271))
        self.label_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_9.raise_()
        self.bnt_gest_hab.raise_()
        self.bnt_mod_reserv.raise_()
        self.bnt_reserva.raise_()
        self.bnt_factura.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #modificacion
        self.bnt_mod_reserv.clicked.connect(self.open_reserva)
        self.bnt_reserva.clicked.connect(self.openGestionReserva)
        self.bnt_gest_hab.clicked.connect(self.openGestionHabi)
        self.bnt_factura.clicked.connect(self.open_factura)

    def retranslateUi(self, Form):
        sql = f"SELECT * FROM Empleado WHERE DNI_Empleado = {self.id_user}"
        user = conexion.resultadoSQL(sql)
        ingreso = user[0][1] + " " + user[0][2]
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "MARK\'S"))
        self.label_7.setText(_translate("Form", ingreso))
        self.bnt_gest_hab.setText(_translate("Form", "GESTIÓN DE HABITACIONES"))
        self.bnt_mod_reserv.setText(_translate("Form", "MODIFICAR / CANCELAR"))
        self.bnt_reserva.setText(_translate("Form", "RESERVA"))
        self.bnt_factura.setText(_translate("Form", "FACTURAS"))
        self.label_16.setText("")

    def transfer_data(self, data):
        self.label.setText(data)




    def __init__(self, dato):
        super().__init__()
        self.id_user = dato
        self.setupUi(self)

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec())