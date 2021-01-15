import sys

# 显示当前棋盘函数 display current board
def printBoard(board):
    print('┏━━━┳━━━┳━━━┓')
    print('┃ '+board['1'] + ' ┃ ' + board['2'] + ' ┃ ' + board['3']+' ┃')
    print('┣━━━╋━━━╋━━━┫')
    print('┃ '+board['4'] + ' ┃ ' + board['5'] + ' ┃ ' + board['6']+' ┃')
    print('┣━━━╋━━━╋━━━┫')
    print('┃ '+board['7'] + ' ┃ ' + board['8'] + ' ┃ ' + board['9']+' ┃')
    print('┗━━━┻━━━┻━━━┛')

# 计分板 scorer
def LeaderBoard():
    print('======================')
    print('LeaderBoard')
    print('X: '+str(Xwin)+' Wins')
    print('O: '+str(Owin)+' Wins')
    print('======================')


# 初始棋盘 reset board
def resettheboard():
    global theBoard
    theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
                '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

# 验证键盘输入是否为数字1-9 check validation of input
def checkCorrectNumber():
    global turn
    global move
    global theBoard
    while True:
        move = input()
        if move != '1' and move != '2' and move != '3' and move != '4' and move != '5' and move != '6' and move != '7' and move != '8' and move != '9':
            print('Please enter a number between 1-9 to move.')
            printBoard(theBoard)
            print('It\'s '+turn+'\'s turn, where would you like to move?')
        else:
            break

# 验证棋盘格子是否被占用  check occupation of the cells
def checkCorrectCell():
    global turn
    global move
    global theBoard
    while True:
        if theBoard[move] != ' ':
            print('This cell has been taken, please try again!')
            printBoard(theBoard)
            print('It\'s '+turn+'\'s turn, where would you like to move?')
            # 验证键盘输入是否为数字1-9 check validation of input
            checkCorrectNumber()
        else:
            break


theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ',
            '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

# 初始化计分器 initialize scorer
Xwin = 0
Owin = 0

# 简单教程 tutorial
print('Welcome to Tic-Tac-Toe! Place your marks in the cells, you can type down the numbers to select the cells.\nThe first one who has three marks in a row wins! X goes first!')

print('┏━━━┳━━━┳━━━┓      ┏━━━┳━━━┳━━━┓      ')
print('┃ 1 ┃ 2 ┃ 3 ┃      ┃ X ┃ O ┃   ┃      ')
print('┣━━━╋━━━╋━━━┫      ┣━━━╋━━━╋━━━┫      ')
print('┃ 4 ┃ 5 ┃ 6 ┃ ---> ┃   ┃ X ┃   ┃ ---> X won!')
print('┣━━━╋━━━╋━━━┫      ┣━━━╋━━━╋━━━┫     ')
print('┃ 7 ┃ 8 ┃ 9 ┃      ┃   ┃ O ┃ X ┃     ')
print('┗━━━┻━━━┻━━━┛      ┗━━━┻━━━┻━━━┛     ')
print()

print('Let\'s get started!')


# 显示当前棋盘 display board
printBoard(theBoard)


