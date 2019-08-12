# -*- coding: utf-8 -*-
"""
This file is basically a tester utility to validate different
utility functions.

"""

import db_utility as db
import os
#import pdf_read_utility as pdf
#import ms_word_read_utility as word
#import sftp_utility as sftp
#import word_to_pdf_utility as w2pdf
#import file_utility as file
#import replace_data_utility as replace
import config_reader as cr
#print(os.getcwd())

#pdf.read_pdf_as_text("D:/PythonBDD/pythonSelenium/resources/uiTestData/TestPDF.pdf")
#word.read_document_as_text("D:/PythonBDD/pythonSelenium/resources/uiTestData/Test_NMI.docx")
#db.fetch_results_by_query("Select * from MP_DATA");
#sftp.fetch_file_from_SFTP("/cifs_ebus/orig_ebiz/AMC","AMC_DEL_062119_170506.xlsx")
#sftp.push_file_to_SFTP("/home/prl_c.takkelapat/testing","D:\\PythonBDD\\pythonSelenium\\resources\\uiTestData\\sample.pdf")
#pdf.read_pdfpage_as_image("D:/PythonBDD/pythonSelenium/resources/uiTestData/TestPDF.pdf","D:/PythonBDD/pythonSelenium/resources/uiTestData","12345")
#w2pdf.convert_to_pdf("D:/PythonBDD/pythonSelenium/resources/uiTestData/AppleorangeBankmay.docx","D:/PythonBDD/pythonSelenium/resources/uiTestData/AppleorangeBankmay.pdf")

#file.zip_folder("D:/PythonBDD/pythonSelenium/resources/uiTestData/2600302764_LBC001_0004", "D:/PythonBDD/pythonSelenium/resources/uiTestData")
#file.create_folder("D:/PythonBDD/pythonSelenium/resources/uiTestData", "TestFldr")
#file.copy_file("D:/PythonBDD/pythonSelenium/resources/uiTestData/sample.pdf", "D:/PythonBDD/pythonSelenium/resources/uiTestData", "testfile.pdf")

#dic={"NMI_MI-Commitment_LCK001.jpg":"sample_text_1","NMI_MI-Commitment_LCK004.jpg" : "sample_text_3","NMI_MI-Commitment_LCK002.jpg":"sample_text_2","NMI_MI-Commitment_LCK005.jpg":"sample_text_4","AppleOrangeBank":"GreenAppleBank"}
#replace.replace_dat_doc_data("D:/PythonBDD/pythonSelenium/resources/uiTestData/dat/NMI_MI-Commitment_LCK003.dat",**dic)

#fields = {"AppleOrange": "CITI", "date": "6/8/2019","Description":"Desc","cNumber":"C0123456","certNumber":"256314","Dollors":"256","Cents":"36"}
#replace.replace_word_doc_data("D:/PythonBDD/pythonSelenium/resources/uiTestData/AppleorangeBankmay.docx",**fields)
data=cr.get_config_by_section("B2B_CONFIG")
print(data.get("headers"))