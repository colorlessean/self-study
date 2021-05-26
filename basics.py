# https://docs.python.org/3/tutorial/
# https://docs.python.org/3/reference/index.html#reference-index
# https://docs.python.org/3/library/index.html#library-index
# https://www.dataquest.io/blog/learn-python-the-right-way/

import math
import os

# random math stuff

print(2 * (2**3) + 1)
print(round(2.35260, 3))

# in iteractive _ will be the previous result

print("'Hello' said the beetle\n\"Good morning\" said the horse") # stringing with escapes
print(r'C:/Users/Bob/New\ Folder') # raw string i.e. no escapes

print("""\
This is a block of text
    We can actually format things with the triple quotes
""")

# string concatination stuff
string = "Hello" + " " + "World"
print(string)

string = 3 * "to" + "day junior"
print(string)

# array indexing with strings
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
print(string[0])
print(string[-1])
print(string[0:5])
print(string[:5])
print(string[5:])

# length attribute
print(len(string))

# lists
squares = [1, 4, 9, 16, 25, 36]
print(squares)
print(squares[:])

# add to the list
squares += [49, 64, 81, 100, 121]
print(squares)

squares.append(12**2)
print(squares)

print(len(squares))

cubes = []
for num in squares:
    cubes.append(math.sqrt(num)**3)

print(cubes)

a, b = 0, 1
# fibonacci sequence
while a < 10:
    print(a, end=',')
    a, b = b, a + b
print()

for i in range(5):
    print(i)

a = ["A", "B", "C", "D", "E"]
for i in range(0, len(a)):
    print(i, a[i])

class MyEmptyClass:
    pass # passively ignore the implemenation helps in development

def function(*args): 
    pass

# can have default values for functions optional arguments
def parrot(voltage, state="a stiff", action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# default values in functions
i = 5
def f(arg=i):
    print(arg)

i = 6
# not it is only evaluted once so the 6 doesn't affect it
f()

# because it is only evaluated once you can accumulate values in a list
def fu(a, L=[]):
    L.append(a)
    return L

print(fu(1))
print(fu(2))
print(fu(3))

# without any *'s is a formal parameter
# with a single * is a tuple of positional arguments beyond the formal parameters and itself is a formal parameter
# with two ** is a dictionary of all keyword arguments without any formal parameters
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# arguments can be passed positionally or by keyword, so we have special symbols to avoid confusion and limit the possibilities
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only
# if neither / or * are in the decleration then all arguments may be passed by position or by keyword

def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# can use *args to define an arbitrary number of arguments
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

blah = concat("earth","mars","venus")
print(blah)
blah = concat("earth","mars","venus",sep=".")
print(blah)

def parrot_1(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

# can deliver keyword arguments with the ** operator
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot_1(**d)

# can have single line lambda functions
def make_incrementor(n): 
    return lambda x: x + n

f = make_incrementor(42)

print(f(1))
print(f(2))

def my_function():
    """Do nothing

    Absolutely nothing...
    """
    pass

print(my_function.__doc__)

def fun(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", fun.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(fun('spam'))
