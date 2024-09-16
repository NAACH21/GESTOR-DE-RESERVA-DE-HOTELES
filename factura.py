import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
import conexion
from fpdf import FPDF
from datetime import date
import os
import uuid


class Ui_Form2(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1482, 891)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(660, 0, 211, 191))
        self.label_4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label_4.setMidLineWidth(-2)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../MIN_PROY1/OIP.jpeg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(24)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color:rgb(24, 71, 113);\n"
        "background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1491, 891))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("luxury-classic-modern-bedroom-suite-hotel.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(0, 190, 1481, 81))
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet("background-color: rgba(24, 71, 113,0.9);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(650, 200, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(36)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_15 = QtWidgets.QLabel(parent=Form)
        self.label_15.setGeometry(QtCore.QRect(0, 190, 1491, 81))
        self.label_15.setStyleSheet("background-color: rgba(24, 71, 113,0.9);\n"
        "border-radius: 20px;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.bntt_regresar = QtWidgets.QPushButton(parent=Form)
        self.bntt_regresar.setGeometry(QtCore.QRect(30, 10, 141, 51))
        self.bntt_regresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_regresar.setStyleSheet("QPushButton {\n"
        "    border-radius: 20px;\n"
        "    background-color: rgb(24, 71, 113);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    color: rgb(24, 71, 113);\n"
        "}")
        self.bntt_regresar.setObjectName("bntt_regresar")
        self.bntt_buscar = QtWidgets.QPushButton(parent=Form)
        self.bntt_buscar.setGeometry(QtCore.QRect(660, 280, 141, 51))
        self.bntt_buscar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_buscar.setStyleSheet("QPushButton {\n"
        "    border-radius: 20px;\n"
        "    background-color: rgb(24, 71, 113);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    color: rgb(24, 71, 113);\n"
        "}")
        self.bntt_buscar.setObjectName("bntt_buscar")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(70, 370, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.txt_id_reserva = QtWidgets.QLineEdit(parent=Form)
        self.txt_id_reserva.setGeometry(QtCore.QRect(320, 380, 281, 31))
        self.txt_id_reserva.setStyleSheet("QLineEdit{\n"
        "border:opx;\n"
        "border-bottom:2px solid rgb(24, 71, 113);\n"
        "}")
        self.txt_id_reserva.setObjectName("txt_id_reserva")
        self.bntt_gen_factura = QtWidgets.QPushButton(parent=Form)
        self.bntt_gen_factura.setGeometry(QtCore.QRect(630, 460, 141, 51))
        self.bntt_gen_factura.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bntt_gen_factura.setStyleSheet("QPushButton {\n"
        "    border-radius: 20px;\n"
        "    background-color: rgb(24, 71, 113);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(171, 235, 198 );\n"
        "    color: rgb(255, 255, 255);\n"
        "}")
        self.bntt_gen_factura.setObjectName("bntt_gen_factura")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(260, 300, 121, 16))
        self.label_10.setObjectName("label_10")
        self.txt_busc = QtWidgets.QLineEdit(parent=Form)
        self.txt_busc.setGeometry(QtCore.QRect(370, 290, 271, 31))
        self.txt_busc.setObjectName("txt_busc")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 1441, 601))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255,0.9);\n"
        "border-radius:20px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 1441, 71))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255,0.9);\n"
        "border-radius:20px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.txt_usuario_reser_2 = QtWidgets.QLineEdit(parent=Form)
        self.txt_usuario_reser_2.setGeometry(QtCore.QRect(890, 380, 281, 31))
        self.txt_usuario_reser_2.setStyleSheet("QLineEdit{\n"
        "border:opx;\n"
        "border-bottom:2px solid rgb(24, 71, 113);\n"
        "}")
        self.txt_usuario_reser_2.setObjectName("txt_usuario_reser_2")
        self.label_12 = QtWidgets.QLabel(parent=Form)
        self.label_12.setGeometry(QtCore.QRect(640, 370, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_15.raise_()
        self.label_5.raise_()
        self.bntt_regresar.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.txt_busc.raise_()
        self.bntt_buscar.raise_()
        self.txt_id_reserva.raise_()
        self.bntt_gen_factura.raise_()
        self.label_11.raise_()
        self.txt_usuario_reser_2.raise_()
        self.label_12.raise_()
        self.bntt_regresar.clicked.connect(self.open_regresar)
        self.bntt_buscar.clicked.connect(self.buscar_reserva)
        self.bntt_gen_factura.clicked.connect(self.realizar_boleta)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "MARK\'S"))
        self.label_5.setText(_translate("Form", "RESERVAS"))
        self.bntt_regresar.setText(_translate("Form", "REGRESAR"))
        self.bntt_buscar.setText(_translate("Form", "BUSCAR"))
        self.label_11.setText(_translate("Form", "TIPO DE LA HABITACIÓN"))
        self.bntt_gen_factura.setText(_translate("Form", "GENERAR FACTURA"))
        self.label_10.setText(_translate("Form", "CÓDIGO DE RESRVA"))
        self.label_12.setText(_translate("Form", "ID DEL USUARIO"))

    def buscar_reserva(self):
        if not self.txt_busc.text():
            QMessageBox.warning(self, "Advertencia", "El campo no puede estar vacío.")
        else:
            QMessageBox.information(self, "Correcto", "Reservacion encontrada.")
            try:
                id_reserva = self.txt_busc.text().upper()
                sql = f"SELECT * FROM Reserva WHERE Reserva_ID = {id_reserva}"
                print(sql)
                self.result = conexion.resultadoSQL(sql)
                if len(self.result) != 0:
                    idUsuario = self.result[0][2]
                    sql1 = f"SELECT * FROM Cliente WHERE DNI_Cliente = {idUsuario}"
                    print(sql1)
                    self.result1 = conexion.resultadoSQL(sql1)
                    self.txt_id_reserva.setText(str(self.result[0][3]))
                    self.txt_usuario_reser_2.setText(str(self.result1[0][1]))
                else:
                    QMessageBox.information(None, "No existe la reserva", "Ingrese una reserva Valida")

            except Exception as e:
                print("Error en la función buscar_reserva:", e)


    def open_regresar(self):
        self.close()
        self.ventana_prin.show()

    def realizar_boleta(self,id_resv):
        try:
            id_resv = self.txt_busc.text().upper()
            sql1 = f"SELECT * FROM reserva WHERE Reserva_ID = {id_resv}"
            print(sql1)
            datos = conexion.resultadoSQL(sql1)
            dni = datos[0][2]
            if datos[0][6] == "Confirmado":
                pdf = FPDF()

                pdf.add_page()
                sql = "SELECT MAX(Factura_ID) AS UltimoCambioID FROM Factura;"
                print(sql)
                s = conexion.resultadoSQL(sql)
                a = s[0][0]

                pdf.set_font("Arial", size=12)
                fecha_actual = date.today()

                pdf.cell(0, 10, txt="MARK'S HOTEL", ln=True, align="C")
                pdf.set_font("Arial", size=10)
                pdf.cell(0, 10, txt="Dirección: Alonso de Molina 1433, Lima, Perú", ln=True, align="C")
                pdf.cell(0, 10, txt=f"Fecha de emisión: {fecha_actual}", ln=True, align="C")
                pdf.cell(0, 10, txt=f"Número de boleta: 00{a}", ln=True, align="C")
                m=f"00{a}"
                pdf.ln(10)
                pdf.cell(0, 0, "", border=1, ln=True)

                pdf.set_font("Arial", size=12)
                pdf.cell(40, 10, txt="Fecha Entrada", border=1, align="C")
                pdf.cell(60, 10, txt="Descripción", border=1, align="C")
                pdf.cell(30, 10, txt="Piso", border=1, align="C")
                pdf.cell(40, 10, txt="Fecha Salida", border=1, align="C")
                pdf.cell(30, 10, txt="Precio", border=1, align="C")
                pdf.ln(10)
                precio_parcial = 0
                for i in datos:

                    sql2 = f"SELECT * FROM Habitacion WHERE Habitacion_ID = {i[3]}"
                    print(sql2)
                    datos2 = conexion.resultadoSQL(sql2)
                    if len(i) > 4:
                        pdf.cell(40, 10, txt=str(i[4]), border=1, align="C")
                    else:
                        pdf.cell(40, 10, txt="N/A", border=1, align="C")
                    if len(datos2) > 0 and len(datos2[0]) > 2:
                        pdf.cell(60, 10, txt=str(datos2[0][1]), border=1, align="C")
                        pdf.cell(30, 10, txt=str(datos2[0][2]), border=1, align="C")
                    else:
                        pdf.cell(60, 10, txt="N/A", border=1, align="C")
                        pdf.cell(30, 10, txt="N/A", border=1, align="C")
                    pdf.cell(40, 10, txt=str(i[5]), border=1, align="C")
                    try:    precio_parcial += int(datos2[0][6])
                    except ValueError:    print(f"Error: El valor '{datos2[0][6]}' no es un n%C3%BAmero.")
                    pdf.cell(30, 10, txt=str(datos2[0][6]), border=1, align="C")
                    pdf.ln(10)

                pdf.cell(0, 0, "", border=1, ln=True)

                pdf.cell(0, 10, txt="Extra", ln=True, align="C")
                pdf.ln(10)
                pdf.cell(0, 0, "", border=1, ln=True)

                pdf.set_font("Arial", size=12)
                pdf.cell(60, 10, txt="Descripción", border=1, align="C")
                pdf.cell(20, 10, txt="Precio", border=1, align="C")
                pdf.ln(10)

                sql3 = f"SELECT * FROM ServiciosExtra WHERE Reserva_ID = {id_resv}"
                print(sql3)
                datos3 = conexion.resultadoSQL(sql3)
                for i in datos3:
                    pdf.cell(60, 10, txt=str(i[2]), border=1, align="C")
                    pdf.cell(20, 10, txt=str(i[3]), border=1, align="C")
                    precio_parcial += i[3]
                    pdf.ln(10)
                pdf.cell(0, 0, "", border=1, ln=True)

                pdf.set_font("Arial", size=10)
                pdf.cell(0, 10, txt=f"PRECIO TOTAL = S/.{precio_parcial}", ln=True, align="C")
                pdf.cell(0, 10, txt="Política de cancelación: 24 horas antes de la llegada", ln=True, align="C")
                pdf.cell(0, 10, txt="Política de privacidad: Tus datos serán tratados con confidencialidad", ln=True, align="C")
                nombre_arch  = f"boleta{a}_{uuid.uuid4()}.pdf"
                pdf.output(nombre_arch)


                sql6 = f"SELECT * FROM Cliente WHERE DNI_Cliente = {dni}"
                print(sql6)
                reuslt10 = conexion.resultadoSQL(sql6)
                correo = reuslt10[0][4]
                self.enviar_correo(correo,nombre_arch)

            else:
                QMessageBox.information(None, "La reserva esta en falta de Pago", "Se debe realizar el pago de la reserva")

        except Exception as e:
            print(f"Error al realizar boleta: {e}")


    def enviar_correo(self, correo, nombre_arch):
        try:
            # Configuración del correo
            sender_email = "fabri21arones@gmail.com"
            receiver_email = correo
            password = "csoepibflteeurcv"

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = "MARK´s Hotel FActura electronica"

            body = "Adjunto encontrarás el archivo PDF generado."
            msg.attach(MIMEText(body, 'plain'))

            filename = f"{nombre_arch}"
            if os.path.isfile(filename):
                attachment = open(filename, "rb")
            else:
                print(f"Error: El archivo {filename} no existe.")
            attachment = open(filename, "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")

            msg.attach(part)

            # Conectar al servidor SMTP y enviar el correo
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
        except Exception as e:
            print(f"Error al enviar el correo: {e}")

    def __init__(self, dato, ventana_principal):
        super().__init__()
        self.id_user = dato
        self.ventana_prin = ventana_principal
        self.setupUi(self)


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_Form2()
    window.show()
    sys.exit(app.exec())