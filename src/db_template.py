import sqlite3
import random


class NewGameDB:

    def __init__(self):
        new_game_seed = 'resources/' + str(random.random())[2:] + '.db'
        print(new_game_seed)
        con = sqlite3.connect(new_game_seed)
        cur = con.cursor()
        cur.execute('''CREATE TABLE players(
        user_id INT PRIMARY KEY, 
        level INT, x INT, y INT, shoes INT
        ''')
        con.commit()
        cur.execute('''CREATE TABLE examined_rooms(
        room_id INT PRIMARY KEY,
        player INT, level INT, x INT, y INT, trap INT
        ''')
        con.commit()
        cur.execute('''CREATE TABLE statistics( 
        stat_id INT PRIMARY KEY, steps INT
        ''')
        con.commit()

