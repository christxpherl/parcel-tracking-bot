################################################################################
##
## 
## BY: CHRISTOPHER L. ZAMORA
## BOT SCRIPTS
## < Selenium and Pandas >
##
################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd 
import time

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



class BotScript:

    #BOT DE PROVEEDOR CEVA
    def CevaScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)

            #En caso de que el numero de guia no inicie con "1Z"
            if not i.startswith("WZ"):

                #Mensaje de error de formato
                formatmsg = QMessageBox()
                formatmsg.setIcon(QMessageBox.Critical)
                formatmsg.setText("Formato invalido | Favor de verificar")
                formatmsg.setWindowTitle("Error")
                formatmsg.exec_()

            #En caso de que el numero de carcateres no sea igual a 18
            elif LenTrackingN != 8:

                #Mensaje de error numero de caracteres 
                numbermsg = QMessageBox()
                numbermsg.setIcon(QMessageBox.Critical)
                numbermsg.setText("Numero de caracteres invalido | Favor de verificar")
                numbermsg.setWindowTitle("Error")
                numbermsg.exec_()

            #Siempre y cuando cumpla con el formato el script continua
            else:

                #Opciones de navegacion 
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                options.add_argument('--disable-extensions')

                #Direccion del driver(Google Chrome)
                driverPath = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(driverPath, options=options)

                #Inicializacion del navegador
                driver.get('https://www.cevalogistics.com/en/ceva-trak?transport_mode=all&codes=')

                #Cerrar ventana de cookies
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#CybotCookiebotDialogBodyButtonAccept')))\
                        .click()

                #Enviar numero de guia en campo de texto
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea#tracking_codes')))\
                        .send_keys(i)
                
                #Click en el boton "Submit"
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#btn-track')))\
                        .click()

                #Esperar a que se despliegue tabla de datos 
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ceva-track--airground--result')))\
                        .click()

                #Obtener nombre de proveedor
                carrier = "Ceva Logistics"
                carrierList = [carrier]

                #Obtener numero de envio
                trackingID = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[1]/p/span[2]')
                trackingID = trackingID.text
                trackIDList = [trackingID]

                #Obtener dia de envio
                shipDate = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[4]/div/div[1]/div[1]/span')
                shipDate = shipDate.text
                shipDateList = [shipDate]

                #Obtener fecha de entrega
                delDate = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[4]/div/div[1]/div[3]/span')
                delDate = delDate.text  
                delDateList = [delDate]    

                #Obtener origen
                origen = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[4]/div/div[2]/div[1]/span')
                origen = origen.text
                origenList = [origen]

                #Obtener lugar de destino
                destination = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[4]/div/div[2]/div[2]/span')
                destination = destination.text
                destList = [destination]

                #Obtener estado de envio
                status = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/div/div/div[3]/div/section/div/div[3]/div/div[6]/span[2]')
                status = status.text
                statusList = [status]

                #Almacenar datos obtenidos en un arreglo
                elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                        'Origen': origenList, 'Destino': destList, 'Estado De Envio': statusList})

                #Obtener DataFrame
                df = pd.DataFrame(elements)  

                #Cerrar navegador
                driver.quit()

                

        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_CEVA.csv', index = False)

        #Mensaje de finalizacion
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("CEVA")
        formatmsg.exec_()

        
    #BOT DE PROVEEDOR DHL
    def DHLScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)

            #En caso de que el numero de carcateres no sea igual a 10
            if LenTrackingN != 10:

                #Mensaje de error numero de caracteres
                numbermsg = QMessageBox()
                numbermsg.setIcon(QMessageBox.Critical)
                numbermsg.setText("Numero de caracteres invalido | Favor de verificar")
                numbermsg.setWindowTitle("Error")
                numbermsg.exec_()


            #Siempre y cuando cumpla con el formato el script continua
            else:

                #Opciones de navegacion 
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                options.add_argument('--disable-extensions')

                #Direccion del driver(Google Chrome)
                driverPath = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(driverPath, options=options)

                #Inicializacion del navegador
                driver.get('https://www.dhl.com/global-en/home/tracking.html')

                #Acepta cookies
                WebDriverWait(driver, 10)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#accept-recommended-btn-handler')))\
                        .click()

                #Enviar numero de guia en campo de texto
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.c-tracking-bar--input.js--tracking--input-field.l-grid--w-auto-s.l-grid--w-75pc-m')))\
                        .send_keys(i)

                #Click en el boton "Submit"
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.c-tracking-input--button.js--tracking--input-submit.base-button.l-grid--w-20-s.has-icon.icon-arrow-link')))\
                        .click()

                #Click en menu de detalles
                WebDriverWait(driver, 10)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.c-tracking-result--moredetails-dropdown-button.js--dropdown-moredetails-toggle-btn.js-tracking-result--checkpoints--toggle-btn.has-icon.l-grid--w-100pc-s.l-grid--w-100pc-m')))\
                        .click()

                #Obtener nombre de proveedor
                carrier = "DHL"
                carrierList = [carrier]

                #Obtener numero de envio
                trackingID = driver.find_element_by_xpath('/html/body/div[4]/main/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[2]')
                trackingID = trackingID.text
                trackIDList = [trackingID]

                #Obtener fecha de entrega
                delDate = driver.find_element_by_css_selector('div.c-tracking-result--status-copy-date')
                delDate = delDate.text  
                delDateList = [delDate]    

                #Obtener lugar de origen
                origen = driver.find_element_by_css_selector('h5.c-tracking-result--origin')
                origen = origen.text
                origenList = [origen]

                #Obtener lugar de destino
                destination = driver.find_element_by_css_selector('h5.c-tracking-result--destination.icon-currentlocation')
                destination = destination.text
                destList = [destination]

                #Obtener estado de envio
                status = driver.find_element_by_css_selector('h3.c-tracking-result--status-copy-message')
                status = status.text
                statusList = [status]

                #Scroll Down
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                #Obtener dia de envio
                shipDate = driver.find_element_by_css_selector('h4.c-tracking-result--checkpoint--date.l-grid--w-100pc-s')
                shipDate = shipDate.text
                shipDateList = [shipDate]

                #Almacenar datos obtenidos en un arreglo
                elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                        'Origen': origenList, 'Destino': destList, 'Estado De Envio': statusList})

                #Obtener DataFrame
                df = pd.DataFrame(elements)  

                #Cerrar navegador
                driver.quit()

        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_DHL.csv', index = False)

        #Mensaje de finalizacion 
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("DHL")
        formatmsg.exec_()

    #BOT DE PROVEEDOR EXPEDITORS
    def ExpeditorsScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)


            #En caso de que el numero de carcateres no sea igual a 10
            if LenTrackingN == 10:
                
                #Opciones de navegacion 
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                options.add_argument('--disable-extensions')

                #Direccion del driver(Google Chrome)
                driverPath = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(driverPath, options=options)

                #Inicializacion del navegador
                driver.get('http://expo.expeditors.com/expo/ExpoReport/SQGuestDetail.jsp')

                #Enviar numero de guia en campo de texto
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#TrackingNumber')))\
                        .send_keys(i)
                
                #Click en el boton "Submit"
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#guestTrack')))\
                        .click()

                #Obtener nombre de proveedor
                carrier = "Expeditors"
                carrierList = [carrier]

                #Obtener numero de envio
                trackingID = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/span[2]')
                trackingID = trackingID.text
                trackIDList = [trackingID]

                #Obtener dia de envio
                shipDate = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div/table/tbody/tr[6]/td[1]')
                shipDate = shipDate.text
                shipDateList = [shipDate]

                #Obtener fecha de entrega
                delDate = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/span[2]')
                delDate = delDate.text  
                delDateList = [delDate]    

                #Obtener origen
                origen = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/span[1]')
                origen = origen.text
                origenList = [origen]

                #Obtener lugar de destino
                destination = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/span[2]')
                destination = destination.text
                destList = [destination]

                #Obtener estado de envio
                status = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/span[1]')
                status = status.text
                statusList = [status]

                #Almacenar datos obtenidos en un arreglo
                elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                        'Origen': origenList, 'Destino': destList, 'Estado De Envio': statusList})

                #Obtener DataFrame
                df = pd.DataFrame(elements)  

                #Cerrar navegador
                driver.quit()


            #Siempre y cuando cumpla con el formato el script continua
            else:

                #Mensaje de error numero de caracteres
                numbermsg = QMessageBox()
                numbermsg.setIcon(QMessageBox.Critical)
                numbermsg.setText("Numero de caracteres invalido | Favor de verificar")
                numbermsg.setWindowTitle("Error")
                numbermsg.exec_()

        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_Expeditors.csv', index = False)

        #Mensaje de finalizacion 
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("EXPEDITORS")
        formatmsg.exec_()

    #BOT DE PROVEEDOR FEDEX
    def FedExScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)

            #En caso de que el numero de carcateres no sea igual a 12 o 15
            if LenTrackingN == 12 or LenTrackingN == 15: 
                
                #Opciones de navegacion 
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                options.add_argument('--disable-extensions')

                #Direccion del driver(Google Chrome)
                driverPath = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(driverPath, options=options)

                #Inicializacion del navegador
                driver.get('https://www.fedex.com/es-mx/tracking.html')

                #Enviar numero de guia en campo de texto
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#track_inbox_track_numbers_area')))\
                        .send_keys(i)
                
                #Click en el boton "Submit"
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div[4]/div/div/div/div[2]/div/div/form/div/div/form/div[1]/div/button')))\
                        .click()
                
                #Click menu de datos de envio
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#tab-list-item-tab_panel_3')))\
                        .click()

                #Esperar a que se despliegue tabla de datos 
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div')))\
                        .click()

                #Obtener nombre de proveedor
                carrier = "FedEx"
                carrierList = [carrier]

                #Obtener numero de envio
                trackingID = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/section[1]/div[1]/div[1]/trk-shared-shipment-identifier/div/div')
                trackingID = trackingID.text
                trackIDList = [trackingID]

                #Obtener dia de envio
                shipDate = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/trk-shared-detail-view-tabs/trk-shared-tab-group/trk-shared-tab[2]/div/div/trk-shared-shipment-facts/trk-shared-key-value-list/ul/li[5]/div')
                shipDate = shipDate.text
                shipDateList = [shipDate]

                #Obtener fecha de entrega
                delDate = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/trk-shared-detail-view-tabs/trk-shared-tab-group/trk-shared-tab[2]/div/div/trk-shared-shipment-facts/trk-shared-key-value-list/ul/li[6]/div')
                delDate = delDate.text  
                delDateList = [delDate]    

                #Obtener origen
                origen = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/section[1]/div[3]/trk-shared-to-from/div/div[1]/trk-shared-address/div/div[2]')
                origen = origen.text
                origenList = [origen]

                #Obtener lugar de destino
                destination = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/section[1]/div[3]/trk-shared-to-from/div/div[2]/trk-shared-address/div/div[2]')
                destination = destination.text
                destList = [destination]

                #Obtener estado de envio
                status = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/ng-component/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page/trk-shared-stylesheet-wrapper/div/div/trk-shared-detail-page-default/div/div/section[1]/trk-shared-shipment-status-text/div/h3[1]')
                status = status.text
                statusList = [status]

                #Almacenar datos obtenidos en un arreglo
                elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                        'Origen': origenList, 'Destino': destList, 'Estado De Envio': statusList})

                #Obtener DataFrame
                df = pd.DataFrame(elements)  

                #Cerrar navegador
                driver.quit()

            #Siempre y cuando cumpla con el formato el script continua
            else:

                #Mensaje de error numero de caracteres 
                numbermsg = QMessageBox()
                numbermsg.setIcon(QMessageBox.Critical)
                numbermsg.setText("Numero de caracteres invalido | Favor de verificar")
                numbermsg.setWindowTitle("Error")
                numbermsg.exec_()

        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_FedEx.csv', index = False)

        #Mensaje de finalizacion 
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("FEDEX")
        formatmsg.exec_()

    #BOT DE PROVEEDOR UPS   
    def UpsScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)

            #En caso de que el numero de guia no inicie con "1Z"
            if not i.startswith("1Z"):

                #Mensaje de error formato
                formatmsg = QMessageBox()
                formatmsg.setIcon(QMessageBox.Critical)
                formatmsg.setText("Formato invalido | Favor de verificar")
                formatmsg.setWindowTitle("Error")
                formatmsg.exec_()


            #En caso de que el numero de carcateres no sea igual a 18
            elif LenTrackingN != 18:
                
                #Mensaje de error numero de caracteres 
                numbermsg = QMessageBox()
                numbermsg.setIcon(QMessageBox.Critical)
                numbermsg.setText("Numero de caracteres invalido | Favor de verificar")
                numbermsg.setWindowTitle("Error")
                numbermsg.exec_()


            #Siempre y cuando cumpla con el formato el script continua
            else:

                #Opciones de navegacion 
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                options.add_argument('--disable-extensions')

                #Direccion del driver(Google Chrome)
                driverPath = "C:\Program Files (x86)\chromedriver.exe"
                driver = webdriver.Chrome(driverPath, options=options)

                #Inicializacion del navegador
                driver.get('https://www.ups.com/track?loc=es&requester=ST/')

                #Cerrar ventana de cookies
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.close_btn_thick')))\
                        .click()

                #Enviar numero de guia en campo de texto
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea#stApp_trackingNumber')))\
                        .send_keys(i)
                
                #Click en el boton "Submit"
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#stApp_btnTrack')))\
                        .click()

                #Cerrar ventana de chat
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#tcChat_btnCloseChat_img')))\
                        .click()

                #Obtener estado de envio
                status = driver.find_element_by_css_selector('td#stApp_ShpmtProg_LVP_milestone_name_3')
                status = status.text
                statusList = [status]

                #Click en dettales de envio
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#stApp_btnProofOfDeliveryonDetails')))\
                        .click()

                #Esperar a que despliegue menu
                WebDriverWait(driver, 5)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#stApp_podModal')))\
                        .click()

                #Obtener nombre de proveedor
                carrier = "UPS"
                carrierList = [carrier]

                #Obtener numero de envio
                trackingID = driver.find_element_by_css_selector('p#stApp_PODtxtTrackingNumber')
                trackingID = trackingID.text
                trackIDList = [trackingID]

                #Obtener dia de envio
                shipDate = driver.find_element_by_css_selector('p#stApp_PODtxtAdditionalInfoBilledOn')
                shipDate = shipDate.text
                shipDateList = [shipDate]

                #Obtener fecha de entrega
                delDate = driver.find_element_by_css_selector('p#stApp_PODtxtDeliveredOn')
                delDate = delDate.text  
                delDateList = [delDate]    

                #Obtener lugar de destino
                destination = driver.find_element_by_css_selector('span#stApp_PODtxtCountry')
                destination = destination.text
                destList = [destination]

                #Almacenar datos obtenidos en un arreglo
                elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                         'Destino': destList, 'Estado De Envio': statusList})

                #Obtener DataFrame
                df = pd.DataFrame(elements)  

                #Cerrar navegador
                driver.quit()


        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_UPS.csv', index = False)

        #Mensaje de finalizacion 
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("UPS")
        formatmsg.exec_()

    #BOT DE PROVEEDOR UPS-SCS
    def UpsScsScript(data):

        #Almacenar en arreglo input recibido
        listTrack = [(x) for x in data.split()]

        #Variable global de elementos
        elements = []

        #Secuencia por cada input recibido
        for i in listTrack:

            #Obtener numero de caracteres de valor ingresado
            LenTrackingN = len(i)

            #Opciones de navegacion 
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.add_argument('--disable-extensions')

            #Direccion del driver(Google Chrome)
            driverPath = "C:\Program Files (x86)\chromedriver.exe"
            driver = webdriver.Chrome(driverPath, options=options)

            #Inicializacion del navegador
            driver.get('https://scsapps.ups.com/forwardinghub/tracking/')

            #Cerrar ventana de cookies 
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.close_btn_thick.icon.ups-icon-x')))\
                    .click()

            #Enviar numero de guia en campo de texto
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#trackingNumber')))\
                    .send_keys(i)

            #Click en el boton "Submit"
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.upsgff-primary-cta.btnWidth')))\
                    .click()

            #Esperar a que la pagina se despliegue 
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]')))\
                    .click()

            #Click en menu de detalles adicionales
            WebDriverWait(driver, 5)\
                .until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-additional-details-logged-in/p-accordion/div/p-accordiontab/div[1]')))\
                    .click()

            #Obtener nombre de proveedor
            carrier = "UPS-SCS"
            carrierList = [carrier]

            #Obtener numero de envio
            #trackingID = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-additional-details-logged-in/p-accordion/div/p-accordiontab/div[2]/div/div/div[5]/div[1]/div[2]')
            trackingID = i
            trackIDList = [trackingID]

            #Obtener dia de envio
            shipDate = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-tracking-card/div/div/div/div[3]/p-card/div/div[2]/div/div/ups-gff-shipment-tracker/ul/li[1]/div[1]/div/span[2]')
            shipDate = shipDate.text
            shipDateList = [shipDate]

            #Obtener fecha de entrega
            delDate = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-tracking-card/div/div/div/div[3]/p-card/div/div[2]/div/div/ups-gff-shipment-tracker/ul/li[6]/div[1]/div/span[2]')
            delDate = delDate.text  
            delDateList = [delDate]    

            #Obtener origen
            origen = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-additional-details-logged-in/p-accordion/div/p-accordiontab/div[2]/div/div/div[7]/div[1]/div[2]')
            origen = origen.text
            origenList = [origen]

            #Obtener lugar de destino
            destination = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-additional-details-logged-in/p-accordion/div/p-accordiontab/div[2]/div/div/div[7]/div[2]/div[2]')
            destination = destination.text
            destList = [destination]

            #Obtener estado de envio
            status = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div[2]/ups-gff-track-wrapper/gff-track/ups-gff-new-search/div[3]/div/ups-gff-tracking-card/div/div/div/div[1]/p-card/div/div[2]/div/div/div[1]/div[2]')
            status = status.text
            statusList = [status]

            #Almacenar datos obtenidos en un arreglo
            elements.append({'Proveedor': carrierList, 'Numero Guia': trackIDList, 'Dia De Envio': shipDateList, 'Dia De Llegada': delDateList,\
                                        'Destino': destList, 'Estado De Envio': statusList})

            #Obtener DataFrame
            df = pd.DataFrame(elements)  

            #Cerrar navegador
            driver.quit()


        #Exportar datos en archivo .csv(Excel)
        df.to_csv('Tracking_Details_UPSSCS.csv', index = False)

        #Mensaje de finalizacion 
        formatmsg = QMessageBox()
        formatmsg.setIcon(QMessageBox.Information)
        formatmsg.setText("PROCESO FINALIZADO")
        formatmsg.setWindowTitle("UPS-SCS")
        formatmsg.exec_()




        
