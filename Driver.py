from AStar import astar
from BFS import bfs

### Welcome message
print("Welcome to the game")

### Dictionary
dic  = {
    '1': 'very_easy.txt',
    '2': 'easy.txt',
    '3': 'medium.txt',
    '4': 'hard.txt',
    '5': 'very_hard.txt'
}

### Choose Mode
instruction = '''
    Please choose your game mode base on the corresponding number
    1. very easy
    2. easy
    3. medium
    4. hard
    5. very hard
    '''
print(instruction)
mode = input("Enter mode: ")
while mode not in dic:
    # Re-enter:
    mode = input("Please re-enter: ")
file = open(f'./mode/{dic[mode]}').read()

### Method dictionary
dic2 = {
    '1': 'BFS',
    '2': 'A*'
}

### Choose Method
instruction2 = '''
    Please choose your method base on the corresponding number
    1. BFS
    2. A*
'''
print(instruction2)
method = input("Enter method: ")
while method not in dic2:
    method = input("Please re-enter: ")

match method:
    case '1':
        print("BFS method")
        game = bfs(file)
        game.getSolution()

    case '2':
        print("A Star")
        game = astar(file)
        game.getSolution()