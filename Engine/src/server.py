# Серверный модуль
from bottle import get, post, request
from bottle import run, redirect
from bottle import template, static_file

# Модуль игровой логики
import src.GameLogic as GL

# Модуль для получения пути
from pathlib import Path

# Путь до HTML файлов
getCWD = str(Path().absolute())
absolutePath = getCWD.replace('Engine', 'WebCode')

# Кто выиграл
set_winner = ""


# Статические файлы------------------------------------------
@get('/static/css/<filename>')
def CSS(filename):
    """Статические файлы CSS"""
    return static_file(filename, root=Path(absolutePath + '/css'))


@get('/static/fonts/<filename>')
def fonts(filename):
    """Статические файлы Fonts"""
    return static_file(filename, root=Path(absolutePath + '/fonts'))



@get('/static/img/<filename>')
def IMG(filename):
    """Статические файлы IMG"""
    return static_file(filename, root=Path(absolutePath + '/img'))



@get('/static/favicon/<filename>')
def FAV(filename):
    """Статические файлы FAV"""
    return static_file(filename, root=Path(absolutePath + '/favicon'))

# -----------------------------------------------------------


# Руты-------------------------------------------------------
@get('/')
def main_page():
    """Главная страница"""
    return template(absolutePath + '/MainPage.html')


@get('/GamePage')
def game_page():
    """Страница с сеткой Tic-tac-toe"""
    return template(absolutePath + '/GamePage.html',
                    place_1=str(GL.board[0]),
                    place_2=str(GL.board[1]),
                    place_3=str(GL.board[2]),
                    place_4=str(GL.board[3]),
                    place_5=str(GL.board[4]),
                    place_6=str(GL.board[5]),
                    place_7=str(GL.board[6]),
                    place_8=str(GL.board[7]),
                    place_9=str(GL.board[8]))


@get('/GamePage/Score')
def gamePageScore():
    """Страница с выводом очков"""
    reset_values(True)
    return template(absolutePath + '/Score.html', winner=str(set_winner))
# -----------------------------------------------------------


# Функции----------------------------------------------------
@post('/Turn')
def Turn():
    """Функция игровой петли"""
    # Функция проверки победителя
    def winner(player):
        global set_winner
        set_winner = GL.game_loop(player)
        if set_winner:
            redirect('/GamePage/Score', code=None)

    # Первый вызов функции для обработки нашего хода
    winner(int(request.forms.get('myTurn')))

    # Второй вызов функции для обработки хода компьютера
    winner(None)
    
    # Прыгнуть обратно на страницу с сеткой
    redirect('/GamePage', code=None)


def reset_values(do_reset):
    """Чистим значения"""
    if do_reset:
        GL.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        GL.turns_remaining = 9
        GL.turn = 0
        GL.congrats = ""


def run_server(start):
    """Запускаем сервер"""
    if start:
        run(host='localhost', reloader=True, port=8080)
# -----------------------------------------------------------
