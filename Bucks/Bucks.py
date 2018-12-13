####Synopsis
#   I got this idea when I was awtching the bucks game and wondered if there was somewhere that I could
#   grab all of the stats from the NBA
#   I found this article https://www.quora.com/Is-there-an-NBA-API-for-free-that-has-live-stats
#   From there my goals are as follows
#   1. get all team stats for each game
#   2. use this data to attempt to predict a win.
#   3. test model
#   4. intereate

#import packages
import requests, json

base_url = 'http://data.nba.net'

#get all the files
response = requests.get(base_url+'/10s/prod/v1/today.json')
links = json.loads(response.text)

#get all Teams
teams_URL = links['links']['teams']
teamsURL = base_url+teams_URL
teams_response = requests.get(teamsURL)
teams=json.loads(teams_response.text)
teams=teams['league']['standard']

#get TeamID
Iteration = -1
for team in teams:
    Iteration = Iteration+1
    for key, value in team.items():
       if key == 'city' and value == 'Milwaukee':
            MKE = Iteration
BucksID = teams[MKE]['teamId']

#get Schedule
Schedule_URL = links['links']['teamSchedule']
Schedule_URL = base_url+Schedule_URL
Schedule_URL=Schedule_URL.replace('{{teamUrlCode}}',str(BucksID))

Schedule_response = requests.get(Schedule_URL)
Schedule=json.loads(Schedule_response.text)
Schedule=Schedule['league']['standard']

#get games
Iteration = -1
Games= []
Game = {}
for game in Schedule:
    Iteration = Iteration+1
    #print(Iteration,game['gameId'],game['seasonStageId'],game['startTimeUTC'],game['isHomeTeam'])
    Game = {
        'gameIndex' : Iteration,
        'gameID' : game['gameId'],
        'seasonStageID': game['seasonStageId'],
        'startTimeUTC' :game['startTimeUTC'],
        'startDateEastern': game['startDateEastern'],
        'isHomeTeam': game['isHomeTeam']
        }
    print(Game)
    #Games.append(Game)
#print(Games)
