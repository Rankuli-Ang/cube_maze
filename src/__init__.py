""""""
import configparser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources.colors import Colors
from resources.steps import Steps
from src.visualizer import Visualizer
from src.cube import Cube
from src.player import Player
from src.processor import Processor


config = configparser.ConfigParser()
config.read('resources/config.ini')
DATABASE_URI = config.get('SQLALCHEMY', 'database_uri')


CUBE_SIDE_PXLS = config.getint('VISUALIZER', 'side_pxls')
CUBE_ROW = config.getint('CUBE', 'row')
DIFFICULTY_COEFFICIENT = config.getfloat('DIFFICULTY_COEFFICIENT', 'medium')
DIFFICULTY_LEVEL = (CUBE_ROW * CUBE_ROW) * DIFFICULTY_COEFFICIENT

proc = Processor()  #  double activating, need to fix( double visualize, add players)
proc.new_game(CUBE_ROW, DIFFICULTY_LEVEL)
proc.create_visualizer(CUBE_SIDE_PXLS, Colors.FRAME_COLOR,
                       Colors.PLAYER_COLOR, Colors.TRAP_COLOR,
                       Colors.EXIT_COLOR,
                       Colors.EXAMINED_COLOR, Colors.NOT_EXAMINED_COLOR)

# proc.process()


app = Flask(__name__, template_folder='web/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)


class PlayerStats(db.Model):  # add examined rooms
    id = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    shoes = db.Column(db.Integer, nullable=False)


new_stats = proc.get_player().get_stats()
player_stats = PlayerStats(level=new_stats['coords'][0],
                           x=new_stats['coords'][1], y=new_stats['coords'][2],
                           shoes=new_stats['shoes'])
db.session.add(player_stats)
db.session.commit()

