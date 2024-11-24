# class NameOfClass():

#     def __init__(self,param1,param2):
#         self.param1 = param1
#         self.param2 = param2
    
#     def some_method(self):
#         #perform some action
#         print(self.param1)

class Dog():

    def __init__(self, breed):

        self.breed = breed

my_dog = Dog(breed='Yorkie')
print(type(my_dog))

print(my_dog.breed)