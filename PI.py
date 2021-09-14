#-------------------------------------------------------------------------------
# Name:        PermisosIndividuales v8
# Purpose: Emisión de PDF con permisos individuales en funcion de un PDF mayor
# con ciertas caracteristicas, al cual, hay que borrarle y agregarle cosas en una
# pagina y agregarle paginas modelo.
#
# Author:      Ing. Esp. Leonardo Barenghi
#
# Created:     14/09/2021
# Copyright:   (c) lbarenghi 2021 https://github.com/leogbar/PermisosIndividuales
# Licence:     BSD 3
#-------------------------------------------------------------------------------

import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/
from unidecode import unidecode  #(c) Tomaz Solc (GPLv2+) (GPL) https://pypi.org/project/Unidecode/ https://github.com/avian2/unidecode
from reportlab.lib.pagesizes import A4 #(c)  Andy Robinson, Robin Becker, the ReportLab team and the community (BSD) https://pypi.org/project/reportlab/
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
import datetime
import PySimpleGUI as sg #(LGPLv3+) PySimpleGUI https://github.com/PySimpleGUI/PySimpleGUI
from sys import platform

if platform == "linux" or platform == "linux2":
    separador = "/"
elif platform == "win32" or platform == "win64":
    separador = "\\"


salida=[]
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial.ttf'))

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)
    return messsage

now = datetime.datetime.now()


event, values = sg.Window('Generacion de Permisos Individuales v8', [[sg.Text('(c) Ing. Esp. Leonardo Barenghi - 2021 - Licencia bajo BSD 3')],[sg.Text(' ')],[sg.Text('Ingrese dias a partir de hoy:')],[sg.InputText()],
[sg.Radio('Permiso Provisorio', "RADIO1", default=False, key="Permiso0")],
[sg.Radio('Permiso Definitivo', "RADIO1", default=False, key="Permiso1")],
[sg.Text(' ')],
[sg.Radio('Una pagina por Permiso', "RADIO2", default=False, key="cantidad0")],
[sg.Radio('Un permiso con multiples paginas', "RADIO2", default=False, key="cantidad1")],
 [sg.Text('Nombre de Archivo con los Permisos Individuales')], [sg.Input(), sg.FileBrowse()],
 [sg.Text('Cargue el Archivo que contiene los nombres de los permisos:')], [sg.Input(), sg.FileBrowse()],
[sg.Text('Seleccione carpeta de salida:')],  [sg.Input(),sg.FolderBrowse()], [sg.OK(), sg.Cancel()]

 ]).read(close=True)

encabezadof=""
adjuntof=""

if values["Permiso0"] == True:
    encabezadof = "encabezadoProvisorio.pdf"
    adjuntof ="adjuntoProvisorio.pdf"
    titulo = "PermisoProvisorio"
else:
    if values["Permiso1"] == True:
        encabezadof ="encabezadoDefinitivo.pdf"
        adjuntof ="adjuntoDefinitivo.pdf"
        titulo = "PermisoDefinitivo"
    else:
        print("Operación invalida")
        exit()



explorar =  values["Browse"]
nombres = values["Browse0"]
canvas = Canvas("firma.pdf", pagesize=A4)
if len(values[0])<1:
    print("No ingresó la cantidad de días...")
    exit()
else:
    dias = int(values[0])
    
FirmaIni=open("firma.ini","r", encoding="utf-8")
NombreFirma=FirmaIni.readline()
PuestoFirma1=FirmaIni.readline()
PuestoFirma2=FirmaIni.readline()

dias=datetime.timedelta(days=dias)
lugar = "BUENOS AIRES, "
fecha = current_date_format(now+dias)
lugarFecha = lugar + fecha
canvas.setFont("Arial", 10)

tamanoTexto = stringWidth(lugarFecha, "Arial", 10)
ubicacionTexto=(AnchoA4*3/4-tamanoTexto)/2
canvas.drawString(ubicacionTexto, 60, lugarFecha )

tamanoTexto = stringWidth(NombreFirma, "Arial", 10)
ubicacionTexto=(AnchoA4*3/4-tamanoTexto)/2
canvas.drawString(ubicacionTexto, 50, NombreFirma[:-1]) #Nombre de quien firma

