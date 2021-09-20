class User ():
    def __init__(self, name) -> (str):
        # Consructor
        self.name = name

    @property
    def name(self):
        print('In the getter')
        return self.__name
        
    @name.setter
    def name(self,value):
        print('In the setter')
        # cool validation here
        self.__name = value


user = User('Jane')
user.name = 'Jane Doe'
print(user.name)

