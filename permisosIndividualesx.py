#-------------------------------------------------------------------------------
# Name:        PermisosIndividuales v1
# Purpose: Emisión de PDF con permisos individuales de mas de una pagina
#
#
#
# Author:      Ing. Esp. Leonardo Barenghi
#
# Created:     26/05/2021
# Copyright:   (c) lbarenghi 2021
# Licence:     BSD 3
#-------------------------------------------------------------------------------

import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/

with open("fusionar.pdf", "rb") as fusionar, open("borrar.pdf", "rb") as borrar, open("adjunto.pdf", "rb") as final, open("sirfrar2.pdf", "rb") as recorrer:

    print("PermisosIndividuales con más Hojas v1\n")
    print("Emisión de PDF con permisos individuales\n")
    print("Author: Ing. Esp. Leonardo Barenghi\n")
    print("Created:     21/05/2021\n")
    print("Modified:     26/05/2021\n")
    print("Copyright:   (c) lbarenghi 2021\n")
    print("Licence:     BSD 3\n")



    borrarPdf = pypdf.PdfFileReader(borrar).getPage(0)
    fusionarPdf = pypdf.PdfFileReader(fusionar).getPage(0)
    final1 = pypdf.PdfFileReader(final).getPage(0)

    hojas = input('Indique cantidad de hojas del permiso: ')
    nombre = input('Indique nombre del permiso: ')


    original = pypdf.PdfFileReader(recorrer)
    licencia1 = pypdf.PdfFileWriter()
    licencia = pypdf.PdfFileWriter()
    for i in range(int(hojas)):
        print(i)
        licencia1 = original.getPage(i)
        licencia1.mergePage(borrarPdf)
        licencia1.mergePage(fusionarPdf)
        licencia.addPage(licencia1)

    licencia.addPage(final1)
    salida="_"+nombre+".pdf"
    print("Generando "+salida+ "..."+"\n")

    with open(salida, "wb") as outFile:
        licencia.write(outFile)
