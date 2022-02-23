""""""
# import configparser
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from resources.colors import Colors
# from resources.steps import Steps
# from src.visualizer import Visualizer
# from src.cube import Cube
# from src.player import Player
# from src.processor import Processor
#
#
#
# app = Flask(__name__, template_folder='web/templates')
#
# config = configparser.ConfigParser()
# config.read('resources/config.ini')
# DATABASE_URI = config.get('SQLALCHEMY', 'database_uri')
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# db = SQLAlchemy(app)
#
#
# CUBE_SIDE_PXLS = config.getint('VISUALIZER', 'side_pxls')
# CUBE_ROW = config.getint('CUBE', 'row')
# DIFFICULTY_COEFFICIENT = config.getfloat('DIFFICULTY_COEFFICIENT', 'medium')
# DIFFICULTY_LEVEL = (CUBE_ROW * CUBE_ROW) * DIFFICULTY_COEFFICIENT
#
#  insert this part to the routes part fix the doubling
# proc = Processor()  # double activating, need to fix( double visualize, add players)
#
#  add if
# db.create_all()
#
# load processor






