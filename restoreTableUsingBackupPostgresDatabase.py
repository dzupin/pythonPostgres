# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import databaseProperties
import psycopg2
import sys
Host=databaseProperties.Host
User=databaseProperties.User
Password=databaseProperties.Password
Dbname=databaseProperties.Dbname
Port=databaseProperties.Port

f = None
conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

#################### Display content of first table ######################
print ("\nRead local file (that contains table backup and use it to restore table on Postgres server")
try:
    f = open('cars_database', 'r')
    cur.copy_from(f, 'cars', sep="|")
    conn.commit()

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

except IOError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if conn:
        conn.close()
    if f:
        f.close()


print ("Successfully used local file to insert new rows to remote database table")