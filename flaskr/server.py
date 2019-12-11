# Серверный модуль
from flask import Flask
app = Flask(__name__)

# Модуль игровой логики
import flaskr.game_logic as GL

# Модуль для получения пути
from pathlib import Path

# Путь до HTML файлов
get_cwd = str(Path().absolute())
absolute_path = get_cwd + '/flaskr'

# Кто выиграл
set_winner = ""


# Статические файлы------------------------------------------
@app.route('/static/<filename>')
def CSS(filename):
    """Статические файлы CSS"""
    return static_file(filename, root=Path(absolute_path + '/css'))


@app.route('/static/<filename>')
def fonts(filename):
    """Статические файлы Fonts"""
    return static_file(filename, root=Path(absolute_path + '/fonts'))


@app.route('/static/<filename>')
def IMG(filename):
    """Статические файлы IMG"""
    return static_file(filename, root=Path(absolute_path + '/img'))


@app.route('/static/<filename>')
def FAV(filename):
    """Статические файлы FAV"""
    return static_file(filename, root=Path(absolute_path + '/favicon'))

# -----------------------------------------------------------


# Руты-------------------------------------------------------
@app.route('/')
def main_page():
    """Главная страница"""
    reset_values(True)
    return template(absolute_path + '/MainPage.html')


@app.route('/GamePage')
def game_page():
    """Страница с сеткой Tic-tac-toe"""
    return template(absolute_path + '/GamePage.html',
                    place_1=str(GL.board[0]),
                    place_2=str(GL.board[1]),
                    place_3=str(GL.board[2]),
                    place_4=str(GL.board[3]),
                    place_5=str(GL.board[4]),
                    place_6=str(GL.board[5]),
                    place_7=str(GL.board[6]),
                    place_8=str(GL.board[7]),
                    place_9=str(GL.board[8]))


@app.route('/GamePage/Score')
def game_page_score():
    """Страница с выводом очков"""
    reset_values(True)
    return template(absolute_path + '/Score.html', winner=str(set_winner))
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
        app.run(debug=True,host='0.0.0.0')

# -----------------------------------------------------------
