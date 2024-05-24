def displayChess(chBoard):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            print(chBoard[row][col], end=" ")
        print()

def isQueenPlaceValid(chBoard, crntRow, crntCol):
    for i in range(crntCol):
        if chBoard[crntRow][i]:
            return False
    for i, j in zip(range(crntRow, -1, -1), range(crntCol, -1, -1)):
        if chBoard[i][j]:
            return False
    for i, j in zip(range(crntRow, BOARD_SIZE), range(crntCol, -1, -1)):
        if chBoard[i][j]:
            return False
    return True

def solveProblem(chBoard, crntCol):
    if crntCol >= BOARD_SIZE:
        return True
    for i in range(BOARD_SIZE):
        if isQueenPlaceValid(chBoard, i, crntCol):
            chBoard[i][crntCol] = 1
            if solveProblem(chBoard, crntCol + 1):
                return True
            chBoard[i][crntCol] = 0
    return False

def displaySolution():
    chBoard = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    if not solveProblem(chBoard, 0):
        print("Solution does not exist")
        return False
    displayChess(chBoard)
    return True

if __name__ == "__main__":
    BOARD_SIZE = int(input("Enter the size of the chessboard: "))
    displaySolution()
