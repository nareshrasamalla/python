import lxml
from lxml import etree
from ext import Constants
import os

def updateElementValue(filePath,xpath,value):
    if isinstance(filePath, str):
        doc = etree.parse(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+filePath)
    elif isinstance(filePath, lxml.etree._ElementTree):
        doc = filePath
    #print(etree.tostring(doc, pretty_print=True).decode())
    elements = doc.findall(xpath,Constants.XMLnamespaces)
    elements[0].text = value
    #print(etree.tostring(doc, pretty_print=True).decode())
    return doc

