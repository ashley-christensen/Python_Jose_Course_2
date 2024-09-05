#ctrl + shift + / === run
# if 1 > 3:
#     print('hello')
# elif 2 == 2:
#     print('hello-bye')
# else:
# #     print('bye')

# hungry = True
# if hungry: 
#     print("three is greater than two ")
# else:
#     print("two is greater than three")
    

# loc = 'Orlando'
# if loc == 'Auto Shop':
#     print("cars are cool!")
# elif loc == 'Bank':
#     print("money is cool")
# elif loc == "Orlando":
#     print("Florida is so amazing!!")
# else: 
#     print("I do not know much")


# for item in fruits:
#     print(item)

# for i in name:
#     print(i)

# for fruit in fruits:
#     print(fruit)

# for thekey in plants:
#     print(plants[thekey])

# for fruit in fruits:

#     if fruit[0] == 'm':
#         print(fruit)

# mylist = [1,2,3,4,5,6,7,8,9,10]
# name = "Ashley"
# fruits = ["apple", "banana", "orange", "mango", "avocado", "coconut", "pineapple"]
# plants = {0: "tree", 2: "flower", 3: "lawn", 4: "houseplant"}
# for key in plants:

#     if key % 2 == 0:
#         print(f'even number: {key} = {plants[key]}')
#     else:
#         print(f"odd number: {key}")

# list_sum = 0

# for num in mylist:
#     list_sum = list_sum + num
#     print(list_sum) #inside for loop

#     if num == mylist[-1]:
#         print(f'the end because number is: {mylist[-1]}')

# print(f"LIST SUM: {list_sum} ") #outside for loop


# mystring = "Hello World"
# for letter in mystring:
#     print(letter)


# mylist = [(1,2,3), (3,4,5), (5,6,7), (7,8,9)]
# # print(len(mylist))

# for a,b,c in mylist: #tuple unpacking
#     print(a)

    
plants = {0: "tree", 2: "flower", 3: "lawn", 4: "houseplant"}

# for i, value in plants.items(): #.items() returns a tuple 
#     print(f"this is {i}, so value is {value}")

for i in plants.values():
    print(i)

# for i in plants.items():
#     print(i)

# for key in plants:
#     print(key)

for i in plants.values():
    print(i)