from flask import render_template
from src import app, proc, CUBE_ROW, CUBE_SIDE_PXLS, \
    DIFFICULTY_LEVEL
from resources.colors import Colors


@app.route("/")
def new_game():  # temporary solution
    proc.new_game(CUBE_ROW, DIFFICULTY_LEVEL)
    proc.create_visualizer(CUBE_SIDE_PXLS, Colors.FRAME_COLOR,
                           Colors.PLAYER_COLOR, Colors.TRAP_COLOR,
                           Colors.EXIT_COLOR,
                           Colors.EXAMINED_COLOR, Colors.NOT_EXAMINED_COLOR)
    return render_template('home.html')


@app.route("/game")
def game_page():
    return render_template('game.html')


@app.route("/login")
def login_page():
    return render_template('login.html')


@app.route("/registration")
def registration_page():
    return render_template('registration.html')
