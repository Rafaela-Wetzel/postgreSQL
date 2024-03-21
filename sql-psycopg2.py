import psycopg2

connection = psycopg2.connect(database="chinook")
cursor = connection.cursor()
cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Judas Priest"])
results = cursor.fetchall()
connection.close()

for result in results:
    print(result)