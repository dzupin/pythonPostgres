import psycopg2

try:
    conn = psycopg2.connect(dbname='cemdb', user='postgres', host='localhost', password='postgres', port='5432' )
    print "Connected to local database"
except:
    print "I am unable to connect to local Postgres database"

cur = conn.cursor()
cur.execute("SELECT * from mytesttable")

rows = cur.fetchall()
print "\nShow me the some data:\n"
for row in rows:
    print  "id: ",row[0]," first:\t", row[1], " second:\t", row[2], " size:\t", row[3]
