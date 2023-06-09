board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('\t\t\t   |   |')
    print('\t\t\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t\t\t   |   |')
    print('\t\t\t-----------')
    print('\t\t\t   |   |')
    print('\t\t\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t\t\t   |   |')
    print('\t\t\t-----------')
    print('\t\t\t   |   |')
    print('\t\t\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t\t\t   |   |')
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('\tPlease select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('\tSorry, this space is occupied!')
            else:
                print('\tPlease type a number within the range!')
        except:
            print('\tPlease type a number!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgeOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('\t\tWelcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('\t\tSorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('\t\tTie Game!')
            else:
                insertLetter('O', move)
                print('\t\tComputer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('\t\tX\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('\t\tTie Game!')

while True:
    answer = input('\t\tDo you want to play again? (Y/N)')
    if answer.lower() == 'y' or 'yes':
        board = [' ' for x in range(10)]
        print('\t\t-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        main()
    elif answer == 'n' or 'no':
    	print('\t\tThank you for playing!')
    break


