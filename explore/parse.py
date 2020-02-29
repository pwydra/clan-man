import json
import mysql.connector
import time
import datetime
import os

#ts = time.time()
#timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

WAR = 'War Hero'
GAMES = 'Games Champion'
DONATIONS = 'Friend in Need'
SPELL_DONATIONS = 'Sharing is caring'
AS_OF_DATE = "2020-02-21 22:00:00"

#CLAN_TAG = "#8CCLVY9L"
CLAN_TAG = os.environ['CLAN_TAG']
DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  passwd=DB_PASSWORD,
  database=DB_NAME
)

mycursor = mydb.cursor()

# player statements
INSERT_PLAYER      = "INSERT INTO player (player_id, first_known_player_name, player_welcome) VALUES (%s, %s, %s)"

# clan_player statements
INSERT_CLAN_PLAYER = "INSERT INTO clan_player (clan_id, player_id, as_of_datetime) VALUES (%s, %s, %s)"

# player progress
INSERT_PLAYER_PROGRESS = (
  "insert into player_progress ("
  "  player_id, current_player_name, as_of_datetime,"
  "  troops_donated, troops_received, friend_in_need,"
  "  war_hero, sharing_is_caring, games_champion"
  ") values ("
  "  %s, %s, %s,"
  "  %s, %s, %s,"
  "  %s, %s, %s)")

with open('./player.json') as file:
  player_data = json.load(file)

for player in player_data:
  tag = player["tag"]
  name = player["name"]
  donations = player["donations"]
  donations_received = player["donationsReceived"]
  achievements = player["achievements"]
  for achievement in achievements:
    if achievement['name'] == WAR:
      war_stars =  achievement['value']
    if achievement['name'] == GAMES:
      games_progress = achievement['value']
    if achievement['name'] == SPELL_DONATIONS:
      spell_donations = achievement['value']
    if achievement['name'] == DONATIONS:
      total_donations = achievement['value']

  mycursor.execute(INSERT_PLAYER, (tag, name, "1"))
  mycursor.execute(INSERT_CLAN_PLAYER, (CLAN_TAG, tag, AS_OF_DATE))
  mycursor.execute(INSERT_PLAYER_PROGRESS, (
    tag, name, AS_OF_DATE, 
    donations, donations_received, total_donations,
    war_stars, spell_donations, games_progress
  ))

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")

