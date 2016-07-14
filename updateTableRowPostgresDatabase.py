# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
import sys
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='mydatabase'
Port='5432'


uId = 1
uPrice = 88888
conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

#################### Update line in first table ######################
print ("\nContent of the first table")
try:
    cur.execute("UPDATE Cars SET Price=%s WHERE Id=%s", (uPrice, uId))
    conn.commit()
    print "Number of rows updated: %d" % cur.rowcount

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to update line in table of Postgres database"
    sys.exit(1)

finally:
    if conn:
        conn.close()

