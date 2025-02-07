from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd
import time  # To avoid rate limits

# range for looped season years
seasons = [
    '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', 
    '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# create the list to store
all_seasons_data = []

# Loop through each season to get team stats
for season in seasons:
    print(f"Fetching data for season: {season}")
    
    team_stats = leaguedashteamstats.LeagueDashTeamStats(season=season)
    
    # Converts to data frame
    df = team_stats.get_data_frames()[0]
    df["SEASON"] = season  # Adds a column to track season

    all_seasons_data.append(df)
    
    # Brief pause on api call time
    time.sleep(1)

# Combine all data into one
final_df = pd.concat(all_seasons_data, ignore_index=True)

# Display header rows as visual queue
print(final_df.head())

# Save to a CSV file
final_df.to_csv("nba_team_stats_2010_2025.csv", index=False)
