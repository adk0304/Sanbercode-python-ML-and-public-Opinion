
from mysql.connector import connect
db = connect(
    host = "localhost",
    user = "root",
    password = "Lolipop123@"
)

cursor_db = db.cursor() 
cursor_db.execute("CREATE DATABASE if not exists school")
cursor_db.execute("SHOW DATABASES")
db.close()

