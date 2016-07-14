# -*- coding: utf-8 -*-
# reference link: http://zetcode.com/db/postgresqlpythontutorial/

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
Host='192.168.86.189'
User='postgres'
Password='postgres'
Dbname='postgres'  #Use default installation database for initial connection
DbnameNew='mydatabase'
Port='5432'

try:
    conn = psycopg2.connect(dbname=Dbname, user=User, host=Host, password=Password, port=Port )
    print "Connected to default database of Postgres server"
except:
    print "I am unable to connect to Postgres server"


try:
    CreateStatement = "CREATE DATABASE " + DbnameNew
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) #to create database you must overwrite default (ISOLATION_LEVEL_READ_COMMITTED) isolation level
    cur = conn.cursor()
    cur.execute(CreateStatement)
    print "Successfully created new database: " + DbnameNew
except:
    print "Failed to create new Postgres database"


cur.close()
conn.close()