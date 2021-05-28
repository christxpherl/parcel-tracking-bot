
################################################################################
##
## 
## BY: CHRISTOPHER L. ZAMORA
## FRONT END: Qt Designer and PySide2
## BACK END: Selenium and Pandas
## V: 1.0.0
##
################################################################################

import sys
import platform

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow
from PySide2.QtWidgets import *


## ==> IMPORTAR SPLASHCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> IMPORTAR SCRIPTS 
import append

## ==> VARIABLE GLOBAL
counter = 0

## ==> VENTANA PRINCIPAL
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ## ==> BOTON PROVEEDOR CEVA
        self.buttonCeva = QPushButton('', self)
        self.buttonCeva.setGeometry(50,20,150, 150)
        self.buttonCeva.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\CEVA.ico"))
        self.buttonCeva.setIconSize(QtCore.QSize(150,150))
        self.buttonCeva.clicked.connect(self.getDataCeva)
        self.buttonCeva.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> BOTON PROVEEDOR DHL
        self.buttonDHL = QPushButton('', self)
        self.buttonDHL.setGeometry(250,20,150, 150)
        self.buttonDHL.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\DHL.ico"))
        self.buttonDHL.setIconSize(QtCore.QSize(140,140))
        self.buttonDHL.clicked.connect(self.getDataDHL)
        self.buttonDHL.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> BOTON PROVEEDOR EXPEDITORS
        self.buttonExpe = QPushButton('', self)
        self.buttonExpe.setGeometry(450,20,150, 150)
        self.buttonExpe.clicked.connect(self.getDataExpeditors)
        self.buttonExpe.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\EXPEDITORS.ico"))
        self.buttonExpe.setIconSize(QtCore.QSize(130,130))
        self.buttonExpe.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> BOTON PROVEEDOR FEDEX
        self.buttonFedEx = QPushButton('', self)
        self.buttonFedEx.setGeometry(50,190,150, 150)
        self.buttonFedEx.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\Fedex.ico"))
        self.buttonFedEx.setIconSize(QtCore.QSize(130,130))
        self.buttonFedEx.clicked.connect(self.getDataFedEx)
        self.buttonFedEx.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> BOTON PROVEEDOR UPS
        self.buttonUps = QPushButton('', self)
        self.buttonUps.setGeometry(250,190,150, 150)
        self.buttonUps.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\UPS.ico"))
        self.buttonUps.setIconSize(QtCore.QSize(120,120))
        self.buttonUps.clicked.connect(self.getDataUps)
        self.buttonUps.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> BOTON PROVEEDOR UPS-SCS
        self.buttonUpsScs = QPushButton('', self)
        self.buttonUpsScs.setGeometry(450,190,150, 150)
        self.buttonUpsScs.setIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\UPSSCS.ico"))
        self.buttonUpsScs.setIconSize(QtCore.QSize(200,200))
        self.buttonUpsScs.clicked.connect(self.getDataUpsScs)
        self.buttonUpsScs.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(78, 88, 110); border: 1px rgb(78, 88, 100);border-radius: 5px; font-weight: bold;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(29,205,254,1), stop:1 rgba(52,245,197,1))"
                                    "}"
                                    )

        ## ==> FORMATO DE VENTANA
        self.resize(680,400)
        self.setWindowTitle("TRACKING BOT")
        self.setStyleSheet("color: rgb(220, 220, 220);background: rgb(47, 69, 92); border-radius: 20px;")  
        self.setWindowIcon(QtGui.QIcon(r"D:\Programación\Tracking_Bot\imageformats\WindowIcon.ico"))

        
  
        
    ## ==> FUNCION PARA EJECUTAR BOT CEVA
    def getDataCeva(self):
        text, result = QInputDialog.getText(self, 'CEVA', 'Ingresa numero/s de guia:  ')
        if result == True:            
            append.BotScript.CevaScript(text)

    ## ==> FUNCION PARA EJECUTAR BOT DHL
    def getDataDHL(self):
        text, result = QInputDialog.getText(self, 'DHL' , 'Ingresa numero/s de guia:  ')
        if result == True:            
            append.BotScript.DHLScript(text)

    ## ==> FUNCION PARA EJECUTAR BOT EXPEDITORS
    def getDataExpeditors(self):
        text, result = QInputDialog.getText(self, 'Expeditors', 'Ingresa numero/s de guia: ')
        if result == True:            
            append.BotScript.ExpeditorsScript(text)
        
    ## ==> FUNCION PARA EJECUTAR BOT FEDEX
    def getDataFedEx(self):
        text, result = QInputDialog.getText(self, 'FedEx', 'Ingresa numero/s de guia: ')
        if result == True:            
            append.BotScript.FedExScript(text)

    ## ==> FUNCION PARA EJECUTAR BOT UPS
    def getDataUps(self):
        text, result = QInputDialog.getText(self, 'UPS', 'Ingresa numero/s de guia: ')
        if result == True:            
            append.BotScript.UpsScript(text)

    ## ==> FUNCION PARA EJECUTAR BOT UPS-SCS
    def getDataUpsScs(self):
        text, result = QInputDialog.getText(self, 'UPS-SCS', 'Ingresa numero/s de guia: ')
        if result == True:            
            append.BotScript.UpsScsScript(text)

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> ELIMINAR BARRA DE TITULOS
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## ==> EFECTO DE SOMBRA
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## ==> QTIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        ## ==> TIMER EN MS
        self.timer.start(35)

        ## ==> TEXTO INICIAL
        self.ui.label_description.setText("<strong>BIENVENIDO</strong> ")

        ## ==> TEXTOS ADICIONALES
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> DATOS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> ENTORNO"))


        ## ==> MOSTRAR VENTANA PRINCIPAL
        self.show()

    def progress(self):

        global counter

        ## ==> ASIGNAR VALOR 
        self.ui.progressBar.setValue(counter)

        ## ==> CERRAR SPLASH SCREEN Y ABRIR APLICACION PRINCIPAL
        if counter > 100:

            ## ==> DETENER TIMER
            self.timer.stop()

            ## ==> MOSTRAR VENTANA PRINCIPAL
            self.main = MainWindow()
            self.main.show()

            ## ==> CERRAR SPLASH SCREEN
            self.close()

        ## ==> INCREMENTAR CONTADOR
        counter += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()

    sys.exit(app.exec_())
