#!/usr/bin/env python3

#This python script connects with the database and fills it with dummy values.

import sqlite3
from datetime import datetime #for timestamp
import random #for dummy values
import time #for dummy values 


DB_path = "test.db"
table = """power"""

def insertData(database, table, data):
    try:
        #open connection to DB
        sqliteConnection = sqlite3.connect(database)
        
        #create cursor ( acts as a pointer to a specific location in the result set, and used to fetch or manipulate data)
        cursor = sqliteConnection.cursor()

        print("Connected to SQLite")
        
        #insert values
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sqlite_insert_query = """INSERT INTO """ + table + """(timestamp, WT_gen, power_usage) VALUES (?, ?, ?);"""
        cursor.executemany(sqlite_insert_query, [(current_time, data[0], data[1])])
        sqliteConnection.commit() #commits local changes 
        print("Total", cursor.rowcount, "data inserted successfully into power table")
        
        #close cursor to free up memory
        cursor.close()

    #Error Handling
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    #close connection to DB
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


#create dummy Data


for i in range (24):
    new_values = (random.randint(0,10),random.randint(0,10))
    insertData(DB_path,table, new_values)
    time.sleep(2)




