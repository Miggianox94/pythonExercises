class MyClass:
  "This is my class"
  a = 10
  def func(self):
    '''
    whenever an object calls its method, the object itself is passed as the first argument.
    So, ob.func() translates into MyClass.func(ob)
    :return:
    '''
    print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function 0x0000000003079bf8="" at="" myclass.func="">
print(MyClass.func)

# Output: 'This is my class'
print(MyClass.__doc__)


# costruttori ----------------------------------------------------------------------
class ComplexNumber:
    def __init__(self,r = 0,i = 0):  # constructor
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))


c1 = ComplexNumber(2,3) # Create a new ComplexNumber object
c1.getData() # Output: 2+3j

c2 = ComplexNumber() # Create a new ComplexNumber object
c2.getData() # Output: 0+0j

#Multiple inheritance e MRO (method resolution) --------------------------------------------------
class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())

#Operator overloading ----------------------------------------------------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

'''
Addition	p1 + p2	p1.__add__(p2)
Subtraction	p1 - p2	p1.__sub__(p2)
Multiplication	p1 * p2	p1.__mul__(p2)
Power	p1 ** p2	p1.__pow__(p2)
Division	p1 / p2	p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2	p1.__and__(p2)
Bitwise OR	p1 | p2	p1.__or__(p2)
Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	~p1	p1.__invert__()


Less than	p1 < p2	p1.__lt__(p2)
Less than or equal to	p1 <= p2	p1.__le__(p2)
Equal to p1 == p2	p1.__eq__(p2)
Not equal to	p1 != p2	p1.__ne__(p2)
Greater than	p1 > p2	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)
'''


# ITERATORS -------------------------------------------------------------------------
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

print(next(my_iter)) # Output: 4
print(next(my_iter)) # Output: 7

# GENERATORS ------------------------------------------------------------------------
'''
Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over 
(one value at a time).
The difference is that, while a return statement terminates a function entirely, yield statement pauses the 
function saving all its states and later continues from there on successive calls.

Utili per memory efficient e per rappresentare stream infiniti
'''
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item)

# equivalente alle lamda ma per generator
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)

# CLOSURES --------------------------------------------------------------------------------
'''
We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.
'''
def print_msg(msg): # outer enclosing function
    def printer():  # inner function
        print(msg)
    return printer  # this got changed

another = print_msg("Hello") # Output: Hello
another()  # è come se la chiamassi con "Hello"


# DECORATORS -------------------------------------------------------------------------------
# ne posso mettere anche più di uno
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

'''
In Python, this magic is done as function(*args, **kwargs). In this way, args will be the tuple of positional 
arguments and kwargs will be the dictionary of keyword arguments.
'''
def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

# PROPERTY-------------------------------------------------------------------------------------------
'''
In Python, property() is a built-in function that creates and returns a property object. 
The signature of this function is property(fget=None, fset=None, fdel=None, doc=None)
'''
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value