canvas.setFont("Times-Roman", 8)

tamanoTexto = stringWidth(PuestoFirma1, "Times-Roman", 8)
ubicacionTexto=(AnchoA4*3/4-tamanoTexto)/2
canvas.drawString(ubicacionTexto, 40, PuestoFirma1[:-1]) #Area a la que pertenece

tamanoTexto = stringWidth(PuestoFirma2, "Times-Roman", 8)
ubicacionTexto=(AnchoA4*3/4-tamanoTexto)/2
canvas.drawString(ubicacionTexto, 30, PuestoFirma2[:-1]) #Area a la que pertenece


canvas.save()

encabezado=open(encabezadof, "rb")
firma=open("firma.pdf", "rb")
borrar=open("borrar.pdf", "rb")
linea=open("linea.pdf", "rb")
adjunto=open(adjuntof, "rb")
anexo=open("anexo.pdf", "rb")
anexoBorrar=open("anexoBorrar.pdf", "rb")
carpeta= values["Browse1"]
if len(explorar)<1:
    print("No ingresó el archivo con los Permisos...")
    exit()
else:
    recorrer=open(explorar, "rb")

if len(nombres)<1:
    nombres="permiso"
else:
    nombres=open(nombres,"r", encoding="utf-8")
if len(carpeta)<1:
    print("No ingresó el archivo con la carpeta de salida...")
    exit()

borrarPdf = pypdf.PdfFileReader(borrar).getPage(0)
encabezadoPdf = pypdf.PdfFileReader(encabezado).getPage(0)
firmaPdf = pypdf.PdfFileReader(firma).getPage(0)
adjuntoPdf = pypdf.PdfFileReader(adjunto).getPage(0)
lineaPdf = pypdf.PdfFileReader(linea).getPage(0)
anexoPdf = pypdf.PdfFileReader(anexo).getPage(0)
anexoBorrarPdf = pypdf.PdfFileReader(anexoBorrar).getPage(0)
original = pypdf.PdfFileReader(recorrer)
x=1

if values["cantidad0"] == True:
    for i in range(original.getNumPages()):
        archivo=nombres.readline()
        licencia1 = pypdf.PdfFileWriter()
        licencia1=original.getPage(i)

        licencia1.mergePage(borrarPdf)
        licencia1.mergePage(encabezadoPdf)
        licencia1.mergePage(lineaPdf)
        licencia1.mergePage(firmaPdf)

        licencia = pypdf.PdfFileWriter()
        licencia.addPage(licencia1)
        licencia.addPage(adjuntoPdf)

        archivo = unidecode(archivo)
        archivo=archivo[:-1]
        salida=carpeta+separador+str(x)+"_"+archivo+".pdf"
        x=x+1
        print("Generando "+salida+ "..."+"\n")
        with open(salida, "wb") as outFile:
            licencia.write(outFile)
    print("Proceso Terminado..."+"\n")
else:
    if values["cantidad1"] == True:
        titulo="permiso"
        fecha='{:%Y%m%d-%H%M%S}'.format(now)
        archivo=titulo+"_"+fecha
        
        licencia = pypdf.PdfFileWriter()

        for i in range(original.getNumPages()):
            if(x==1):
                licencia1 = pypdf.PdfFileWriter()
                licencia1=original.getPage(i)
                licencia1.mergePage(borrarPdf)
                licencia1.mergePage(encabezadoPdf)
                licencia1.mergePage(lineaPdf)
                licencia1.mergePage(firmaPdf)
                licencia.addPage(licencia1)
                licencia.addPage(adjuntoPdf)
                x=x+1
            else:
                licencia1 = pypdf.PdfFileWriter()
                licencia1=original.getPage(i)
                licencia1.mergePage(anexoBorrarPdf)
                licencia1.mergePage(anexoPdf)
                licencia.addPage(licencia1)
                x=x+1

        salida=carpeta+separador+archivo+".pdf"
        print("Generando "+salida+ "..."+"\n")

        with open(salida, "wb") as outFile:
            licencia.write(outFile)
        print("Proceso Terminado..."+"\n")
    else:
        print("No ingresó la cantidad de hojas...")
        exit()
