import sqlite3
from time import time as timestamp

from settings import Settings as SETTINGS


def leaderboards(player, score):
	newrecord = True

	con = sqlite3.connect(SETTINGS.DATABASE)
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS leaderboards
		(player text PRIMARY KEY, score integer)""")

	score_in_db = list(cur.execute("SELECT score from leaderboards WHERE player='{0}'".format(player)))
	
	if score_in_db:
		if score_in_db[0][0] < score:
			cur.execute("INSERT OR REPLACE INTO leaderboards (player, score) VALUES ('{0}', {1})".format(player, score))
		else:
			newrecord = False
	else:
		cur.execute("INSERT OR REPLACE INTO leaderboards (player, score) VALUES ('{0}', {1})".format(player, score))

	con.commit()
	con.close()

	return newrecord


def get_leaderboards():
	con = sqlite3.connect(SETTINGS.DATABASE)
	cur = con.cursor()

	result = list(cur.execute('SELECT * FROM leaderboards ORDER BY score DESC, rowid DESC'))

	con.close()
	return result