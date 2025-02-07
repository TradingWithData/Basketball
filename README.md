# Basketball

*This is a work in progress*

Basketball analysis and data collection through the NBA api.

This is a personal project with the intention to regularly collect new basketball games through the NBA website and run calculations to predict points scored and winning teams. The current dataset is incomplete which I believe is an issue with the size of the requests being made. Once the dataset is fully collected efforts in cleaning the data will be made. The current limitations pulls data from all of history from Basketball, these results will be filted down by active players. There are some rows that have multiple results for years a player played based on team transfers. There is a summary row underneath the sums up stats for the total year for both teams that will need to be filtered out.

The following packages are required to run the code:

**Python**
- nba_api - interacts with the NBA API, see link for API documentation (https://nba-apidocumentation.knowledgeowl.com/help)
- pandas  - manipulate data frames
- openpyxl - package to read/write Excel files

**Issues**
- Read timed out error - this is possibly due to the size of the data request
- Incomplete data - a master list will need to be created and stored effectively so new data can be added without pulling all previous data
- Data is not currently cleaned or filtered

**Future Plans**
- Automate the data collection script to regularly
- Extend the analysis
    - Goal is to have a complex analysis derived from many different variables and comparing results to Vegas odds
- Create a script that regularly cleans the new incoming data


Analysis on Kaggle:
https://www.kaggle.com/code/anonbball/basketball-api-probablities
