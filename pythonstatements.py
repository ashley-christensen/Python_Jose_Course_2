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

# print(2 in [1,2,3])

# from random import shuffle
# mylist = [1,2,3]
# shuffle(mylist)
# print(mylist)

# from random import randint
# randint(0,100)
# print(randint(0,10))

# result = input('enter a number here: ')
# print(f'whoa {result}')

# mylist = [x for x in range(0, 11) if x%2 == 0]

# print(mylist)

# myveg = ['tomato', 'watermelon', 'grass']
# myfruit = [x for x in myveg if x == 'watermelon']
# print(myfruit)

# mynums = [x for x in range(1, 101)]

# for num in mynums:
#     if num%3 == 0 and num%5 == 0:
#         print(f'{num} = fizzbuzz')
#     if num%3 == 0:
#         print(f'{num} = fizz')
#     if num % 5 == 0:
#         print(f'{num} = buzz')
#     else:
#         print(num)


# st = 'create a list of teh first letters of every word in this string'
# mylist = [x for x in st.split()[1]]
# print(mylist)

# mylist = [1,2,3,4]

# mylist.append(1)
# print(mylist)

# def name_of_function() --> snake casing

# result = input('enter your name here')

# def say_hello(name):
#     '''calls hello'''
#     return f'hello  + {name}'

# call = say_hello(result)
# print(call)

# def add_function(num1, num2):
#     return num1 + num2

# numbers = add_function(3,4)
# print(numbers)

# def even_check(number):
#    return number % 2 == 0

# final = even_check(20)
# print(final)

# mylist = [x for x in range(1,12)]
# print(mylist)

# def evens_only(list):
#     return [x for x in list if x%2 == 0]

# evens = evens_only(mylist)
# print(evens)

# def give_evens_list(list):

#     new_list = []

#     for number in list:
#         if number % 2 == 0:
#             new_list.append(number)

#     return new_list

# result = give_evens_list([x for x in range(1,150)])
# print(result)

# work_hours = [('Abby',1000), ('Billy', 400), ('John', 900)]

# def employee_check(work_hours):
#     current_max = 0
#     employee_of_month = ''

#     for employee, hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
#         else:
#             pass
 
#     #Return
#     return (employee_of_month, current_max)

# result = employee_check(work_hours)
# name, hours = employee_check(work_hours)
# print(hours, name)



# # Interactions between functions
# example = [' ', 'O', ' ']
# from random import shuffle
# result = shuffle(example)

# def shuffle_list(mylist):
#     shuffle(mylist)
#     return(mylist)

# def player_guess():
#     guess = '' 

#     while guess not in ["0", "1", "2"]:
#         guess = input("Pick a number: 0, 1, or 2")

#     return int(guess)

# myindex = player_guess()

# def check_guess(mylist, guess):
#     if mylist[guess] == 'O':
#         print('Correct!')
#     else:
#         print("Wrong Guess!")
#         print(mylist)

# #Initial List
# mylist = [' ', 'O', ' ']
# #Shuffle List
# mixedup_list = shuffle_list(mylist)
# #User Guess
# guess = player_guess()
# #Check User Guess
# check_guess(mixedup_list, guess)


#Quick Solutions
#*arg arbitrary number of parameters

# def myfunc(*args):#treat as tuple of parameters
#     print(args)
#     return sum(args) * .05
    

# result = myfunc(40, 60)
# print(result)

# def myfunc(**kwargs): #treat as dictionary of parameters
#     if 'fruit' in kwargs:
#         print('my fruit of chioce is {}'.format(kwargs['fruit']))

# myfunc(fruit='fruit')

# def myfunc(*args, **kwargs):
#     print('I would like {} {}'.format(args[1], kwargs['fruit']))

# result = myfunc(10,20,30, fruit = 'apple', food = 'rice')
# print(result)

# tuple = (0,1,2)

# def myfunc(*args):
#     my_list = []
    
#     for thing in args:
#         if thing%2 == 0:
#             my_list.append(thing)
#     print(my_list)
#     return my_list 
# myfunc(tuple)

# def myfunc(**kwargs):
    
#     for item in kwargs:
#         print(item)

# result = myfunc()


# row2[1] = 'X'
# display(row1, row2, row3)

#Input function

# position_index = int(input("Please enter a value from 0-2: "))
# row1[position_index] = 'X'
# display(row1, row2, row3)

# row1 = ['','','']
# row2 = ['','','']
# row3 = ['','','']


# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)

# def user_choice():

#     #Variables

#     #Initial
#     choice = "WRONG"
#     acceptable_range = range(0,10)
#     within_range = False

#     #Two conditions to check
#     #DIGIT OR WITHIN_RANGE =- False
#     while choice.isdigit() == False:

#         choice = input("Please enter number (0-10): ")
        
#         #Digit check
#         if choice.isdigit() == False:
#             print("Sorry, not a digit!")
#         #Range check
#         if choice.isdigit() == True:
#             if int(choice) in acceptable_range:
#                 within_range = True
#             else:
#                 print("Sorry, you're out of 0-10 acceptable range")
#                 within_range = False
                 
    
#     return int(choice)

# user_choice()
from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    def player_input():
        marker = ''
    
        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    
    def place_marker(board, marker, position):
        board[position] = marker

    
    def win_check(board,mark):
    
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
        (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
    
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

            
