import csv
import pymysql as pm 
import db_tools as dt 

# dt.clear_db()
# dt.create_table()

db = dt.connection()
cursor = db.cursor()

# read data from room.csv and insert into mysql
print('start copy data in room.csv')
csvfile = open('room.csv', encoding='gbk', newline='')
csvreader = csv.reader(csvfile, delimiter=',')
data_list = []
for row in csvreader:
    data_list.append(row)

# store the header of table, to construct sql dynamically
headers = data_list[0]
data_list = data_list[1:]

# construct the predix of sql command
query_predix = 'INSERT INTO room ('
for header in headers:
    query_predix += (header + ', ')
# rid the ', ' at the end of query_predix
query_predix = query_predix.strip(' ')
query_predix = query_predix.strip(',')
query_predix += ') VALUES ('

for data in data_list:
    query = query_predix
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

headers = data_list[0]
data_list = data_list[1:]

query_predix = 'INSERT INTO student ('
for header in headers:
    query_predix += (header + ', ')
query_predix = query_predix.strip(' ')
query_predix = query_predix.strip(',')
query_predix += ') VALUES ('
for data in data_list:
    query = query_predix
    for content in data:
        query += '"' + content + '", '
    query = query.strip(' ')
    query = query.strip(',')
    query += ');'
    # print(query)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()
print('copy done.')