from random import randint

# Доска в которую сохраняются значения 'X' и '0'
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turnsRemaining = 9
turn = 0
congrats = ""


def winner():
    """Сохранение ответа"""
    global congrats
    if checkWin(board) == 'X':
        congrats = '👨‍💻'

    elif checkWin(board) == 'O':
        congrats = '🖥'


def takeInput(playerToken, myTurn):
    """Ввод игрока"""
    board[myTurn-1] = playerToken


def compInput(compToken):
    """Ввод компьютера"""
    valid = False
    while not valid:
        compAnswer = randint(1, 9)
        if (str(board[compAnswer-1]) not in "XO"):
            board[compAnswer-1] = compToken

            valid = True


def checkWin(board):
    """Проверка комбинаций"""
    winCoord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for each in winCoord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def gameLoop(myTurn):
    """Игровая петля"""
    global turnsRemaining
    global turn
    global congrats

    while turnsRemaining:

        if turn % 2 == 0:
            takeInput("X", myTurn)
            turn += 1
            turnsRemaining -= 1
            winner()
            return congrats
        else:
            compInput("O")
            turn += 1
            turnsRemaining -= 1
            winner()
            return congrats

    if not turnsRemaining:
        congrats = '⚔️'
        return congrats
