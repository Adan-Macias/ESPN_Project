import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#input file
raw_data = pd.read_excel('C:/Users/melen/Desktop/PORTFOLIO/ESPN_Project/Data/NFL_Query.xlsx')

# Filters
filter1 = raw_data[(raw_data.SACK >= 0)]
filter1 = filter1.sort_values(by=['SACK'])

filter2 = raw_data[(raw_data.TD >= 0)]
filter2 = filter2.sort_values(by=['TD'])

#Data Visual #1
plt.figure(1, figsize=[13,8])
plt.barh(filter2.QBName,filter2.TD, color='green', height=.8, label='TD')
plt.grid(color='black', linestyle='--', linewidth=.4, axis='x', alpha=0.7)
plt.title('Number Of Touchdowns Per (QB)')
plt.ylabel('Quarterback')
plt.xlabel('Touchdowns')
x_ticks = np.arange(0, 60, 2)
plt.xticks(x_ticks)
plt.tick_params(axis='y', which='major', labelsize=7)
plt.legend()
plt.margins(y=0)
plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/ESPN_Project/Data_Visuals/TD.png', bbox_inches='tight')

#Data Visual #2
plt.figure(2, figsize=[11.5,7])
plt.bar(filter1.QBName,filter1.SACK, color='red', label='Sacks')
plt.grid(color='black', linestyle='--', linewidth=.4, axis='y', alpha=0.7)
plt.title('Number Of Sacks Per (QB)')
plt.ylabel('Sacks')
plt.xlabel('Quarterback')
y_ticks = np.arange(0, 60, 2)
plt.yticks(y_ticks)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.xticks(raw_data.QBName, rotation=90)
plt.legend()
plt.margins(x=0)
plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/ESPN_Project/Data_Visuals/sacks.png', bbox_inches='tight')

#Data Visual #3
plt.figure(3, figsize=[10,5.5])
plt.title("QB Rating")
plt.plot(raw_data.QBName, raw_data.QBR, marker='.', markersize='6', color='green',
    markeredgecolor='black', markerfacecolor='black', linewidth='2', label='QBR')
    
plt.plot(raw_data.QBName, raw_data['CMP%'], marker='+', markersize='6', 
    color='red', markeredgecolor='black', markeredgewidth=1, linewidth='2', label='CMP%')

plt.grid(color='grey', linestyle='--', linewidth=.4, axis='x', alpha=0.7)
plt.grid(color='grey', linestyle='--', linewidth=.4, axis='y', alpha=0.7)

plt.title('CMP% & QBR Comparisons Per (QB)')
plt.ylabel('CMP%/QBR')
plt.xlabel('Quarterback')
plt.xticks(raw_data.QBName, rotation=90)
y_ticks = np.arange(0, 90, 5)
plt.yticks(y_ticks)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.legend()
plt.margins(x=0)
plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/ESPN_Project/Data_Visuals/QBR-CMP.png', bbox_inches='tight')

##Data Visual #4
raw_data = raw_data.sort_values(by=['TD','INT'])
plt.figure(4, figsize=[10,5.5])
plt.bar(raw_data.QBName,raw_data.TD, color='blue', label='TD', bottom=raw_data.INT)
plt.bar(raw_data.QBName,raw_data.INT, color='red', label='INT')
plt.grid(color='black', linestyle='--', linewidth=.4, axis='y', alpha=0.7)
plt.title('Touchdown vs Interception Comparison')
plt.ylabel('Touchdowns/Intrceptions')
plt.xlabel('Quarterback ')
y_ticks = np.arange(0, 50, 3)
plt.yticks(y_ticks)
plt.tick_params(axis='x', which='major', labelsize=7)
plt.xticks(raw_data.QBName, rotation=90)
plt.legend()
plt.margins(x=0)
plt.savefig('C:/Users/melen/Desktop/PORTFOLIO/ESPN_Project/Data_Visuals/TD-INT.png', bbox_inches='tight')



print('------------Data Visuals Created----------')