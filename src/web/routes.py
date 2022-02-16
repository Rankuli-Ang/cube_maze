import src
from flask import render_template
import cv2


@src.app.route("/")
def home_page():
    return render_template('home.html')


@src.app.route("/game")
def game_page():
    player_stats = src.proc.get_player().test_get_stats()
    return render_template('game.html',
                           cube_row=src.CUBE_ROW, difficulty_level=src.DIFFICULTY_LEVEL,
                           coords=player_stats[0], shoes=player_stats[1],
                           rooms=player_stats[2], alive=player_stats[3])


@src.app.route("/login")
def login_page():
    return render_template('login.html')


@src.app.route("/registration")
def registration_page():
    return render_template('registration.html')
