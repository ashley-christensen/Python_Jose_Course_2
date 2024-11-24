# class NameOfClass():

#     def __init__(self,param1,param2):
#         self.param1 = param1
#         self.param2 = param2
    
#     def some_method(self):
#         #perform some action
#         print(self.param1)

class Dog():

    #Class Object Attribute
    #Same for any Instance of Class
    species = 'mammal'

    def __init__(self, breed, name, spots): 

        #Assign using self.attribute_name
        self.breed = breed
        self.name = name

        #Excpect boolean True/False
        self.spots = spots

my_dog = Dog(breed='Yorkie', name="Anna", spots=False)
print(type(my_dog))

print(my_dog.species)
