# loops 
# we have 2 loops in python: 
# -for loops
# -while loops

# collection of names
names = ['Ayo', 'Ola']

# for loops
# loop through a collection
for name in names:
    print(name)

# looping a number of times
for index in range(0,4): #in range first parameter is start point '0' and second parameter is number of items '2'
    print(index)



# while loops
# looping with a condition

index = 0
while index < len(names):
    print(names[index])
    # change the condition
    index = index + 1