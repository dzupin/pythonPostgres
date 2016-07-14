# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
import sys
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='mydatabase'
Port='5432'

fout = None
conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

#################### Display content of first table ######################
print ("\nMake backup of Postgres database and store it to file")
try:
    fout = open('cars_database', 'w')
    cur.copy_to(fout, 'cars', sep="|")

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

except IOError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
    if fout:
        fout.close()


print ("Successfully created database backup file")