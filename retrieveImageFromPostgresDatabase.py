# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
import sys
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='mydatabase'
Port='5432'

#Get image sample file from your computer
def writeImage(data):
    try:
        fout = open("hummer2.jpg", "wb")
        fout.write(data)

    except IOError, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if fout:
            fout.close()


conn = None
# Initialize connection to Postgress database
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"


# Insert image to your newly created/recreate table
try:
    cur.execute("SELECT Data FROM Images LIMIT 1")
    data = cur.fetchone()[0]

    writeImage(data)
    print "Successfully got image from Postgres database"

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to retrieve image from your Postgres database"
    sys.exit(1)


finally:
    if conn:
        conn.close()


conn.close()