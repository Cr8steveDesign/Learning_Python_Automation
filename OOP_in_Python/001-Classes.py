# Learning About Classes in Python

class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def get_details(self):
        return [self.name, self.age, self.profession]

    def set_details(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
    

# Creating Instance of the class

stephen = Person("Stephen Omoregie", age=55, profession="Software Engineer")
tracy = Person("Tracy Okogun", age=35, profession="Educational Consultant")

# Accessing members of the instance
print(isinstance(stephen, Person))

print(tracy.profession)

# Using method to set member
tracy.set_details(age=tracy.age, name=tracy.name, profession="International Consultant")
print(tracy.profession)


