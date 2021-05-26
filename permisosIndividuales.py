#-------------------------------------------------------------------------------
# Name:        PermisosIndividuales v5
# Purpose: Emisión de PDF con permisos individuales en funcion de un PDF mayor 
# con ciertas caracteristicas, al cual, hay que borrarle y agregarle cosas en una
# pagina y agregarle paginas modelo.
#
# Author:      Ing. Esp. Leonardo Barenghi
#
# Created:     26/05/2021
# Copyright:   (c) lbarenghi 2021
# Licence:     BSD 3
#-------------------------------------------------------------------------------

import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/
from unidecode import unidecode  #(c) Tomaz Solc (GPLv2+) (GPL) https://pypi.org/project/Unidecode/ https://github.com/avian2/unidecode

with open("fusionar.pdf", "rb") as fusionar, open("borrar.pdf", "rb") as borrar, open("adjunto.pdf", "rb") as final, open("sirfrar.pdf", "rb") as recorrer, open("nombres.txt","r", encoding="utf-8") as nombres:

    print("PermisosIndividuales v4\n")
    print("Emisión de PDF con permisos individuales\n")
    print("Author: Ing. Esp. Leonardo Barenghi\n")
    print("Created:     21/05/2021\n")
    print("Modified:     26/05/2021\n")
    print("Copyright:   (c) lbarenghi 2021\n")
    print("Licence:     BSD 3\n")



    borrarPdf = pypdf.PdfFileReader(borrar).getPage(0)
    fusionarPdf = pypdf.PdfFileReader(fusionar).getPage(0)
    final1 = pypdf.PdfFileReader(final).getPage(0)
    original = pypdf.PdfFileReader(recorrer)
    x=1
    for i in range(original.getNumPages()):
            archivo=nombres.readline()
            licencia1 = pypdf.PdfFileWriter()
            licencia1 = original.getPage(i)
            licencia1.mergePage(borrarPdf)
            licencia1.mergePage(fusionarPdf)
            licencia = pypdf.PdfFileWriter()
            licencia.addPage(licencia1)
            licencia.addPage(final1)
            archivo = unidecode(archivo)
            archivo=archivo[:-1]
            salida=str(x)+"_"+archivo+".pdf"
            x=x+1
            print("Generando "+salida+ "..."+"\n")
            with open(salida, "wb") as outFile:
                licencia.write(outFile)
