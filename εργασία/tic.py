

board = [' ' for x in range(10)]

def eisagwgh(letter, pos):
    board[pos] = letter

def fun1(pos):
    return board[pos] == ' '

def pinakas(board):
    print 
    print( board[1] + ' ' + board[2] + ' ' + board[3])
   
    print('------')
    
    print( board[4] + ' ' + board[5] + ' ' + board[6])
   
    print('------')
   
    print( board[7] + ' ' + board[8] + ' ' + board[9])

	
def Nikhths(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)
   
    

def paixths():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if fun1(move):
                    run = False
                    eisagwgh('X', move)
                else:
                    print('Den mporeis na valeis se authn thn thesh' )
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def upol():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if Nikhths(boardCopy, let):
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
        move = selectRandom(edgesOpen)
        
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
    print('Triliza!')
    pinakas(board)

    while not(isBoardFull(board)):
        if not(Nikhths(board, 'O')):
            paixths()
            pinakas(board)
        else:
            print('O upologisths se nikhse')
            break

        if not(Nikhths(board, 'X')):
            move = upol()
            if move == 0:
                print('Isopalia!')
            else:
                eisagwgh('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                pinakas(board)
        else:
            print('Mpravo!!Kerdises!')
            break

    if isBoardFull(board):
        print('Isopalia')

while True:
    answer = input('Thes na paikseis? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        
        main()
    else:
        break
	
			
		
	
	
		
	
