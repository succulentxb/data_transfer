import pymysql as pm 
import configparser

print('config file loading...')
conf = configparser.ConfigParser()
conf.read('db.conf')
ms_user = conf['mysql_db']['user']
ms_passw = conf['mysql_db']['password']
ms_host = conf['mysql_db']['host']
ms_db = conf['mysql_db']['db']
print('config file loaded')

db = pm.connect(ms_host, ms_user, ms_passw, ms_db)
cursor = db.cursor()
cursor.execute('CREATE TABLE room(kdno TEXT, kcno TEXT, ccno TEXT, kdname TEXT, exptime TEXT, papername TEXT);')
db.close()