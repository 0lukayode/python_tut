# Classes define
# - data Structure 
# - behavior

# for 
# - reusable components
# - group data and operations together 

# parts
# - Classes- nouns 
# - Properties- adjectives
# - Methods- verbs 

class User ():
    def __init__(self, name) -> (str):
        # Consructor
        self.name = name

    def say_hello(self):
        # method
        print('Hello, ' + self.name)

user = User('Jane')
user.name = 'Jane Doe'
user.say_hello()
