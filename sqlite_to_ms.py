import pymysql as pm 
import sqlite3 as sqli 
import db_tools as dt 

dt.clear_db()
dt.create_table()

ms_db = dt.connection()
ms_cursor = ms_db.cursor()

sqli_db = sqli.connect('database.db')
sqli_cursor = sqli_db.cursor()

# copy data in room table
print('start copy data in room.')
sqli_cursor.execute('SELECT * FROM room;')
data_list = sqli_cursor.fetchall()
# print(data)
for data in data_list:
    query = 'INSERT INTO room (kdno, kcno, ccno, kdname, exptime, papername) VALUES ('
    for content in data:
        query += '"' + content + '", '
    query = query.strip(' ')
    query = query.strip(',')
    query += ');'
    # print(query)
    try:
        ms_cursor.execute(query)
        ms_db.commit()
    except:
        ms_db.rollback()
print('copy done.')

# copy data in student table
print('start copy data in student.')
sqli_cursor.execute('SELECT * FROM student;')
data_list = sqli_cursor.fetchall()
for data in data_list:
    query = 'INSERT INTO student (registno, name, kdno, kcno, ccno, seat) VALUES ('
    for content in data:
        query += '"' + content + '", '
    query = query.strip(' ')
    query = query.strip(',')
    query += ');'
    try:
        ms_cursor.execute(query)
        ms_db.commit()
    except:
        ms_db.rollback()
print('copy done.')

ms_db.close()
sqli_db.close()