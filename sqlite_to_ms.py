import pymysql as pm 
import sqlite3 as sqli 
import db_tools as dt 
import configparser

# dt.clear_db()
# dt.create_table()

ms_db = dt.connection()
ms_cursor = ms_db.cursor()

conf = configparser.ConfigParser()
conf.read('db.conf')
sqli_db = sqli.connect(conf['sqlite_db']['db'])
sqli_cursor = sqli_db.cursor()

# copy data in student table
print('start copy data in student.')
sqli_cursor.execute('PRAGMA table_info ("student");')
header_raw = sqli_cursor.fetchall()
headers = [row[1] for row in header_raw]
query_predix = 'INSERT INTO student ('
for header in headers:
    query_predix += (header + ', ')
query_predix = query_predix.strip(' ')
query_predix = query_predix.strip(',')
query_predix += ') VALUES ('
sqli_cursor.execute('SELECT * FROM student;')
data_list = sqli_cursor.fetchall()
for data in data_list:
    query = query_predix
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

# copy data in room table
print('start copy data in room.')
# read the header of table room and construct a predix of query
sqli_cursor.execute('PRAGMA table_info ("room");')
header_raw = sqli_cursor.fetchall()
headers = [row[1] for row in header_raw]
headers[4] = 'exptime'
query_predix = 'INSERT INTO room ('
for header in headers:
    query_predix += (header + ', ')
query_predix = query_predix.strip(' ')
query_predix = query_predix.strip(',')
query_predix += ') VALUES ('
# read the content in table
sqli_cursor.execute('SELECT * FROM room;')
data_list = sqli_cursor.fetchall()
# print(data)
for data in data_list:
    query = query_predix
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

ms_db.close()
sqli_db.close()