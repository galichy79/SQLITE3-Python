import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute ("""CREATE TABLE IF NOT EXISTS users (

	login TEXT,
	password TEXT,
	cash BIGINT



)""")

db.commit()

user_login = input('Login:  ')
user_password = input('Password:  ')

sql.execute("SELECT login FROM users")
if sql.fetchone() is None:
	sql.execute(f"INSERT INTO users VALUES (?,?,?)", (user_login, user_password, 0))
	db.commit()
	
	print('Zagreegistrirovano')

else: 
	print('This is is')
	
	for value in sql.execute("SELECT * FROM users"):
		print(value)