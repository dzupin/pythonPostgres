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

#################### Delete table ######################
print ("\nDelete all rows in table from Postgres database")
try:
    cur.execute("DELETE FROM Cars")
    conn.commit()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()



print ("Successfully deleted all records from table")