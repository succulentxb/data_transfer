import pymysql as pm 
import sqlite3 as sqli 
import db_tools as dt 


ms_db = dt.connection()
ms_cursor = ms_db.cursor()

sqli_db = sqli.connect('database.db')
sqli_cursor = sqli_db.cursor()

# copy data in table room
sqli_cursor.execute('select * from room;')
data_list = sqli_cursor.fetchall()
# print(data)
for data in data_list:
    query = 'INSERT INTO room ('