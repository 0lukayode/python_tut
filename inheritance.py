# inheritance -specialization/generalization
# Creates an "is a" relationship
#   - Student is a Person
#   - SqlConnection is a DatabaseConnection
#   - MySqlconnection is a DatabaseConnection

# Composition (with propeties) createa has "has a" relationship
#   - Student has a class 
#   - DatabaseConnection has a ConnectionString

class Person:
    def __init__(self,name):
        self.name = name
    def say_hello(self):
        print('Hello, '+ self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to '+ self.school)
    def say_hello(self):
        # let  parent class do some work
        super().say_hello() #adding 'super' tells it to call the parent class
        # add a custom code 
        print('rest a bit')
    # overrides the __str__ method
    def __str__(self) -> str:
        return f'{self.name} attends {self.school}'


student = Student('Charles', 'ZTH')
student.say_hello()
student.sing_school_song()
print(student)
print()

# What are you?
print(f'Is this a student? {isinstance(student,Student)}')
print(f'Is this a Person? {isinstance(student,Person)}')
print(f'Is Student a Person? {issubclass(Student,Person)}')

 
