-------------------------------------------------------------
      Player Performance Profile: Analyzing Gameplay Trends and Strategies
-------------------------------------------------------------
```sql
select *
from aram_data
where summonerName = 'Qrownin'
```

```sql
-- inital partition by statement
-- discovered that aliases can not be used to calculate in select statement unless it is used in a subquery
-- the second sql statement is the same output but is different without partition and subquery
SELECT 
  DISTINCT championName, 
  games_played, 
  total_kills, 
  total_deaths, 
  total_assists, 
  CASE WHEN total_deaths = 0 THEN 0 ELSE (total_kills + total_assists) / total_deaths END AS kda 
FROM 
  (
    SELECT 
      championName, 
      COUNT(*) OVER (PARTITION BY championName) AS games_played, 
      SUM(kills) OVER (PARTITION BY championName) AS total_kills, 
      SUM(deaths) OVER (PARTITION BY championName) AS total_deaths, 
      SUM(assists) OVER (PARTITION BY championName) AS total_assists 
    FROM 
      aram_data 
    WHERE 
      summonerName = 'Qrownin'
  ) AS subquery 
ORDER BY 
  kda DESC, 
  games_played DESC, 
  championName;

```
```sql
-- overall stats
SELECT 
  championName, 
  COUNT(*) AS games_played, 
  SUM(kills) AS total_kills, 
  SUM(deaths) AS total_deaths, 
  SUM(assists) AS total_assists, 
  CASE WHEN AVG(deaths) = 0 THEN 0 ELSE (
    AVG(kills) + AVG(assists)
  ) / AVG(deaths) END AS avg_kda, 
  CASE WHEN SUM(kills) > SUM(deaths) THEN 'True' WHEN SUM(kills) = SUM(deaths) THEN 'Neutral' ELSE 'False' END AS positive_kd, 
  MAX(killingSprees) AS Killing_spree, 
  MAX(kills) AS highest_kill_game, 
  MIN(kills) AS lowest_kill_game, 
  MAX(deaths) AS highest_death_game, 
  MIN(deaths) AS lowest_death_game, 
  SUM(totalDamageDealtToChampions) AS overall_dmg, 
  AVG(totalDamageDealtToChampions) AS avg_dmg, 
  AVG(goldEarned) AS avg_gold, 
  AVG(longestTimeSpentLiving) AS time_alive_seconds, 
  AVG(timeCCingOthers) AS avg_cc_seconds, 
  AVG(totalTimeCCDealt) AS avg_cc_time_seconds, 
  AVG(timePlayed) / 60 AS avg_game_time_minutes, 
  AVG(totalTimeSpentDead) AS avg_time_dead_seconds, 
  AVG(totalMinionsKilled) AS avg_minions, 
  SUM(
    CASE WHEN doubleKills > 0 THEN 1 ELSE 0 END
  ) AS double_kills, 
  SUM(
    CASE WHEN tripleKills > 0 THEN 1 ELSE 0 END
  ) AS triple_kills, 
  SUM(
    CASE WHEN quadraKills > 0 THEN 1 ELSE 0 END
  ) AS quadra_kills, 
  SUM(
    CASE WHEN pentaKills > 0 THEN 1 ELSE 0 END
  ) AS penta_kills, 
  SUM(CASE WHEN win > 0 THEN 1 ELSE 0 END) AS wins, 
  CONCAT(
    CAST(
      CASE WHEN COUNT(*) > 0 THEN (
        SUM(CASE WHEN win > 0 THEN 1 ELSE 0 END) * 100
      ) / COUNT(*) ELSE 0 END AS INT
    ), 
    '%'
  ) AS win_rate, 
  CASE WHEN (
    SUM(totalDamageDealtToChampions) / NULLIF(
      (
        SUM(kills) + SUM(assists)
      ), 
      0
    )
  ) IS NULL THEN 0 ELSE (
    SUM(totalDamageDealtToChampions) / NULLIF(
      (
        SUM(kills) + SUM(assists)
      ), 
      0
    )
  ) END AS avg_damage_per_kill_and_assist 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  summonerName = 'Qrownin' 
GROUP BY 
  championName 
ORDER BY 
  games_played DESC, 
  championName;

```
```sql
-- look into best average champion with 2 or more games
SELECT 
  championName, 
  COUNT(*) AS games_played, 
  SUM(kills) AS total_kills, 
  SUM(deaths) AS total_deaths, 
  SUM(assists) AS total_assists, 
  CASE WHEN AVG(deaths) = 0 THEN 0 ELSE (
    AVG(kills) + AVG(assists)
  ) / AVG(deaths) END AS avg_kda, 
  CASE WHEN SUM(kills) > SUM(deaths) THEN 'True' WHEN SUM(kills) = SUM(deaths) THEN 'Neutral' ELSE 'False' END AS positive_kd, 
  MAX(killingSprees) AS Killing_spree, 
  MAX(kills) AS highest_kill_game, 
  MIN(kills) AS lowest_kill_game, 
  MAX(deaths) AS highest_death_game, 
  MIN(deaths) AS lowest_death_game, 
  SUM(totalDamageDealtToChampions) AS overall_dmg, 
  AVG(totalDamageDealtToChampions) AS avg_dmg, 
  AVG(goldEarned) AS avg_gold, 
  AVG(longestTimeSpentLiving) AS time_alive_seconds, 
  AVG(timeCCingOthers) AS avg_cc_seconds, 
  AVG(totalTimeCCDealt) AS avg_cc_time_seconds, 
  AVG(timePlayed) / 60 AS avg_game_time_minutes, 
  AVG(totalTimeSpentDead) AS avg_time_dead_seconds, 
  AVG(totalMinionsKilled) AS avg_minions, 
  SUM(
    CASE WHEN doubleKills > 0 THEN 1 ELSE 0 END
  ) AS double_kills, 
  SUM(
    CASE WHEN tripleKills > 0 THEN 1 ELSE 0 END
  ) AS triple_kills, 
  SUM(
    CASE WHEN quadraKills > 0 THEN 1 ELSE 0 END
  ) AS quadra_kills, 
  SUM(
    CASE WHEN pentaKills > 0 THEN 1 ELSE 0 END
  ) AS penta_kills, 
  SUM(CASE WHEN win > 0 THEN 1 ELSE 0 END) AS wins, 
  CONCAT(
    CAST(
      CASE WHEN COUNT(*) > 0 THEN (
        SUM(CASE WHEN win > 0 THEN 1 ELSE 0 END) * 100
      ) / COUNT(*) ELSE 0 END AS INT
    ), 
    '%'
  ) AS win_rate, 
  CASE WHEN (
    SUM(totalDamageDealtToChampions) / NULLIF(
      (
        SUM(kills) + SUM(assists)
      ), 
      0
    )
  ) IS NULL THEN 0 ELSE (
    SUM(totalDamageDealtToChampions) / NULLIF(
      (
        SUM(kills) + SUM(assists)
      ), 
      0
    )
  ) END AS avg_damage_per_kill_and_assist 
FROM 
  aram_games.dbo.aram_data 
WHERE 
  summonerName = 'Qrownin' 
GROUP BY 
  championName 
HAVING 
  count(*) >= 2 
ORDER BY 
  avg_damage_per_kill_and_assist DESC, 
  win_rate, 
  avg_dmg DESC, 
  positive_kd

```
