# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
import sys
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='mydatabase'
Port='5432'

cars2 = (
    (1, 'Audi', 25264),
    (2, 'Mercedes', 25712),
    (3, 'Skoda', 2900),
    (4, 'Volvo', 22900),
    (5, 'Bentley', 235000),
    (6, 'Citroen', 22100),
    (7, 'Hummer', 24140),
    (8, 'Volkswagen', 22160)
)

conn = None
try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    print "Connected to following database on Postgres server: " + Dbname
except:
    print "I am unable to connect to Postgres server"

try:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars2")
    cur.execute("CREATE TABLE Cars2(Id INT PRIMARY KEY, Name TEXT, Price INT)")
    query = "INSERT INTO Cars2 (Id, Name, Price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars2)

    conn.commit()
    print "Successfully created new table with sample data"

except psycopg2.DatabaseError, e:
    if conn:
        conn.rollback()
    print 'Error %s' % e
    print "Failed to create table2 in your Postgres database"
    sys.exit(1)

finally:
    if conn:
        conn.close()


conn.close()