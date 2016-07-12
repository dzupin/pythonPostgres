import psycopg2
Host='192.168.86.188'
User='postgres'
Password='postgres'
Dbname='cemdb'
Port='5432'
Table='mytesttable'

try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    print "Connected to specified Postgres database"
except:
    print "I am unable to connect to Postgres database"

try:
    SelectStatement = "SELECT * from " + Table
    cur = conn.cursor()
    cur.execute(SelectStatement)
    rows = cur.fetchall()
except:
    print "Select statement error during data retrieval from Postgres database"


print "\nShow me the some data:\n"
for row in rows:
    print  "id: ",row[0]," first:\t", row[1], " second:\t", row[2], " size:\t", row[3]
