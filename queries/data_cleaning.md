-------------------------------------------------------------
						          Deleting data
-------------------------------------------------------------
columns that are not needed for the analysis
since this game mode does not have certain objectives, some columns are not needed
examples being baron, dragons, ward
data not needed for analysis such as various pings

```sql
-- Dropping multiple unneeded columns
ALTER TABLE 
  aram_games.dbo.aram_data 
DROP 
  COLUMN allInPings, 
  perks, 
  challenges, 
  assistMePings, 
  baronKills, 
  basicPings, 
  championTransform, 
  commandPings, 
  dangerPings, 
  detectorWardsPlaced, 
  dragonKills, 
  eligibleForProgression, 
  enemyMissingPings, 
  enemyVisionPings, 
  getBackPings, 
  holdPings, 
  individualPosition, 
  lane, 
  missions, 
  needVisionPings, 
  neutralMinionsKilled, 
  objectivesStolen, 
  objectivesStolenAssists, 
  onMyWayPings, 
  placement, 
  playerAugment1, 
  playerAugment2, 
  playerAugment3, 
  playerAugment4, 
  playerScore0, 
  playerScore1, 
  playerScore10, 
  playerScore11, 
  playerScore2, 
  playerScore3, 
  playerScore4, 
  playerScore5, 
  playerScore6, 
  playerScore7, 
  playerScore8, 
  playerScore9, 
  playerSubteamid, 
  pushPings, 
  riotIdTagline, 
  role, 
  sightWardsBoughtInGame, 
  subteamPlacement, 
  teamEarlySurrendered, 
  teamId, 
  teamPosition, 
  totalAllyJungleMinionsKilled, 
  totalEnemyJungleMinionsKilled, 
  unrealKills, 
  visionClearedPings, 
  visionScore, 
  visionWardsBoughtInGame, 
  wardsKilled, 
  wardsPlaced;

```
-------------------------------------------------------------
				   		     Game count with summoners
-------------------------------------------------------------
checking number of games for each summoner in data
100 games should have 100 count of my in game name: Qrownin

 ```sql 
-- view game count
SELECT 
  summonerName, 
  count(summonerName) AS games_played 
FROM 
  aram_games.dbo.aram_data 
GROUP BY 
  summonerName 
ORDER BY 
  count(summonerName) DESC

```
-------------------------------------------------------------
					        	Adressing null values
-------------------------------------------------------------
there are a few null values to address but does not seem to overall matter too much for the analysis
null values found are in summonerName as some names are null but given riotIfGameName
most game names and summoner name are the same but others are different due potential name change
i will assign null values to their riotIdGameName for now. it will not affect the overall analysis as the focus are not on the players but the game data overall
vice versa as well since there are null values in riot id game name
this will assist in the reference 

```sql
-- riotidGameName is the same as summonerName
SELECT 
  DISTINCT riotIdGameName, 
  summonerName 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  riotIdGameName = summonerName
```
```sql
-- riotIdGameName is not the same as summonerName
SELECT 
  riotIdGameName, 
  summonerName 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  riotIdGameName <> summonerName

```
```sql
-- null values for summonerName
SELECT 
  riotIdGameName, 
  summonerName 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  summonerName IS NULL

```
```sql
-- Update test for missing null value
UPDATE 
  aram_games.dbo.aram_data 
SET 
  summonerName = 'hot aramer tgirl' 
WHERE 
  riotIdGameName = 'hot aramer tgirl' 
SELECT 
  summonerName 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  summonerName = 'hot aramer tgirl'

```

