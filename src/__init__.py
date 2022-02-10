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
DIFFICULTY_COEFFICIENT = config.getfloat('DIFFICULTY_COEFFICIENT', 'medium')
DIFFICULTY_LEVEL = (CUBE_ROW * CUBE_ROW) * DIFFICULTY_COEFFICIENT

proc = Processor()
proc.new_game(CUBE_ROW, DIFFICULTY_LEVEL)
proc.create_visualizer(CUBE_SIDE_PXLS, Colors.FRAME_COLOR,
                       Colors.PLAYER_COLOR, Colors.TRAP_COLOR,
                       Colors.EXIT_COLOR,
                       Colors.EXAMINED_COLOR, Colors.NOT_EXAMINED_COLOR)

# end_game = False
# while not end_game:
#     end_game = proc.process()
#
# proc.end_game()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
