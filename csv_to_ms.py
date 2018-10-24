import csv
import pymysql as pm 
import db_tools as dt 

#dt.clear_db()
#dt.create_table()

db = dt.connection()
cursor = db.cursor()

# read data from room.csv and insert into mysql
print('start copy data in room.csv')
csvfile = open('room.csv', encoding='gbk', newline='')
csvreader = csv.reader(csvfile, delimiter=',')
data_list = []
for row in csvreader:
    data_list.append(row)
# delete the first header row
data_list = data_list[1:]
# print(data_list)
for data in data_list:
    query = 'INSERT INTO room (kdno, kcno, ccno, kdname, exptime, papername) VALUES ('
    for content in data:
        query += '"' + content + '", '
    query = query.strip(' ')
    query = query.strip(',')
    query += ');'
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()
print('copy done.')

# read data from student.csv and insert into mysql
print('start copy data in student.csv')
csvfile = open('student.csv', encoding='utf8', newline='')
csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
data_list = []
for row in csvreader:
    data_list.append(row)
data_list = data_list[1:]
for data in data_list:
    query = 'INSERT INTO student (registno, name, kdno, kcno, ccno, seat) VALUES ('
    for content in data:
        query += '"' + content + '", '
    query = query.strip(' ')
    query = query.strip(',')
    query += ');'
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()
print('copy done.')