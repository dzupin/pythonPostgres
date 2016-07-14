# -*- coding: utf-8 -*-
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
print ("\nContent of the first table")
try:
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print row
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
        print row
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