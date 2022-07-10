import mysql.connector
#from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "J3$$ic@21",
    database = "pysports"
)

cursor = db.cursor()

print("-- DISPLAYING PLAYERS AFTER INSERT --")

cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES (%s,%s,%s)", ("Smeagol", "Shire Folk", 1))

db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

for player in cursor:
  print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))


print("-- DISPLAYING PLAYERS AFTER UPDATE --")

cursor.execute("UPDATE player SET team_id = '2' WHERE team_id = '1' ")

db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

for player in cursor:
   print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))


print("-- DISPLAYING PLAYERS AFTER DELETE --")

cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol' ")

db.commit()

cursor.execute("SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

for player in cursor:
   print("\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

input("\n Press any key to continue...")

db.close