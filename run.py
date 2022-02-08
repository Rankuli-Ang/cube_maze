# from src import app
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

""""""
import configparser
from flask import Flask
from resources.colors import Colors
from resources.steps import Steps
from src.visualizer import Visualizer
from src.cube import Cube
from src.player import Player
from src.processor import Processor


config = configparser.ConfigParser()
config.read('resources/config.ini')

CUBE_SIDE_PXLS = config.getint('VISUALIZER', 'side_pxls')
CUBE_ROW = config.getint('CUBE', 'row')
DIFFICULTY_LEVEL = config.getint('DIFFICULTY_LEVEL', 'medium')

proc = Processor()
proc.new_game(CUBE_ROW, DIFFICULTY_LEVEL)
proc.create_visualizer(CUBE_SIDE_PXLS, Colors.FRAME_COLOR,
                       Colors.PLAYER_COLOR, Colors.TRAP_COLOR,
                       Colors.EXAMINED_COLOR,
                       Colors.EXAMINED_COLOR, Colors.NOT_EXAMINED_COLOR)

game = True
while game:
    proc.process()

# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


