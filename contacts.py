import sqlite3

db = sqlite3.connect("pontacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS pontacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO pontacts(name, phone, email) VALUES('John Doe', 123456789, 'johndoe@example.com')")
db.execute("INSERT INTO pontacts(name, phone, email) VALUES('Tim', 6545678, 'timehai@gman.com')")
db.execute("INSERT INTO pontacts VALUES('Brian', 1234, 'brian@yahoo.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM pontacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)

cursor.close()
db.close()