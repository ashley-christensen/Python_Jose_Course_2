# name = "sam"
# S = name[0]
# # print(name[0])
# # print(name)
# last_letters = name[1:]
# # print(name + last_letters + (last_letters*3))
# # last_letters * 3
# # S*3
# 's'*3

# x = "Hello World"
# x.upper()

import math
# print(x.upper())
# print(x.lower())
# print(x.split())

# x = 'hi this is a string'
# print(x.split())

# print('This is a string {}'.format('WHICH IS INSIDE MY CODE NOW'))
# # print('The {2} {1} {0}'. format('ashley', 'baby', 'Will'))
# print('The {q} {b} {f}'.format(f='fox', b="brown", q='quick'))

# result = 100/777
# print(result)
# print('the result was.. {r:1.2}'.format(r = result))

# name = 'Ashley'
# age = 35

# print(f'Hello, her name is {name} and she is {age} years old ')

# my_list = [1, 2, 3]
# print(my_list)
# new_list = ['a', 'hello', 16]
# print(my_list)
# len(my_list)
# my_list[1:]
# print(my_list[1:])
# print(my_list + new_list)

# new_list = ['hello', 'whats up']


# popped_item = new_list.pop()
# # print(popped_item)
# print(new_list.pop(-1))

# new_list = ['a', 'i', 'e', 'o', 'y']
# num_list = [4,3,1,2]
# new_list.sort()
# print(new_list)
# num_list.sort()
# print(num_list)

# d = {'key1': 'value1', 'key2': [1,3,2], 'key3': 'value3'}
# print(d['key2'])
# d['key4'] = 'value4'
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())


# t = (1,2,3)
# print(type(t))
# print(t[0])
# print(t.count(1))
# print(t.index(3))

# mys = set()
# mys.add(1)
# print(mys)
# mys.add(2)
# print(mys)
# mys.add(2)
# print(mys)

# mylist = [3,3,3,4,4,2,2,5,5,1,2,7,8,9]
# set(mylist)
# print(set(mylist))

# print(True)
# print(False)
# print(type(False))
# print(1 > 2)
# b = None
# print(type(b))

# myfile = open('myfile.txt')
# # print(myfile.read())
# myfile.seek(0)

# contents = myfile.read()
# # print(contents)
# reading = myfile.readlines()
# print(reading)
# myfile.close()

# with open('myfile.txt') as my_new_file:
#     contents = my_new_file.read()

# # print(contents)
# with open('myfile.txt', mode='r') as myfile:
#     contents = myfile.read()

# print(contents)

# with open('my_new_file.txt', mode = 'r') as f:
#     print(f.read())

# with open('my_new_file.txt', mode='a') as f:
#     f.write('\nFOUR ON FOURTH')

    
# with open('my_new_file.txt', mode = 'r') as f:
#     print(f.read())

# with open('daasdf.txt', mode='w') as f:
#     f.write('I CREATED THIS FILE')

# with open('daasdf.txt', mode='r') as f:
#     print(f.read())

# print(type(3.2))
# print(math.sqrt(100))
# print(math.sq(10))
# s = 'hello'
# # Print out 'e' using indexing
# # print(s[1])
# # print(s[::-1])
# print(s[-1])
# print(s[4])

# list3 = [1,2,[3,4,'hello']]
# list3[2][2] = 'goodbye'
# # print(list3)

# list4 = [5,3,4,6,1]
# list4.sort()
# print(list4)

# d = {'simple_key':'hello'}
# # Grab 'hello'
# print(d['simple_key'])

# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'
# print(d['k1']['k2'])

# # Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

# #Grab hello

# # print(d['k1'][0]['nest_key'][1][0])

# # This will be hard and annoying!
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# print(d['k1'][2]['k2'][1]['tough'][2][0])

# # list5 = [1,2,2,33,4,4,11,22,3,3,2]

# print(set(list5))