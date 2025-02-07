import time
import concurrent.futures
from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.endpoints import leaguegamefinder 
import pandas as pd

start_time = time.time()

# Years of the seasons to pull
seasons = [
    #'2015-16', '2016-17', '2017-18', '2018-19', '2019-20', 
    #'2020-21', '2021-22', '2022-23', '2023-24', 
    '2024-25'
]

all_games = []  # Holds data frames for each season

for season in seasons:
    print(f"Querying Regular Season games for {season}...")
    # Query regular season games in the season
    gamefinder_reg = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable='Regular Season'
    )
    df_reg = gamefinder_reg.get_data_frames()[0]
    all_games.append(df_reg)
    
    # Brief pause on api call time - may need to extend time due to read timed out errors
    time.sleep(1)
    
    print(f"Querying Playoff games for {season}...")
    # Query playoff games for the season
    gamefinder_po = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable='Playoffs'
    )
    df_po = gamefinder_po.get_data_frames()[0]
    all_games.append(df_po)
    
    # Brief pause on api call time - may need to extend time due to read timed out errors
    time.sleep(1)

# Combine all the season DataFrames into one
all_games_df = pd.concat(all_games, ignore_index=True)

# Save the results to a CSV file
output_filename = "nba_games_last_10_years.csv"
all_games_df.to_csv(output_filename, index=False)

print(f"All game data for the last ten seasons has been saved to {output_filename}")




# Read the CSV file - file should contain game ID's
games_df = pd.read_csv("nba_games_last_10_years.csv")

# Unique game ID's for the loop - this is the argument that gets passed through the statement
unique_game_ids = games_df["GAME_ID"].unique()
print(f"Found {len(unique_game_ids)} unique game IDs.")

# Loop through each game ID
combined_boxscores = pd.DataFrame()  # This will hold all the box score data

for game_id in unique_game_ids:
    print(f"Processing game ID: {game_id}")
    try:
        # Data integrity - Checking string length is 10 digits long, if output file is opened and saved, it could delete leading 0's
        game_id_str = str(game_id).zfill(10)
        
        # Call the endpoint with required parameters
        boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(
            game_id=game_id_str,
            start_period=1,
            end_period=4,
            start_range=0,
            end_range=0,
            range_type=0
        )
        

        game_boxscore = boxscore.get_data_frames()[0]
        
        # (Optional) Add a column for the game ID if not already present
        if "GAME_ID" not in game_boxscore.columns:
            game_boxscore["GAME_ID"] = game_id_str
        
        # Append the result to our combined DataFrame
        combined_boxscores = pd.concat([combined_boxscores, game_boxscore], ignore_index=True)
        
        # Brief pause on api call time - may need to extend time due to read timed out errors
        time.sleep(1)

    # e assigns the error message as a variable, using the f-string displays a dynamic error message - Not necessary but helpful for debugging
    except Exception as e:
        print(f"Error processing game {game_id}: {e}")

# Output as an Excel file
output_filename = "combined_boxscores.xlsx"
combined_boxscores.to_excel(output_filename, index=False)

print(f"Combined box score data saved to {output_filename}")




# Tracking total processing time of code
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")
