# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import databaseProperties
import psycopg2
Host=databaseProperties.Host
User=databaseProperties.User
Password=databaseProperties.Password
Dbname=databaseProperties.Dbname
Port=databaseProperties.Port

try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    print "Connected to specified Postgres database"
except:
    print "I am unable to connect to Postgres database"

try:
    SelectStatement = "SELECT * from " + "Cars"
    cur = conn.cursor()
    cur.execute(SelectStatement)
    rows = cur.fetchall()
except:
    print "Select statement error during data retrieval from Postgres database"


print "\nShow me the some data:\n"
for row in rows:
    print  "id: ",row[0]," name:\t", row[1], "\t\t price:\t", row[2]
