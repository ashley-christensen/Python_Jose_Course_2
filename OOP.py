# class NameOfClass():

#     def __init__(self,param1,param2):
#         self.param1 = param1
#         self.param2 = param2
    
#     def some_method(self):
#         #perform some action
#         print(self.param1)

# class Dog():

#     #Class Object Attribute
#     #Same for any Instance of Class
#     species = 'mammal'

#     def __init__(self, breed, name): 

#         #Assign using self.attribute_name
#         self.breed = breed
#         self.name = name

#         # Methods
#     def bark(self, number):
#             print("WOOF! My name is {} and the number is {}".format(self.name, number))

# my_dog = Dog(breed='Yorkie', name="Anna")
# print(type(my_dog))

# print(my_dog.name)
# my_dog.bark(36)

# class Cat(): 
#     species = 'mammal'

#     def __init__(self, breed, name, stripes):
#         self.breed = breed
#         self.name = name

#         self.stripes = stripes

# my_cat = Cat(breed= 'orange', name="Louie", stripes=True)
# print(type(my_cat))
# print(my_cat.name)

class Circle():
     
    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
         
         self.radius = radius
         self.area = radius*radius*self.pi

    # Method
    def get_circumference(self):
         return self.radius * self.pi * 2
    
my_circle = Circle()

print(my_circle.get_circumference())
print(my_circle.area)