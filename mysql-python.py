#----------------------
#WORKING WITH MYSQL DATABASE - CRUDE OPERATIONS USING PYTHON.
#----------------------
'''
SOME BASIC DATABASE COMMANDS

show databases;
use <databse-name> ;
create table <table_name> (colum-name-1 interger(5), name varchar(25), address varchar(50) );
DROP TABLE <table_name>;
select name from tbl_students where roll_no= 1;
describe <table_name>   # it will show the structructre of table



Basic Steps for communicating with database
1.	Establish Connection to Database Server
2.	Create Cursor object for sending SQL Statements
3.	Read Result from Cursor object
4.	Close cursor
5.	Close Connection

Establishing connection to database
cn = mysql.connector.connect()
cn = mysql.connector.connect(database=my-db,user="root", password="my-pwd",host="serverip/localhost") # 'cn' is connection object, will be used to coonect and disconect from any particular database.
This method establish connection to database and return connection object. and using this 'cn' connection object we create one Cursor object 'c = cn.cursor()' this cursor object 'c' is used for running
Mysqsl queries on database 'c.execute(Mysql-queries)' and this query response is stored in 'c' as well, 
we can reads the data from cursor object using following methods.

fetchone() : This return one row and return each row as one tuple
fetchmany(n) : This return n rows inside list of tuples
fetchall() : This fetch all rows and return as list of tuples

# EXAMPLE OF READING DATA FROM TABLE  'marks_table'

import mysql.connector as mysql

cn=mysql.connect(database="database5pm",user="root",password="root")
c=cn.cursor() #creating cursor object
c.execute("select * from marks_table") #result of query stored in cursor objeject 'c'
r1=c.fetchone() #fetchone() returns one row at a time as a tuple. 
print(r1)
r2=c.fetchone()
print(r2)
r3=c.fetchone()
print(r3)
r4=c.fetchone()
print(r4)
r5=c.fetchone()
print(r5)
r6=c.fetchone() #if there is no next row to read, will return None
print(r6)
cn.close()

-----------------


'mysql' is one package, 'connector' is module, and connect is one class of this module.

database - name of the database created in mysql
user - database user name
password - database password
host - hostname or ip-address of system where database server running.


Cursor object provide the following methods for sending SQL statements or command
1.	execute()
2.	executeMany()
After executing SQL statements, the result of SQL statement is return inside cursor object.



EXAMPLE OF INSERTING NEW COLUMN IN EXISTING TABLE
c.execute("
    ALTER TABLE tbl_students
    ADD COLUMN sub1 FLOAT(3,2),
    ADD COLUMN sub2 FLOAT(3,2)
")


'''

import mysql.connector
import os
from dotenv import load_dotenv # creates Env variable from provided file, by default reads -> '.env' file for creaing environment variables.


#CONNECTING WITH DATABASE
load_dotenv() # creating environment variables form .env file.
PWD = os.getenv('PASSWORD') #storing value in python variable 'PWD', form OS's Environment varaible 'PASSWORD', this 'PASSWORD' os's envionment vari is created using .env file. 
cn = mysql.connector.connect(database="db_college", user="root", password=PWD, host="localhost")
print(f"connnectd with database 'db_college' ")

# Creating cursor object for sending SQL quesry and command to execute on this database. 
c = cn.cursor() #we are simply saying that use this connection 'cn' and execute my query on that databse

#CREATING TABLE
# The table 'tbl_students' is created if it does not already exist using CREATE TABLE IF NOT EXISTS.
# c.execute("DROP TABLE tbl_students")
c.execute("CREATE TABLE IF NOT EXISTS tbl_students (roll_no integer(5), name varchar(25), addr varchar(50), sub1 float(5,2), sub2 float(5,2), total_marks float(5,2), avg_marks float(5,2) ) ")

print("table created ")


#INSERTING DATA IN TABLE
while True:

    ans = input("Want to add more record? Enter 'no' to Stop? ")
    if ans == 'no':
        break

    roll = input("Enter Student roll no:? ")
    name = input("Enter Student name: ")
    addr = input("Enter student city/state name: ")
    sub1 = float(input("Enter marks of subject 1: "))
    sub2 = float(input("Enter marks of subject 2: "))

    c.execute("INSERT INTO tbl_students (roll_no, name, addr, sub1, sub2) values(%s,%s,%s,%s,%s)", params=(roll, name, addr, sub1, sub2))

    k = c.rowcount
    if k == 1:
        print("1 Student data is saved")
c.close()
cn.commit()
cn.close

