    def maximum_difference(a, b, c) : #def stands for define
    """Returns the value with the maximum difference among diff1, diff2 and diff3"""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
#If we don't include the 'return' keyword in a function that requires 'return', then we're going to get a special value 
#called 'Null'

def least_dif(a ,b, c):
    """Docstring - Finds the minimum value with the least difference between numbers"""
    diff1 = a - b
    diff2 = b - c
    diff3 = a - c
    return min(diff1, diff2, diff3)

print(
    least_dif(1, 10, 100),
    least_dif(1, 2, 3),
    least_dif(10, 20, 30)
    )
#help(least_dif)

print(1, 2, 3, sep=" < ") #Seperate values in between printed arguments #By default sep is a single space ' '

#help(maximum_difference)^^^

#Adding optional arguments with default values to custom made functions >>>>>>

def greet(who="Mahdee"):
    print("Hello ", who) 
    print(who)

greet()
greet(who="Mahdee")
greet("world")

#Functions applied on functions



def mult_by_five(x, y):
    return 5 * x + y

def call(fn, *arg):
    """Call fn on arg"""
    return fn(*arg)

print(call(mult_by_five, 1, 1) , "\n\n")

example = call(mult_by_five, 1, 3)
print(example)

def squared_call(fn, a, b, ans):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(a, b), ans)

print(
    call(mult_by_five, 3, 6),
    squared_call(mult_by_five, 1, 1, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

def my_function():
    print("Hello From My Function!")

my_function()

def function_with_args(name, greeting):
    print("Hello, %s, this is an example for function with args, %s" % (name, greeting))

function_with_args("Mahdee", "Good Morning")

def additioner(x, y):
    return x + y

print(additioner(1, 3))

def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to connect and share code together"

def build_sentence(info):
    return "%s , is a benefit of functions" % info

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#Exercise
def to_smash(total_candies, n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends
 
print(to_smash(91))

x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))

def f(x):
    y = abs(x)
    return y

print(f(0.00234))
