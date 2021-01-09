# ESPN NFL Data Analysis
Repo for Webscrapping and Data Analysis for ESPN/NFL stats


- Webscraping(Python Beautiful Soup Package) program to parse HTML structures.
- Extracted various tables while also transferring DataFrames to Excel worksheets for analysis. 
- Specialized SQL Queries are also integrated into this Python program to retrieve unique and customized NFL statistics from Excel.
- Produced Data visualizations using Matplotlib python library.

### *Code executed after NFL sunday, MNF, TNF*

  - **[x] Current QB stats**
  - **[x] QB negatives (Sacks/Interceptions)**
  - **[x] Current Team standings**
  - **[x] NFL worst team/s**
  - **[x] Injuries**
  
 # Code & Resources 
 #### Python Version: 3.7
 #### Packages: pandas, BeautifulSoup, matplotlib
  
 # Web Scrapping Process:
  - Data structures utilized to manually scrape target HTML tables.
  - QB attributes scrapped from passing tables
    - *QBName|POS|GP|CMP|ATT|CMP%|YDS|AVG|YDS/G|LNG|TD|INT|SACK|SYL|QBR|RTG*
  - Injury attrbutes scrapped from injury tables
    - *Name|POS|DATE|COMMENTS*
  - Standing attributes scrapped from standings tables
    - *Teams|W|L|T|PCT|HOME|AWAY|DIV|CONF|PF|PA|DIFF|STRK*
   
 # SQL Queries: 
 #### Multiple sub tables were generated from scrapped website data using queries
  - Query results packed into seperate DataFrames and dumped into Excel files.
  - Built-In Python sqlite3 for fast temporary data Filtering/Extraction
  
# Excel and Dataframes:Data Storage/Results
  - **NFL_Stats.xlsx** contains all scrapped HTML tables from ESPN URL.
    - **Sheets:** Passing, Standings, Injuries 
  - **NFL_Query.xlsx** This file contains all SQL Queries from **sql_espn.py**.Sub-Tables generated for in depth filtering or Analysis.
    - **Sheets:** Current-Stats(Copy of original Data), Negatives,Current-Standings, NFL-Worst, Injuries

# DATA VISUALIZATION: 
#### *This Process Automatically Saves Data Visuals After Execution*
## Data Visual #1: Demonstrates Touchdowns/Sacks completed by each Quarterback
![](https://raw.githubusercontent.com/Adan-Macias/espn_nfl_stats/main/Data_Visuals/TD_SACK.png)

## Data Visual #2: Amount of Touchdowns completed along with Interceptions.
![](https://raw.githubusercontent.com/Adan-Macias/espn_nfl_stats/main/Data_Visuals/TD-INT.png)

## Data Visual #3: Displays and Compares CMP% and QBR.
![](https://raw.githubusercontent.com/Adan-Macias/espn_nfl_stats/main/Data_Visuals/QBR-CMP.png)
