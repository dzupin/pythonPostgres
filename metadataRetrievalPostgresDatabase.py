# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
import sys
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='mydatabase'
Port='5432'

conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

#################### Display content of first table ######################
print ("\nMetadata example: get names of columns in Postgres table")
try:
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    for row in rows:
        print "%2s %-10s %s" % row

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()