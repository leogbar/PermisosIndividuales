#-------------------------------------------------------------------------------
# Name:        PermisosIndividuales
# Purpose: Emisión de PDF con permisos individuales en funcion de un PDF mayor 
# con ciertas caracteristicas, al cual, hay que borrarle y agregarle cosas en una
# pagina y agregarle paginas modelo.
#
# Author:      Ing. Esp. Leonardo Barenghi
#
# Created:     21/05/2021
# Copyright:   (c) lbarenghi 2021
# Licence:     BSD 3
#-------------------------------------------------------------------------------

import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/ o https://github.com/mstamy2/PyPDF2

with open("modelo.pdf", "rb") as overlay, open("infder1.pdf", "rb") as infder1, open("final.pdf", "rb") as final, open("sirfrar.pdf", "rb") as recorrer, open("nombres.txt", "r") as nombres:

    limpiar = pypdf.PdfFileReader(infder1).getPage(0)
    firma = pypdf.PdfFileReader(overlay).getPage(0)
    final1 = pypdf.PdfFileReader(final).getPage(0)
    original = pypdf.PdfFileReader(recorrer)
    x=1
    for i in range(original.getNumPages()):
            archivo=nombres.readline()
            licencia1 = pypdf.PdfFileWriter()
            licencia1 = original.getPage(i)
            licencia1.mergePage(limpiar)
            licencia1.mergePage(firma)
            licencia = pypdf.PdfFileWriter()
            licencia.addPage(licencia1)
            licencia.addPage(final1)
            #archivo=archivo[:-1] # Sacar comentario si se ejecuta en windows que no quita el "\n" en la concatenacion de strings
            salida=str(x)+"_"+archivo+".pdf"
            x=x+1
            prints("Imprimiendo el archivo: 
            with open(salida, "wb") as outFile:
                licencia.write(outFile)
