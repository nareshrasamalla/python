# -*- coding: utf-8 -*-
"""
This file contains utility functions to interact with 
database.

"""
import config_reader as cr
import mysql.connector
from mysql.connector import Error

#Load the Configurations
db_configurations = cr.get_config_by_section("DB_CONFIG")

# fetch_results_by_query executes a Query against database
# and returns retrived result as JSON List.
def fetch_results_by_query(query):
    host = db_configurations.get("db.host")
    database = db_configurations.get("db.database")
    user = db_configurations.get("db.user")
    pwd  = db_configurations.get("db.password")
    port = db_configurations.get("db.port")
    
    print(" Host Name "+ host + " DB Name " + database + " ID " + user + " PWD " + pwd + " Port " + port)
    print(query)
    records = None
    conn = None
    try:
        conn=mysql.connector.connect(host=host,user=user,password=pwd,database=database,port=port)
        mysql.connector.connect()
        cur=conn.cursor()        
        cur.execute(query)        
        records=cur.fetchall()
        
        row_headers=[x[0] for x in cur.description]
        
        dic_data=[]
        for row in records:
            dic_data.append(dict(zip(row_headers,row)))
            
    except Error as err:
        print("Error while connecting to MySQL !")
        print(err);
    
    finally:
        if conn is not None and conn.is_connected():
            cur.close()
            conn.close()
            print(dic_data)
            print("Connection Closed !")
    
    return dic_data
    


