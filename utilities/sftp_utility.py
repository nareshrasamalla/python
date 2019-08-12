# -*- coding: utf-8 -*-
"""
This file contains utility functions to interact with 
FTP.

"""
import config.config_reader as cr
from ftplib import Error
import os
import pysftp
#Load the Configurations
ftp_configurations = cr.get_config_by_section("FTP_CONFIG")

# fetch_file_from_FTP retrives a File from specified directory
# in FTP and copies it to current working directory.
def fetch_file_from_FTP(directory, file):
    fetchVar = None
    tgtFldr = ftp_configurations.get("ftp.target.folder")
    sftp = None
    data=None
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        with pysftp.Connection(host=ftp_configurations.get("ftp.host"), username=ftp_configurations.get("ftp.user"), password=ftp_configurations.get("ftp.password"), cnopts=cnopts) as sftp:
         os.chdir("..")
         cwd=os.getcwd()
         src_file = directory+"/"+file
         tgt_file = os.chdir(cwd+"\\"+tgtFldr)
         sftp.get(src_file,tgt_file)
         print("File "+file+" downloaded successfully!")
         if os.path.splitext(file)[1] == ".txt" :
            fetchVar = open(file,"rb")
            data=fetchVar.read()
#           print(fetchVar.read())
         else:
            print("File is not a text file. Please check the location : "+tgtFldr)
    except Error as err:
         print(err)   
    finally:
        sftp.close()
    return data


# push_file_to_FTP uploads a File in a specified directory
# in FTP.
def push_file_to_FTP(directory, file): 
    sftp = None
    
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        
        with pysftp.Connection(host=ftp_configurations.get("ftp.host"), username=ftp_configurations.get("ftp.user"),            password=ftp_configurations.get("ftp.password"), cnopts=cnopts) as sftp:
        
            with sftp.cd(directory): #chdir to public
                sftp.put(file) 
            
                print("File "+file+" uploaded successfully!")
        
    except Error as err:
        print(err)
    finally:
        sftp.close()


fetch_file_from_FTP('/cifs_ebus/orig_ebiz/AMC','AMC_DEL_062119_170506.xlsx')