```sql
-- rest of null values
UPDATE 
  aram_games.dbo.aram_data 
SET 
  summonerName = 'CalPork' 
WHERE 
  riotIdGameName = 'CalPork' 
  
UPDATE 
  aram_games.dbo.aram_data 
SET 
  summonerName = 'shiraki' 
WHERE 
  riotIdGameName = 'shiraki' 

UPDATE 
  aram_games.dbo.aram_data 
SET 
  summonerName = 'ZeroJuju' 
WHERE 
  riotIdGameName = 'ZeroJuju' 
```
```sql
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'BLM Quavo' 
WHERE 
  puuid = 'a4D-WeOlZJD5oOJZ8WCb9lIxCv_5yGcF4azg8xbbweIebxyEzxzV1IOr7M4SGvh3r2YtBTBXmmT_KQ' -- test
SELECT 
  riotIdGameName 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  puuid = 'a4D-WeOlZJD5oOJZ8WCb9lIxCv_5yGcF4azg8xbbweIebxyEzxzV1IOr7M4SGvh3r2YtBTBXmmT_KQ' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'BLM Quavo' 
WHERE 
  puuid = 'a4D-WeOlZJD5oOJZ8WCb9lIxCv_5yGcF4azg8xbbweIebxyEzxzV1IOr7M4SGvh3r2YtBTBXmmT_KQ' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Teravolte' 
WHERE 
  puuid = 'RPxdnbIWkmPg76yc7_Va0rWT91Uz7rIbJAypRWA37MkJ0ftltzjmzwDm_moRWDWObGGyahIkfTgQAQ' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = '??v?n Æ?évén' 
WHERE 
  puuid = '3lZuzNI3b_NuBM--Ld0jN6gVBEfMKAVaH8Nohz4kUuOtQJWgUFcxvVdL4ungwQuxlYTDHaQfjswYKg' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Pardner' 
WHERE 
  puuid = 'qMYCEr_i_hrsDaVk3BmG6JcUTmSnGFsIpBEy0ThHEJkVXKMNVBOYfUot2L7x9mZgDatRhc6qLyLIVg' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Gimhae Kimchanho' 
WHERE 
  puuid = 'He4AAAY1_YEzQxVIvlg5bCfx67Iy5Cde4YFJ5Uxzrl_FSsVkHrHzdHi6sOnCHLuXIWHqO82RpenCKw' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = '60 Pengu' 
WHERE 
  puuid = '14AVtQHRZjkdzoAEkxZVQ6WE7cv7SnnmakY-8Lp9Cd3Dn6RJbj3WaVQm1nut7Iq3NF3E4NpEJJHSrQ' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Jiu Jiu Jiu' 
WHERE 
  puuid = '_RYahK1LRVnk_s48dZ9prEqWQh30HOCrjtiKZdXlASZwtOfHFBwswUMoJ0L9mNKs1W0hKXtw3iUrbg' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Mokbi' 
WHERE 
  puuid = 'aQXo-aJ6vhuLughGosMsiewybT5PfyREyZz6wkKWBnl0irkcUVCo0cyRqp19I-NpVQuUIFC9smxlpA' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'rbookki' 
WHERE 
  puuid = 'GQ5opsDeaNkGLO6x5jvQSfJGfBhjFsD3kppcA91bMmK9lbpm4qibDHMnv-kQkqhh4ovCU-39BHy23w' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'zu ãn meî meî' 
WHERE 
  puuid = 'maqdN2JrMX8n7LPMWlA01f9StX4DYY-8NrwhReNr4WdFHD1LSJLl-VdyrPu9tsY2O3xPek_hMADP7w' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'Lazy Tamago' 
WHERE 
  puuid = 'dWR1z4PJxaURahP55ICTUMbD5zXbHDzn8z2FR7GHPsKqTP5OjiFIcCXE8AueXCpRBgkZN4BF9H6brw' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'LynnwoodBloodSea' 
WHERE 
  puuid = 'OU1fyVp14lukRUkqVRfmmyaWzjU-rYswIAHzUE1f49pZfgBAX9eY6fLy99gETuKNCQtvJ8B3iD_BeQ' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'TimeClimber' 
WHERE 
  puuid = 'cMG6g1ZhG2Xf4XxBGj6f-jFOIE0xlhLz7SiPL9rDvBj6SlUEGGKbQt2wd8W79UKtbBOJAhaBieBqxw' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'ONLYsupfov' 
WHERE 
  puuid = 'zRxTBQ0yB7rIs8QagWunbcbrF17cqWEMDxMVomHDSnkuSg7dtZxFhTQSPFtHmxQRTXTnUaTe0uV1Lg' 
UPDATE 
  aram_games.dbo.aram_data 
SET 
  riotIdGameName = 'RuuunJerry' 
WHERE 
  puuid = 'F3t5UuTtKFnnvrB_PsCA3ke8r2JHhCZdwuL4whR5GjX4G4kcyK7bmgT3i3SiJw9XIXqHs9WccmrgVw'

```

