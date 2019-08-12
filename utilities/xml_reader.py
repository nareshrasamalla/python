from lxml import etree



def getXMLdatafromFile(filePath):

    doc = etree.parse(filePath)
    return etree.tostring(doc, pretty_print=True).decode()


#getXMLdatafromFile("D:\Python\pythonSelenium\pythonSelenium\\resources\\apiTestData\BSI\ERQ\ERQ_v3.3_Request.XML")
