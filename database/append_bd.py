import psycopg2 as psc
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    connection = psc.connect(user='postgres', password='Mamont263_', host='127.0.0.1', port='5432')
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    sql_create_database = 'create database fishing_an_db'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print('error while working with db', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('connection is closed')
