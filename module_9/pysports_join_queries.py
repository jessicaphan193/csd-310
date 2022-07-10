import mysql.connector
#from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "J3$$ic@21",
    database = "pysports"
)

cursor = db.cursor()

print("-- DISPLAYING PLAYER RECORDS --")

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

all = cursor.fetchall()

for player in all:
    print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

input("\n Press any key to continue...")

db.close