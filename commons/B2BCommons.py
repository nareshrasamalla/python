import requests, os
from utilities import xml_reader
from xml.etree import ElementTree
import lxml
from lxml import etree
from ext import Constants


def generateRateQuote(filePath,Type='No Test'):
    doc = hitEndpoint(filePath)
    if Type != 'Test':
        elements =  doc.findall('.//ns0:LoanIdentifier', Constants.XMLnamespaces)
        print("Generate Estimated Rate Quote with ID: " + elements[0].text)
        return elements[0].text
    elif Type == 'Test':
        return doc


def createMIApplication(filePath,Type='No Test'):
    doc = hitEndpoint(filePath)
    if Type != 'Test':
        elements = doc.findall('.//ns0:MICertificateIdentifier', Constants.XMLnamespaces)
        print("Created MI Application with number: "+elements[0].text)
        return elements[0].text
    elif Type == 'Test':
        return doc

def hitEndpoint(filePath):
    request_data = ''
    if isinstance(filePath,str):
        request_data = xml_reader.getXMLdatafromFile(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + filePath)
    elif isinstance(filePath,lxml.etree._ElementTree):
        request_data = etree.tostring(filePath, pretty_print=True).decode()
    else:
        print("")
    response = requests.post(url=Constants.B2BEndpoint, data=request_data, headers=Constants.headers, verify=False)
    print("Received Response from Endpoint Successfully in :" + str(response.elapsed.total_seconds()) + " sec.")
    responseString = response.content.decode("utf-8").replace('\n', '', 1)
    #print("Response :"+responseString)
    return  ElementTree.fromstring(responseString)
