# python code to extract information via api from riot on my 100 aram games
# install request using
# pip install requests
import requests
# api key in another .py folder called creds.py
import creds

# api key and summonder name
summoner_name = 'Qrownin'

headers = {
    'X-Riot-Token': creds.api_key,
}


# API endpoint access for summoner
api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/qrownin"

# argument to connect key
api_url = api_url + '?api_key=' + creds.api_key

# request API key
response = requests.get(api_url)

# test status code and text
pass # print(response.status_code)

pass # print(response.json())

player_info = response.json()

player_account_ID = player_info['accountId']
player_name = player_info['name']
player_puuid = player_info['puuid']

# print functions to get player data
pass # print(player_account_ID)
pass # print(player_name)
pass # print(player_puuid)

#------------------

api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/Gjf1gwQxaVeCyWutDAAXv2hPXsZYUzk2Y93Kn4DXCH7UsnhgBtW-gfLnTVNTaFSJm5XyEFMgjP9UZQ/ids?start=0&count=100"

# separate arugment for new api key with &
api_url = api_url + "&api_key=" + creds.api_key


response = requests.get(api_url)

matches = response.json()

#print(len(matches))

# print(matches)

#-------------------------------------
# API endpoint access for matchId
api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4938690468" 

api_url = api_url + "?api_key=" + creds.api_key

pass # print(api_url)

response = requests.get(api_url)
match_id = response.json()

pass # print(response.status_code)
# print(response.json())

pass # print(match['metadata'])

# indicate the keys available in dataset
pass # print(match_id["info"].keys())

# print(match_id['info']['participants'][0])

#-----------------------------------
import pandas as pd
import requests
import time

# Function to retrieve player data from a match
def get_player_data(match_id):
    match_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}"
    match_params = {
        'api_key': creds.api_key
    }
    match_response = requests.get(match_url, params=match_params)

    # Check if the request was successful
    if match_response.status_code != 200:
        print(f"Failed to retrieve match data for match ID {match_id}. Status code: {match_response.status_code}")
        return None

    match_data = match_response.json()

    player_data = []
    if 'info' in match_data:
        participants = match_data['info']['participants']
        for participant in participants:
            player_data.append(participant)
    return player_data

# Loop through match IDs and retrieve player data
all_players_data = []
for match_id in matches:
    match_players_data = get_player_data(match_id)
    if match_players_data:
        all_players_data.extend(match_players_data)

        # Convert data to DataFrame
        df = pd.DataFrame(all_players_data)

        # Write data to Excel file
        df.to_excel('player_data.xlsx', index=False)
        print(f"Player data successfully updated with match ID {match_id}.")

    # Introduce a delay of 2 seconds between requests to bypass rate limit
    time.sleep(2)

# Check if any match data was retrieved
if not all_players_data:
    print("No match data was retrieved.")
