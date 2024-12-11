import psycopg2


print('Connecting to PostgreSQL database...')
con = psycopg2.connect(host='localhost',
                               database='banco',
                               user='amaurirg',
                               password='arg3110')

cur = con.cursor()
cur.execute("select * from tabela")
recset = cur.fetchall()
for rec in recset:
	print(rec)
# cur.execute("insert into tabela values('3','greSQL')")
# con.commit()
con.close()
print("Connection closed.")