while True:
    # X的回合 X's turn
    turn = 'X'
    print('It\'s '+turn+'\'s turn, where would you like to move?')
    # 验证键盘输入是否为数字1-9 check validation of input
    checkCorrectNumber()
    # 验证棋盘格子是否被占用 check occupation of the cells
    checkCorrectCell()
    # 把X的选择输入到字典里 assgin X's choice to dictionary
    if move == '1':
        theBoard['1'] = 'X'
    elif move == '2':
        theBoard['2'] = 'X'
    elif move == '3':
        theBoard['3'] = 'X'
    elif move == '4':
        theBoard['4'] = 'X'
    elif move == '5':
        theBoard['5'] = 'X'
    elif move == '6':
        theBoard['6'] = 'X'
    elif move == '7':
        theBoard['7'] = 'X'
    elif move == '8':
        theBoard['8'] = 'X'
    elif move == '9':
        theBoard['9'] = 'X'
    # 显示当前棋盘 display board
    printBoard(theBoard)

    # 判断X是否赢了 check if X wins
    if (theBoard['1'] == 'X' and theBoard['2'] == 'X' and theBoard['3'] == 'X') or (theBoard['4'] == 'X' and theBoard['5'] == 'X' and theBoard['6'] == 'X') or (theBoard['7'] == 'X' and theBoard['8'] == 'X' and theBoard['9'] == 'X') or (theBoard['1'] == 'X' and theBoard['4'] == 'X' and theBoard['7'] == 'X') or (theBoard['2'] == 'X' and theBoard['5'] == 'X' and theBoard['8'] == 'X') or (theBoard['3'] == 'X' and theBoard['6'] == 'X' and theBoard['9'] == 'X') or (theBoard['1'] == 'X' and theBoard['5'] == 'X' and theBoard['9'] == 'X') or (theBoard['3'] == 'X' and theBoard['5'] == 'X' and theBoard['7'] == 'X'):
        print('X won!')
        Xwin += 1
        LeaderBoard()
        # 是否想再玩一遍 ask permission to play again
        while True:
            print('Would you like to play it again? (Y/N)')
            permission = input()
            if permission == 'Y':
                LeaderBoard()
                resettheboard()
                printBoard(theBoard)
                break
            elif permission == 'N':
                LeaderBoard()
                if Xwin > Owin:
                    print('Congratuations, X won!')
                elif Xwin == Owin:
                    print('It\'s a draw!')
                else:
                    print('Congratuations, O won!')
                sys.exit()
            else:
                print('You must enter Y or N!')
                continue
        continue

    # 判断格子是否满了 check occupation of the board
    if theBoard['1'] != ' ' and theBoard['2'] != ' ' and theBoard['3'] != ' ' and theBoard['4'] != ' ' and theBoard['5'] != ' ' and theBoard['6'] != ' ' and theBoard['7'] != ' ' and theBoard['8'] != ' ' and theBoard['9'] != ' ':
        print('It\'s a draw!')
        print('Let\'s try again!')
        LeaderBoard()
        resettheboard()
        printBoard(theBoard)
        continue

    # O的回合
    turn = 'O'
    print('It\'s '+turn+'\'s turn, where would you like to move?')
    # 验证输入是否为数字1-9
    checkCorrectNumber()
    # 验证棋盘格子是否被占用 check occupation of the cells
    checkCorrectCell()
    # 把O的选择输入到字典里 assgin O's choice to dictionary
    if move == '1':
        theBoard['1'] = 'O'
    elif move == '2':
        theBoard['2'] = 'O'
    elif move == '3':
        theBoard['3'] = 'O'
    elif move == '4':
        theBoard['4'] = 'O'
    elif move == '5':
        theBoard['5'] = 'O'
    elif move == '6':
        theBoard['6'] = 'O'
    elif move == '7':
        theBoard['7'] = 'O'
    elif move == '8':
        theBoard['8'] = 'O'
    elif move == '9':
        theBoard['9'] = 'O'
    # 显示当前棋盘 display board
    printBoard(theBoard)

    # 判断O是否赢了
    if (theBoard['1'] == 'O' and theBoard['2'] == 'O' and theBoard['3'] == 'O') or (theBoard['4'] == 'O' and theBoard['5'] == 'O' and theBoard['6'] == 'O') or (theBoard['7'] == 'O' and theBoard['8'] == 'O' and theBoard['9'] == 'O') or (theBoard['1'] == 'O' and theBoard['4'] == 'O' and theBoard['7'] == 'O') or (theBoard['2'] == 'O' and theBoard['5'] == 'O' and theBoard['8'] == 'O') or (theBoard['3'] == 'O' and theBoard['6'] == 'O' and theBoard['9'] == 'O') or (theBoard['1'] == 'O' and theBoard['5'] == 'O' and theBoard['9'] == 'O') or (theBoard['3'] == 'O' and theBoard['5'] == 'O' and theBoard['7'] == 'O'):
        print('O won!')
        Owin += 1
        LeaderBoard()
        # 是否想再玩一遍
        while True:
            print('Would you like to play it again? (Y/N)')
            permission = input()
            if permission == 'Y':
                LeaderBoard()
                resettheboard()
                printBoard(theBoard)
                break
            elif permission == 'N':
                LeaderBoard()
                if Xwin > Owin:
                    print('Congratuations, X won!')
                elif Xwin == Owin:
                    print('It\'s a draw!')
                else:
                    print('Congratuations, O won!')
                sys.exit()
            else:
                print('You must enter Y or N!')
                continue
        continue

    # 判断格子是否满了
    if theBoard['1'] != ' ' and theBoard['2'] != ' ' and theBoard['3'] != ' ' and theBoard['4'] != ' ' and theBoard['5'] != ' ' and theBoard['6'] != ' ' and theBoard['7'] != ' ' and theBoard['8'] != ' ' and theBoard['9'] != ' ':
        print('It\'s a draw!')
        print('Let\'s try again!')
        LeaderBoard()
        resettheboard()
        printBoard(theBoard)
        continue
