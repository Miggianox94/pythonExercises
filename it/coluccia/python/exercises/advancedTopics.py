#  FUNCTIONS --------------------------------------------------------------------
def add_numbers(a, b):
  sum = a + b
  return sum

result = add_numbers(4, 5)
print(result)


# LAMBDA ------------------------------------------------------------------------
square = lambda x: x ** 2
print(square(5))

#MAP FUNCTIONS
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

#FILTER FUNCTIONS
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

# MODULES
import math

result = math.log2(5) # return the base-2 logarithm
print(result) # Output: 2.321928094887362

from math import pi
print("The value of pi is", pi)

'''
A directory must contain a file named __init__.py in order for Python to consider it as a package. 
This file can be left empty but we generally place the initialization code for that package in this file.
'''


# I/O Operations
f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f = open("test.txt",'r',encoding = 'utf-8')
f.read(4)


import os
os.getcwd()  // present working directory
os.chdir('D:\\Hello') // Changing current directory to D:\Hello
os.listdir()  // list all sub directories and files in that path
os.mkdir('test') // making a new directory test
os.rename('test','tasty') // renaming the directory test to tasty
os.remove('old.txt')  // deleting old.txt file

# EXCEPTIONS -------------------------------------------------------------------
class CustomError(Exception):
    print("Custom fucking error")

try:
    raise MemoryError("This is an argument")
except ValueError as ve:
   # handle ValueError exception
   pass
except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass
except:
    raise CustomError
finally:
   print("Finally block motherfucker")


#GLOBAL E LOCAL VARIABLE ----------------------------------------------------------
x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)

'''
The basic rules for global keyword in Python are:

When we create a variable inside a function, it’s local by default.
When we define a variable outside of a function, it’s global by default. You don’t have to use global keyword.
We use global keyword to read and write a global variable inside a function.
Use of global keyword outside a function has no effect
'''



# ACCESSO DB MySql -------------------------------------------------------------------------------------
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()


#MULTITHREADING --------------------------------------------------------------------------------------
import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")