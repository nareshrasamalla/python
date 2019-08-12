# -*- coding: utf-8 -*-
"""
This file is intended to read the System config file and 
fetch values out of it based on the section queried.

"""

import configparser
import os

#Intialize the Config Parser.
config = configparser.RawConfigParser()
os.chdir("..\config")

#Load the Config File.
config.read('nmi.config')

#get_config_by_section is intended to read
#a section from the specified config file.
def get_config_by_section(section_name):
    return dict(config.items(section_name))

