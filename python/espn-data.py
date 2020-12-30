import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Table Data
player_names = []
pass_stats = []
teams_list = []
stand_list = []
pass_cols = []
injury_list = []
injury_team = []

# HTML Table Vars
defense_table = ''
stat_table = ''
stat_table2 = ''
headers = ''
standings = ''
teams = ''

# Team standings split lists
t_list1 = []
t_list2 = []

# Scrapping ESPN NFL Passing statistics from espn_url.
# Scrapping all table elements and storing into managable Data Structures.
def scrapeEspnPass():
    espn_url = 'https://www.espn.com/nfl/stats/player/_/view/offense/table/passing/sort/passingYards/dir/desc'
    response = requests.get(espn_url)
    #bs4 object creation
    soup = BeautifulSoup(response.content, 'html.parser')

    #find table elements in ESPN
    stat_table = soup.find_all('table', class_ = 'Table Table--align-right')
    stat_table2 = soup.find_all('table', class_ = 'Table Table--align-right Table--fixed Table--fixed-left')
    headers = soup.find_all('table', class_ = 'Table Table--align-right')
   
    stat_table = stat_table[0]
    stat_table2 = stat_table2[0]
    headers = headers[0]

    #create lists with data
    for row in stat_table2.find_all('tr')[1:]:
        for cell in row.find_all('td'):
            player_names.append(cell.text)
    
    for row in stat_table.find_all('tr')[1:]:
        for cell in row.find_all('td'):
            pass_stats.append(cell.text)
    
    for row in headers.find_all('tr')[0:]:
        for cell in row.find_all('th'):
            pass_cols.append(cell.text)

# Scrapping ESPN NFL Standings statistics from espn_url.
# Scrapping all table elements and storing into managable Data Structures.
def scrapeEspnStandings():
    espn_url = 'https://www.espn.com/nfl/standings'
    response = requests.get(espn_url)
    # bs4 object creation
    soup = BeautifulSoup(response.content, 'html.parser')
    standings = soup.find(class_="tabs__content")
    
    for row in standings.find_all('tr')[0:]:
        for cell in row.find_all('td'):
            stand_list.append(cell.text)
  
    # Retrieving team names from dataset
    for x in stand_list[0:20]:
        t_list1.append(x)
    for x in stand_list[260:280]:
        t_list2.append(x)

    # Delete team names after extraction
    # Result is only standings stats
    del stand_list[0:20]
    del stand_list[240:260]

# Scrapping ESPN NFL Injury Table from espn_url.
# Scrapping all table elements and storing into managable Data Structures.
def scrapeEspnInjuries():
    espn_url = 'https://www.espn.com/nfl/injuries'
    response = requests.get(espn_url)
    #bs4 object creation
    soup = BeautifulSoup(response.content, 'html.parser')
    injury_table = soup.find(class_="Wrapper Card__Content")
    teams_with_injuries = soup.find(class_='Wrapper Card__Content')

    for row in injury_table.find_all('tr')[0:]:
        for cell in row.find_all('td'):
            injury_list.append(cell.text)

# Method used to remove non-alpha characters from scrapped Data  
def convertListToAlpha(list):
    words = []
    for x in list:
        if not x.isdigit():
            words.append(str(x))
    return words

# Method used to split lists with desired length
def split_list(list, size):
    for i in range(0, len(list), size):
        yield list[i:i + size]

# Transferring all parsed/cleaned data with Dataframes to excel files
# All Arrays/lists containing Data loaded into DF's.
def transferData():
    #call conversion methods and assign to variables
    name = convertListToAlpha(player_names)

    
    # Seperating/Splitting scrapped HTML data that was appended into a list for easier manipulation.
    # Passing and Standing stats are stored in lists. Lists are then divided into sublists at specfic
    # points before creating dataframe.
    split_pass_stats = []
    split_pass_stats = list(split_list(pass_stats, 15))

    split_standing_list = []
    split_standing_list = list(split_list(stand_list, 12))

    split_injury_list = []
    split_injury_list = list(split_list(injury_list, 5))
    
    # Create headers for standings list
    s_headers = []
    s_headers = split_standing_list[0]

    # Merge team lists
    teams_list = t_list1 + t_list2

    # Removing duplicate headers from standings table
    remove_index = [0,5,10,15,20,25,30,35]
    remove_index2 = [0,5,10,15,20,25,30,35]

    for index in sorted(remove_index, reverse=True):
        del split_standing_list[index]

    for index in sorted(remove_index2, reverse=True):
        del teams_list[index]

    
    # Loadeing all Data into Dataframes and dumping into excel files/sheets
    dataToExcel = pd.ExcelWriter("YOUR PATH/NFL_Stats.xlsx", engine='xlsxwriter')
    # Passing list of names as index
    data1 = pd.DataFrame(split_pass_stats, index=name)
    # Passing list of headers as columns
    data1.columns = pass_cols
    data1.index.names = ['QBName']
    data1.to_excel(dataToExcel, sheet_name='Passing')

    # Passing list of team names as index
    data2 = pd.DataFrame(split_standing_list, index=teams_list)
    data2.columns = s_headers
    data2.index.names = ['Teams']
    data2.to_excel(dataToExcel, sheet_name='Standings')
    
    # Passing injury list
    data3 = pd.DataFrame(split_injury_list)
    data3.columns = ['Name', 'POS', 'DATE', 'STATUS', 'COMMENTS']
    data3.to_excel(dataToExcel, sheet_name='Injuries')

    dataToExcel.save()

def main():
    # Invoke all Methods
    scrapeEspnPass()
    scrapeEspnStandings()
    scrapeEspnInjuries()
    transferData()

    print('---------------Webscrapping Complete--------------')

#call MAIN
main()


