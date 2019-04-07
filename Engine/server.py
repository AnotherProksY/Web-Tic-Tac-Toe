# Серверный модуль
from bottle import get, post, request
from bottle import run, redirect
from bottle import template, TEMPLATE_PATH, static_file

# Модуль игровой логики
import GameLogic as GL

# Путь до HTML файлов
absolutePath = '/Users/kamil/Desktop/Dev/Python Codes/Web Tic-Tac-Toe/WebCode'
TEMPLATE_PATH.insert(0, absolutePath)

# Кто выиграл
setWinner = ""


@get('/static/<filename>')
def serverStatic(filename):
    """Статические файлы CSS и png"""
    return static_file(filename, root='../WebCode')


@get('/')
def mainPage():
    """Главная страница"""
    return template('MainPage.html')


@get('/GamePage')
def gamePage():
    """Страница с сеткой Tic-tac-toe"""
    return template('GamePage.html',
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
    resetValues(True)
    return template('Score.html', winner=str(setWinner))


@post('/Turn')
def Turn():
    """Функция игровой петли"""
    global setWinner
    myTurn = int(request.forms.get('myTurn'))

    # Первый вызов функции для обработки нашего хода
    setWinner = GL.gameLoop(myTurn)
    if setWinner == '👨‍💻':
        redirect('/GamePage/Score', code=None)
    elif setWinner == '⚔️':
        redirect('/GamePage/Score', code=None)

    # Второй вызов функции для обработки хода компьютера
    setWinner = GL.gameLoop(None)
    if setWinner == '🖥':
        redirect('/GamePage/Score', code=None)
    elif setWinner == '⚔️':
        redirect('/GamePage/Score', code=None)
    redirect('/GamePage', code=None)


def resetValues(doReset):
    """Чистим значения"""
    if doReset:
        GL.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        GL.turnsRemaining = 9
        GL.turn = 0
        GL.congrats = ""


def runServer(start):
    """Запускаем сервер"""
    if start:
        run(host='localhost', port=8080)
