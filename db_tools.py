import pymysql as pm 
import configparser

# build connection to mysql localhost root database and return the db connection
def connection():
    print('config file loading...')
    conf = configparser.ConfigParser()
    conf.read('db.conf')
    ms_user = conf['mysql_db']['user']
    ms_passw = conf['mysql_db']['password']
    ms_host = conf['mysql_db']['host']
    ms_db = conf['mysql_db']['db']
    print('config file loaded')

    return pm.connect(ms_host, ms_user, ms_passw, ms_db)

def clear_db():
    db = connection()
    cursor = db.cursor()
    sql_file = open('clear_db.sql', 'r')
    for line in sql_file:
        cursor.execute(line.strip())
    db.close()
    print('database lab1 clear done.')

def create_table():
    db = connection()
    cursor = db.cursor()
    sql_file = open('create_table.sql', 'r')
    for line in sql_file:
        cursor.execute(line.strip())
    db.close()
    print('database lab1 tables created.')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('please enter one arg, create or clear.')
        exit()
    arg = sys.argv[1]
    if arg == 'clear':
        clear_db()
    elif arg == 'create':
        create_table()
    else:
        print('please enter correct arg, create or clear.')