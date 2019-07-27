# Hello world----------------------------------------------------------------------
print("Hello, World!")

# Costant - there isn't a keyword constant----------------------------------------------------------------------
IAMCONSTANT = "ciao merde"
print(IAMCONSTANT)
IAMCONSTANT = "non posso farlo ma python me lo fa fare"
print(IAMCONSTANT)
# but I can use a class with only getter


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)


class _Const(object):
    @constant
    def FOO():
        return 0xBAADFACE

    @constant
    def BAR():
        return 0xDEADBEEF


CONST = _Const()

print(CONST.FOO)
# #3131964110
# se faccio questo mi spacco
# CONST.FOO = 0

# LIST,DICT,SET----------------------------------------------------------------------
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple --> not editable list
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

# Equivalent java NULL----------------------------------------------------------------------
food = None

# Left operand raised to the power of right (x^y) ----------------------------------------------------------------------
x = 14
y = 4
print('x ** y =', x**y)

# Input utente ----------------------------------------------------------------------
inputString = input('Enter a sentence:')
print('The inputted string is:', inputString)

# Explicit cast  ----------------------------------------------------------------------
num_int = 123  # int type
num_str = "456" # str type

# explicitly converted to int type
num_str = int(num_str)

print(num_int+num_str)

# STRING creation ----------------------------------------------------------------------
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

# slicing 2nd to 5th character
print('str[1:5] = ', my_string[1:5])

str1 = 'Hello '
str2 ='World!'

# Output: Hello World!
print(str1 + str2)

# Hello Hello Hello
print(str1 * 3)

# SETS ---------------------------------------------------------------------------
# set of integers
my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set) # Output: {1, 2, 3, 4}

my_set.update([3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set) # Output: {1, 2, 3, 5}

A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B)
# Also equivalent to B.union(A)
print(A | B) # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print (A & B) # Output: {2, 3}

# Set Difference
print (A - B) # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}

# DICTS -------------------------------------------
person = {'name': 'Jack', 'age': 26}

# Changing age to 36
print(person) # Output: {'name': 'Jack', 'age': 36}

# Adding salary key, value pair
person['salary'] = 4342.4
print(person)  # Output: {'name': 'Jack', 'age': 36, 'salary': 4342.4}


# Deleting age
del person['age']
print(person)  # Output: {'name': 'Jack', 'salary': 4342.4}

# Deleting entire dictionary
del person


# RANGE() ---------------------------------------------
numbers = range(1, 6)

print(list(numbers)) # Output: [1, 2, 3, 4, 5]
print(tuple(numbers)) # Output: (1, 2, 3, 4, 5)
print(set(numbers)) # Output: {1, 2, 3, 4, 5}

# Output: {1: 99, 2: 99, 3: 99, 4: 99, 5: 99}
print(dict.fromkeys(numbers, 99))

# IF ELSE ------------------------------------------
num = -1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#LOOP ------------------------------------------
n = 100

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

numbers = [6, 5, 3, 8, 4, 2]

sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val
    if sum > 10:
        break
    if sum > 9:
        print("Greater than 9")

print("The sum is", sum) # Output: The sum is 28

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass  #si usa quando una roba non è stata ancora implementata