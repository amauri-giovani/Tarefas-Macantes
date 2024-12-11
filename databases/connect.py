import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        print('Connecting to MySQL database...')
        conn = mysql.connector.connect(host='localhost',
                                       database='cadastro',
                                       user='root',
                                       password='arg47910113AM')
        if conn.is_connected():
            print('connection established.')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
        print('Connection closed.')
 
if __name__ == '__main__':
    connect()