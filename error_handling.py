# Syntax Error
# This code won't run at all
# x = 42
# y = 206
# if x == y
#     print('Success!!')

# correction
x = 5
y = 9 
if x == y:
    print('Successful!')
else :
    print('Successful!')

# Runtime Errors
# This coode fail when run
i = 42
k = 0
#   print(i/k)
# correction (dividing by error)

try:
    print(i/k)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, not allowed to  divide bby zero')
else:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')

# Logic errors
# This code  would run but give a wrong output 
m = 206
n = 42
if m > n:
    print(str(x)+' is grater than ' +str(y))