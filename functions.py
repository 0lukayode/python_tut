# functions 
#
from datetime import datetime 

# Print the current time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

op_first_name = 'Kayode'
print_time('Starting Task... Operator: '+ op_first_name)

for x in range(0,10):
    print(x)
print_time('Task Completed')

# fuction that returns a value 
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial + last_name_initial)

# clever code 
ben_first_name = input('Enter your Beneficiary first name: ')

ben_last_name = input('Enter your Beneficiary last name: ')
print('Beneficiary initials are: ' + get_initial(ben_first_name) + get_initial(ben_last_name) )

# parameterized functions
# positional notation & named notation

# positional notation parameter as to  be passed in the order they were declared in the function
def get_first_letter(word, force_upppercase): 
    #To set a parameter to defalut 
    # def get_first_letter(word, force_upppercase=true): 
    # 'force_upppercase=true' sets force_upppercase to a default of true
    if force_upppercase: #if force_uppercase is true
        first_letter = word[0:1].upper()
    else:
        first_letter = word[0:1]
    return first_letter

word_entered = input('enter your a word: ')
word_entered_first_letter = get_first_letter(word_entered, False)
print('First letter of word enter is :'+ word_entered_first_letter)


# named notation the parameter can be passed in any order and makes the codemore readable
# but have to be declared this: parameter_name = parameter_value whem calling the fuction
def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: '+ error_message)
    # Imagine code here that logs our error to a database or file

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger( log_to_db=True, error_message='second number greater than first',error_code= 45, error_severity= 1, source_module= 'my_math_method')