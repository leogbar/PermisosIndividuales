#-------------------------------------------------------------------------------
# Name:        PermisosIndividuales v4
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

import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/

with open("fusionar.pdf", "rb") as fusionar, open("borrar.pdf", "rb") as borrar, open("adjunto.pdf", "rb") as final, open("sirfrar.pdf", "rb") as recorrer, open("nombres.txt", "r") as nombres:

printf("PermisosIndividuales v4\n")
printf("Emisión de PDF con permisos individuales\n")
printf("Author: Ing. Esp. Leonardo Barenghi\n")
printf("Created:     21/05/2021\n")
printf("Modified:     26/05/2021\n")
printf("Copyright:   (c) lbarenghi 2021\n")
printf("Licence:     BSD 3\n")



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
            #archivo=archivo[:-1] # Sacar comentario si se ejecuta en windows que no quita el "\n" en la concatenacion de strings
            salida=str(x)+"_"+archivo+".pdf"
            x=x+1
            print("Generando "+salida+ "..."+"\n")
            with open(salida, "wb") as outFile:
                licencia.write(outFile)
