import pymysql
pymysql.install_as_MySQLdb()
import csv
import MySQLdb
db = MySQLdb.connect(host='localhost',
    user='sonali',
    passwd='Sheenu**1',
    db='employee')
cursor = db.cursor()
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-file",type=str)
args = parser.parse_args(['-file', 'untitled1.txt'])
with open(args.file) as f:
    reader=f.readlines()
    for row in reader:
        print(row)
with open(args.file) as f:
    for line in f:
        line1=line.split(',')
        cursor.execute("""INSERT INTO employees(id,name,dept,sal)VALUES(%s, %s, %s, %s)""", line1)
db.commit();