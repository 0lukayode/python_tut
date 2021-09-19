first_name = input('Hello \nPlease enter your firstname:')
last_name = input('Please enter your lastname:')
sentence='Welcome '+ first_name+ ' '+ last_name

print()
print('Welcome '+ first_name.capitalize()+ ' '+ last_name.capitalize())
# print('Hello \nwelcome')
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count("e"))

print()
# 
# format variable?
# form = format(first_name, last_name)
# print('Hello, {1}, {0}'.form)
# 
print('Hello, {} {}'.format(first_name, last_name))
print('Hello, {1}, {0}'.format(first_name, last_name))

print(f'Hello, {first_name} {last_name}')