import PyPDF2 as pypdf #https://mstamy2.github.io/PyPDF2/

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
            salida=str(x)+"_"+archivo+".pdf"
            x=x+1
            with open(salida, "wb") as outFile:
                licencia.write(outFile)
