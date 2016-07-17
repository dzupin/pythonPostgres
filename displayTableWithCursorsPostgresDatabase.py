# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import databaseProperties
import psycopg2
import psycopg2.extras
import sys
Host=databaseProperties.Host
User=databaseProperties.User
Password=databaseProperties.Password
Dbname=databaseProperties.Dbname
Port=databaseProperties.Port

conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

#################### Display content of first table ######################
print ("\nContent of the first table")
try:
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" % (row["id"], row["name"], row["price"])
except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to retrieve table from Postgres database"


#################### Display content of second table ######################
print ("\nContent of the second table")
try:
    cur.execute("SELECT * FROM Cars2")
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" % (row["id"], row["name"], row["price"])
except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to retrieve table from Postgres database"
    sys.exit(1)
finally:
    if conn:
        conn.close()


conn.close()