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

    
# plants = {0: "tree", 2: "flower", 3: "lawn", 4: "houseplant"}

# # for i, value in plants.items(): #.items() returns a tuple 
# #     print(f"this is {i}, so value is {value}")

# for i in plants.values():
#     print(i)

# for i in plants.items():
#     print(i)

# for key in plants:
#     print(key)

# for i in plants.values():
#     print(i)

# myhouse = ["shower", "plants", "kid", "friends"]

# for i in myhouse:
#     print(i)



#while loops

# x = 0 
# list = ["1"]

# while x <= 5:
#     if x % 2 == 0:
#         pass
#     if x % 2 != 0:
#         print(f'the current value of x is {x}')

#     x += 1


# mystring = 'Ashley'
# for letter in mystring:
#     if letter == 'e':
#         break
#     print(letter)

#useful operators 

# for num in range(3,10,2): #up to but not including 10
#     print(num)

# print(list(range(0,12,2)))

# index_count = 0

# for letter in 'abcde':
#     print('at index {} the letter is {}'.format(index_count,letter))
#     index_count += 1


# num = 0
# mylist = ['apple', 'banana', 'orange', 'peach']

#'string'.format() --> 
# for fruit in mylist:
#     print('at num {} we get fruit from my list {}'.format(num, fruit))
#     num += 1

#enumerate(list) ==> gives index count for us in form of tuples
# for index, fruit in enumerate(mylist):
#     print(f'{index} = {fruit}')
  
# mylist1 = [1,2,3,4,5]
# mylist2 = ['a', 'b', 'c']

#  #zip ==> [pairs up and maps two lists according to index]
# for item in zip(mylist1,mylist2):
#     print(item)

# list(zip(mylist1, mylist2))
# print(list)

print(2 in [1,2,3])