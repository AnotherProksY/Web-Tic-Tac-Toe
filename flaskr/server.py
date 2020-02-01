"""Серверный модуль"""

# Модуль игровой логики
import flaskr.game as GL

from flask import Flask
from flask import render_template
from flask import request, redirect
app = Flask(__name__)


# Кто выиграл
set_winner = ""


# Роуты-------------------------------------------------
@app.route('/')
def main_page():
    """Главная страница"""
    reset_values(True)
    return render_template('index.html')


@app.route('/GamePage')
def game_page():
    """Страница с сеткой Tic-tac-toe"""
    return render_template(
                    'game.html',
                    place_1=str(GL.board[0]),
                    place_2=str(GL.board[1]),
                    place_3=str(GL.board[2]),
                    place_4=str(GL.board[3]),
                    place_5=str(GL.board[4]),
                    place_6=str(GL.board[5]),
                    place_7=str(GL.board[6]),
                    place_8=str(GL.board[7]),
                    place_9=str(GL.board[8])
    )


@app.route('/GamePage/Score')
def game_page_score():
    """Страница с выводом победителя"""
    reset_values(True)
    return render_template('score.html', winner=str(set_winner))
# -----------------------------------------------------------


# Функции----------------------------------------------------
@app.route('/Turn', methods=['POST'])
def Turn():
    """Функция игровой петли"""
    # Функция проверки победителя
    def winner(player):
        global set_winner
        set_winner = GL.game_loop(player)
        if set_winner:
            return True

    # Первый вызов функции для обработки нашего хода
    if winner(int(request.form.get('myTurn'))):
        return redirect('/GamePage/Score')

    # Второй вызов функции для обработки хода компьютера
    if winner(None):
        return redirect('/GamePage/Score')

    # Прыгнуть обратно на страницу с сеткой
    return redirect('/GamePage')


def reset_values(do_reset):
    """Чистим значения для следующей игры"""
    if do_reset:
        GL.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        GL.turns_remaining = 9
        GL.turn = 0
        GL.congrats = ""

# -----------------------------------------------------------
