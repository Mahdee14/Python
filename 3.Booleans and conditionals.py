def validity(age):
    #Checks whether a person can marry
    return age >= 18

print("Can a 15 year old marry ? ", validity(15))
print("Can a 20 year old marry ? ", validity(20), "\n\n")

def is_odd(num):
    #Checks whether a num is odd
    return (num % 2) == 1

print("Is 100 odd ? ", is_odd(100))
print("Is -1 odd ? ", is_odd(-1), "\n")

def is_even(num):
    #Checks whether a num is even
    return (num % 2) == 0

print("Is 100 even ? ", is_even(100))
print("Is -1 even ? ", is_even(-1), "\n")

x = False #Type of variable called bool. Either True/False
print("%d is a %s" % (x,type(x)), "\n") #Outputs 0...

print(bool(234327)) #All numbers are True except 0
print(bool(0), "\n")

print(bool("Mahdee")) #All strings are True except for empty ones
print(bool(""), "\n")

print(bool("0"))#All floats are True except for empty values
print(bool(""), "\n")

bool1 = bool(1) or bool(0) and bool(0) or bool(0) and bool(0)
print(bool1)
print(type(bool1), "\n")

def exactly_one_topping(k, m, o):
    total = k + m + o
    return True if total == 1 else False

print(
    exactly_one_topping(0,0,0),
    exactly_one_topping(0,0,1),
    exactly_one_topping(0,1,1),
    exactly_one_topping(1,1,1),
    "\n"
)

if 0:
    print(0)
elif "spam":
    print("spam", "\n")

def sign(x):
    if x > 0:
        print("1")
    elif x < 0:
        print("-1")
    else: 
        print("0")
    return 0

sign(-1)

total_candies = 5
print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

