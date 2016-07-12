import psycopg2
Host='localhost'
User='postgres'
Password='postgres'
Dbname='cemdb'
Port='5432'

try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    print "Connected to local database"
except:
    print "I am unable to connect to local Postgres database"

cur = conn.cursor()
cur.execute("SELECT * from mytesttable")

rows = cur.fetchall()
print "\nShow me the some data:\n"
for row in rows:
    print  "id: ",row[0]," first:\t", row[1], " second:\t", row[2], " size:\t", row[3]
