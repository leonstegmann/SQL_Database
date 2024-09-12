#!/usr/bin/env python3

#This python script creates a Database

import sqlite3
from datetime import datetime #for timestamp

database = 'test.db'

def createDB(DB_name):
	conn = sqlite3.connect(DB_name) #if the database file doesn't exist, it will be created

	cursor = conn.cursor() #Create a cursor object

	#USE SQL command to create table with different columns and datatypes
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS power (
			timestamp DATETIME PRIMARY KEY,
			WT_gen FLOAT,
			power_usage FLOAT
		)
	''')

	#commit changes
	conn.commit() 
	cursor.close()
	conn.close()

createDB(database)

