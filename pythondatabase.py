import pymysql
pymysql.install_as_MySQLdb()
import csv
import MySQLdb

# TODO: Create separate functions to perform different tasks

# TODO: separate function to handle connection creation - can return connection/cursor
db = MySQLdb.connect(host='localhost',
    user='sonali',
    passwd='Sheenu**1',
    db='employee')
cursor = db.cursor()
import argparse

# TODO: Whatif the argument parsing fails, how will you close the connection
# TODO: Instead of hard-coding file. Should've provided the facility to pass the file via commandline 
parser = argparse.ArgumentParser()
parser.add_argument("-file",type=str)
args = parser.parse_args(['-file', 'untitled1.txt'])

# TODO: file reading is performed twice here. Try to read the file just once and pass the rows to use
with open(args.file) as f:
    reader=f.readlines()
    for row in reader:
        print(row)

# TODO: there is a large gap between a resource acquisition(database connection) and its usage
# try to keep resource acquistion and its usage as close as possible
with open(args.file) as f:
    # TODO: Would have been better to create separate function for statement execution. function could have taken(query, args) as parameters
    for line in f:
        line1=line.split(',')
        cursor.execute("""INSERT INTO employees(id,name,dept,sal)VALUES(%s, %s, %s, %s)""", line1)
db.commit()