# #OUTPUT
# +---------+-------+-----------+-------+-------+-------------+-----------+
# | roll_no | name  | addr      | sub1  | sub2  | total_marks | avg_marks |
# +---------+-------+-----------+-------+-------+-------------+-----------+
# |    1001 | rahul | gaya      | 60.00 | 65.00 |        NULL |      NULL |
# |    1002 | sohan | bangalore |  0.00 | 76.00 |        NULL |      NULL |
# |    1003 | shiva | hyderabad | 90.00 | 98.00 |        NULL |      NULL |
# +---------+-------+-----------+-------+-------+-------------+-----------+


#------------------


# CALCULATE TOTAL AND AVERAGE MARK OF STUDENT (UPDATE)
#CONNECTING WITH DATABASE
load_dotenv() # creating environment variables form .env file.
PWD = os.getenv('PASSWORD')
cn = mysql.connector.connect(database="db_college", user="root", password=PWD, host="localhost")
print(f"connnectd with database 'db_college' ")

c = cn.cursor() 
c.execute("UPDATE tbl_students SET total_marks=sub1+sub2 ")
c.execute("UPDATE tbl_Students SET avg_marks=total_marks/2 ")
print("total and avg marks is updated !")

c.close() # closing cursonr session
cn.commit() # commiting the changes into database permanently
cn.close() # cloasing the conncction 

# #OUTPUT:
# | roll_no | name  | addr      | sub1  | sub2  | total_marks | avg_marks |
# +---------+-------+-----------+-------+-------+-------------+-----------+
# |    1001 | rahul | gaya      | 60.00 | 65.00 |      125.00 |     62.50 |
# |    1002 | sohan | bangalore |  0.00 | 76.00 |       76.00 |     38.00 |
# |    1003 | shiva | hyderabad | 90.00 | 98.00 |      188.00 |     94.00 |
# +---------+-------+-----------+-------+-------+-------------+-----------+


#---------------------
# READING DATA FROM TABLE

# fetchone() : This return one row and return each row as one tuple
# fetchmany(n) : This return n rows inside list of tuples
# fetchall() : This fetch all rows and return as list of tuples

load_dotenv() # creating environment variables form .env file.
PWD = os.getenv('PASSWORD') #loading env variable PASSWORD into pyhon variable PWD
cn = mysql.connector.connect(database="db_college", user="root", password=PWD, host="localhost")
print(f"connnectd with database 'db_college' ")

c = cn.cursor()
c.execute("SELECT * FROM tbl_students")
row1 = c.fetchone() # fetch one row from table 'tbl_students'
print(row1)

list1 = c.fetchmany(2)
print(list1)# fecth two record of two rows, returned as list of tuple having two elements. 

list2 = c.fetchall()
print(list2) # fectch all rows of table and retruned as list of tuple. 

# OUTPUT: IF ALLL ROW IS ALREADY READ, AND ROW REMAINING TO READ, TI WILL RETURN EMPTY LIST
# (1001, 'rahul', 'gaya', 60.0, 65.0, 125.0, 62.5)
# [(1002, 'sohan', 'bangalore', 0.0, 76.0, 76.0, 38.0), (1003, 'shiva', 'hyderabad', 90.0, 98.0, 188.0, 94.0)]
# []

#------------------------

#READING DATA FROM TABLE AND DETERMINIG PASS AND FAIL
c.execute("SELECT * FROM tbl_students")
slist = c.fetchall()
for sroll, sname, saddr, ssub1, ssub2, stotal_marks, savg_marks in slist:
    result = "Pass" if ssub1>=30 and ssub2>=30 else "Fail"
    print(f'{sroll}\t{sname}\t{ssub1:.2f}\t{ssub2:.2f}\t{stotal_marks:.2f}\t{savg_marks:.2f}\t{result}')

cn.close()

# #OUTPUT
# 1001    rahul   60.00   65.00   125.00  62.50   Pass
# 1002    sohan   0.00    76.00   76.00   38.00   Fail
# 1003    shiva   90.00   98.00   188.00  94.00   Pass


#--------------
#DELETE ANY STUDENT FROM DATABASE USING ROLL NO.
load_dotenv() # creating environment variables form .env file.
PWD = os.getenv('PASSWORD') #loading env variable PASSWORD into pyhon variable PWD
cn = mysql.connector.connect(database="db_college", user="root", password=PWD, host="localhost")
print(f"connnectd with database 'db_college' ")

c = cn.cursor()

rollno = input("Enter any roll no of student, whose data will be deleted:?: ")
c.execute("DELETE FROM tbl_students where roll_no=%s", params=(rollno,))
a = c.rowcount
if a == 1:
    print(f"Roll NO: {rollno}, Student is deleted ")
else:
    print(f"invalid rollno")


cn.commit() # saves all the changes permaently into databse what ever we do on python script
cn.close()


#----------------------