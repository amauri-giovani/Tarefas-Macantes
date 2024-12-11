import mysql.connector, os
from mysql.connector import Error


class Conndb():
	""" Conectando ao banco de dados """
	def __init__(self):
		try:
		    print('Connecting to MySQL database...')
		    self.conn = mysql.connector.connect(host='localhost',
		                                   database='meteorologia',
		                                   user='root',
		                                   password='%s'%os.getenv('PASSDBMYSQL'))
		    if self.conn.is_connected():
		        print('connection established.')
		        self.cursor = self.conn.cursor()

		except Error as e:
		    print(e)
