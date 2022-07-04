import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "J3$$ic@21",
    database = "pysports"
)

cursor = db.cursor()

#cursor.execute(f_query)
#cursor.execute(s_query)

f_query = "SELECT team_id, team_name, mascot FROM team"

s_query = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor.execute(f_query)
for team in cursor:
   print(team)

cursor.execute(s_query)
for player in cursor:
    print(player)

cursor.close()

db.close()