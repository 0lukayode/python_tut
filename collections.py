# Collection

# arrays 
# arrays  are collection of items
from array import array 
print('...... Arrays .....')
marks = array('d') #specify data type "double"
marks.append(95)
marks.append(90)
print(marks)
print(marks[1])
print()



# Lists
# Lists are collection of items
# can hold multiple data types

# common Operations
print('...... Lists .....')

names = ['Susan','Christopher']
scores = []
scores.append(98) #add new item to the end 
scores.append(98)
print(scores)
print(names)
print(scores[1])
print(len(names)) #get the number of items
names.insert(0, 'Bill')#Insert before index
print(names)
names.sort() #modifies list arranges from small to big 9(first to last)
print(names)
print()

# Retriving ranges
names = ['susan','Christopher', 'bill', 'Justin']
presenters = names[1:3] #takes value between 1 to 3 ","
 #start and end index

print(names)
print(presenters)
print()


# Dictionaries
print('...... Dictionaries .....')

person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])
