import requests
from utilities import xml_reader



headers = {"Content-Type": "application/xml"}
request_data = xml_reader.getXMLdatafromFile("D:\Python\pythonSelenium\pythonSelenium\\resources\\apiTestData\BSI\ERQ\ERQ_v3.3_Request.XML")
response = requests.post(url="https://EDI.QAT.NMICORE.COM/NMISync", data=request_data, headers=headers,verify=False)
print(response.content)