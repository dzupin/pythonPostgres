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
def readImage():
    try:
        fin = open("hummer.jpg", "rb")
        img = fin.read()
        print ("Sample image is accessible and ready to be used")
        return img

    except IOError, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if fin:
            fin.close()

conn = None
# Initialize connection to Postgress database
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    cur = conn.cursor()
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

# Create new table in database
try:
    cur.execute("DROP TABLE IF EXISTS Images")
    cur.execute("CREATE TABLE Images(Id INT PRIMARY KEY, Data BYTEA)")
    conn.commit()
    print "Successfully created new table for storing images"

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to create for image storing in your Postgres database"
    sys.exit(1)

# Insert image to your newly created/recreate table
try:
    data = readImage()
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO Images(Id, Data) VALUES (1, %s)", (binary,))

    conn.commit()
    print "Successfully inserted image into new table"

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to insert image into your Postgres database"
    sys.exit(1)


finally:
    if conn:
        conn.close()


conn.close()