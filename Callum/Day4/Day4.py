from Board import Board

with open("./input.txt", "r") as inputFile:
    numbers = inputFile.readline().split(',')
    inputFile.readline()
    boardsStr = inputFile.read().split("\n\n")

boards = []
for boardStr in boardsStr:
    boards.append(Board(boardStr.splitlines()))
    
def GetWinningBoard():
    won = False
    for number in numbers:
        for board in boards:
            if board.Mark(number):
                print(f'Score: {board.Score() * int(number)}')
                won = True
        if won:
            break
        
def GetLosingBoard():
    for number in numbers:
        for board in reversed(boards):
            if board.Mark(number):
                if len(boards) == 1:
                    print(f'Score: {board.Score() * int(number)}')
                boards.remove(board)
    
GetWinningBoard()
#GetLosingBoard()
