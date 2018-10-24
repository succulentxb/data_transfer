import pymysql as pm 
import sqlite3 as sqli 
import configparser

print('config file loading...')
conf = configparser.ConfigParser()
conf.read('db.conf')
ms_user = conf['mysql_db']['user']
ms_passw = conf['mysql_db']['password']
ms_host = conf['mysql_db']['host']
ms_db = conf['mysql_db']['db']
sqli_db = conf['sqlite_db']['db']
print('config file loaded')

ms_db = pm.connect(ms_host, ms_user, ms_passw, ms_db)
ms_cursor = ms_db.cursor()

