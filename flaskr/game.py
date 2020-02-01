"""Модуль игровой логики"""
from random import randint

# Доска в которую сохраняются значения 'X' и '0'
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turns_remaining = 9
turn = 0
congrats = ""


def winner():
    """Сохранение ответа"""
    global congrats
    if check_win(board) == 'X':
        congrats = '👨‍💻'

    elif check_win(board) == 'O':
        congrats = '🖥'


def take_input(player_token, my_turn):
    """Ввод игрока"""
    board[my_turn-1] = player_token


def comp_input(comp_token):
    """Ввод компьютера"""
    valid = False
    while not valid:
        comp_answer = randint(1, 9)
        if (str(board[comp_answer-1]) not in "XO"):
            board[comp_answer-1] = comp_token
            valid = True


def check_win(board):
    """Проверка комбинаций"""
    win_coord = ((0, 1, 2), (3, 4, 5),
                 (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))

    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def game_loop(my_turn):
    """Игровая петля"""
    global turns_remaining
    global turn
    global congrats

    while turns_remaining:

        if turn % 2 == 0:
            take_input("X", my_turn)
            turn += 1
            turns_remaining -= 1
            winner()
            return congrats
        else:
            comp_input("O")
            turn += 1
            turns_remaining -= 1
            winner()
            return congrats

    if not turns_remaining:
        congrats = '⚔️'
        return congrats
