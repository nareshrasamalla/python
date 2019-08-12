# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:35:12 2019

@author: AShete
"""
    
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import random
from io import BytesIO
import re
import io
from pdf2jpg import pdf2jpg
import os
import time
import file_utility as file


def read_pdf_as_text(pdf):
    # Cast to StringIO object
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    manager = PDFResourceManager()

    # retstr = BytesIO()
    retstr = StringIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(pdf, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()

    print(text)

    filepath.close()
    device.close()
    retstr.close()
    return text
    
def read_pdfpage_as_image(pdf,directory,cert_no):
    tgt_img_dir = os.path.basename(pdf) + "_dir"

    pdf2jpg.convert_pdf2jpg(pdf,directory,dpi=150,pages="ALL")
    
    tgt_folder = directory+"/"+tgt_img_dir

    img_list = os.listdir(tgt_folder) 
    file_count = len(img_list)

    index = 0

    for fname in os.listdir(tgt_folder):
        src_file = tgt_folder+"/"+fname
        tgt_path = directory
       
        timestamp=time.time()
        random_number=random.randint(10000000,99999999)

      
        #tgt_path = tgt_path + "/"+ cert_no +  "_" + str(timestamp)
        tgt_path = tgt_path + "/" + cert_no +  "_" + str(random_number)
        
        if file_count > 1:
            index += 1
            tgt_path = tgt_path + "_" + str(index) + ".jpg" 
        else:
            tgt_path = tgt_path + ".jpg"
        
        file.rename_file(src_file, tgt_path)
        
        
    file.remove_directory(tgt_folder)     
    
    



