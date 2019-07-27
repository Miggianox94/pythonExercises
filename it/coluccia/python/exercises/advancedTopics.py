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