# Nested list
list_example = [
    [1, 2, 3],
    ['2', 'K', '2', '1'],
    ["hi", "hello", "Mahdee"]
]
print(list_example)
print(list_example[2], "\n")

#List indexing (0 based indexing - starts from 0)
subjects = ["ICT", "Maths", "Eng.lit", "Islam", "Science", "English", "BS", "Tamil", "History"]
print(subjects[0])
print(subjects[-1], "\n") # Prints from backwards

#Slicing
print(subjects[0:3]) #Prints first 3 subjects starting from 0 , but not 3
print(subjects[:3]) #Assumes first index is 0
print(subjects[0:]) #Assumed to be the length of the list
print(subjects[1:-1]) #All items except for first and last
print(subjects[-3:]) #Last 3 subjects
print(subjects[:-3], "\n") #Excluding last 3 subjects

#Changing lists - Lists are mutable meaning modifiable unlike tuple
subjects[0] = "I"
subjects[1] = "M"
subjects[2] = "E"
print(subjects[0], subjects[1], subjects[2], "\n")

subjects[-3:] = "B", "T", "H" #Shortening the names of the first 3 subjects
print(subjects, "\n")

#List functions
print(
    len(list_example),
    len(subjects),
    "\n"
)

print( #Sorted sorts the list in alphabetical or numerical order
    sorted(list_example[0]),
    sorted(list_example[1]),
    sorted(subjects),
    "\n"
)

print(sum(list_example[0]), "\n") #Sums everything up

print( #min shows the min value of the list and max shows the max value of the list
    min(list_example[0]),
    max(list_example[0]),
    "\n"
) 

#Interluding objects in python -  objects carry some things around with them
#Non-function things like .imag attached to objects are called attributes
x = 12 #x is a real number, so it's imaginary part is 0
print(x.imag)

c = 12 + 3j #How to make an imaginary number
print(c.imag)

#Thing an object carries can also include functions - It's called methods
print(x.bit_length)

#help(x.bit_length)

#List methods

#.append adds an item to the end
subjects.append("Mahdee")
print(subjects)

