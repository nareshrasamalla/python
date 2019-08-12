"""
    This Utility file handles file operations
    1. Create new folder
    2. Copy File
    3. Zip the Folder
    4. Rename File
    5. Remove Folder

"""

import os
from zipfile import ZipFile
import config_reader as cr
import shutil

#Load the Configurations
ftp_configurations = cr.get_config_by_section("FTP_CONFIG")
    
    
#Creating Folder in the specified location    
# @path : path for the new folder to be create
# @directory_name : Name of the Folder
def create_folder(path, directory_name):
    print("Starting creating folder")
    try:
        # Create target Directory
        os.mkdir(path+"//"+directory_name)
        print("Directory ", directory_name,  " Created ") 
    except FileExistsError:
        print("Directory ", directory_name,  " already exists")
    
# Copy file from one location to another location   
# @ src_file : source file to be copy
# @ tgt_path : path for the file to be copy
# @ new_file_name : file name for the coping file
def copy_file(src_file, tgt_path, new_file_name):
    # Getting Source & Target file extensions
    extension = os.path.splitext(src_file)[1][1:]
    new_file_extension = os.path.splitext(new_file_name)[1][1:]
    
    # Checking if Target file has extension or not
    if not new_file_extension:
        new_file_name = new_file_name+"."+extension 
        
    tgt_file = tgt_path+"//"+new_file_name
    
    try:
        shutil.copy2(src_file, tgt_file)
        print("File Copy is Done")
    except shutil.Error as e:
        print('Error: %s' % e)


# Zip the folder
# @ directory : folder to be zipped (path)
# @target_location : where we need to place the zipped directory
def zip_folder(directory, target_location=None):
    try:
        tgt_path = directory if target_location is None else target_location

        os.chdir(tgt_path)

        output_dirname = os.path.basename(directory)

        # make_archive(output_filename, 'zip', dir_name)
        shutil.make_archive(output_dirname, 'zip', directory)
        print("Zipped successfully")
    except Error as err:
        print(err)


# Rename File        
def rename_file(src, tgt):
    os.rename(src,tgt)    
    
# Delete Directory
def remove_directory(directory):
    ## Try to remove tree; if failed show an error using try...except on screen
    try:
        shutil.rmtree(directory)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    