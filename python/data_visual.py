import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#input file
raw_data = pd.read_excel('YOUR PATH/NFL_Query.xlsx')

# Filters
filter1 = raw_data[(raw_data.TD >= 0)]
filter1 = filter1.sort_values(by=['TD'])

#Data Visual #1
plt.rcParams["figure.figsize"] = [20,22]
filter1.reset_index().plot(y=['TD', 'SACK'],x='QBName', kind='barh', stacked=False, width=0.7, color=['teal', 'firebrick'])
plt.grid(color='black', linestyle='--', linewidth=.4, axis='x', alpha=0.8)
plt.title('Number Of Touchdowns Per (QB)', fontsize=15)
plt.ylabel('Quarterback', fontsize=14)
plt.xlabel('Touchdowns', fontsize=14)
x_ticks = np.arange(0, 60, 2)
plt.xticks(x_ticks)
plt.tick_params(axis='y', which='major', labelsize=12)
plt.tick_params(axis='x', which='major', labelsize=12)
plt.margins(y=0)
plt.legend(fontsize=12)
plt.savefig('YOUR PATH/TD-SACK.png', bbox_inches='tight')

#Data Visual #2
plt.figure(figsize=[10,5.5])
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
plt.savefig('YOUR PATH/QBR-CMP.png', bbox_inches='tight')

##Data Visual #3
plt.rcParams["figure.figsize"] = [20,8]
filter1.reset_index().plot(y=['TD', 'INT'],x='QBName', kind='bar', stacked=False, width=0.8, color=['blue', 'firebrick'])
plt.grid(color='black', linestyle='--', linewidth=.4, axis='y', alpha=0.7)
plt.title('Touchdown vs Interception Comparison',fontsize=15)
plt.ylabel('Touchdowns/Intrceptions', fontsize=12)
plt.xlabel('Quarterback ', fontsize=12)
y_ticks = np.arange(0, 50, 2)
plt.yticks(y_ticks)
plt.tick_params(axis='x', which='major', labelsize=10)
plt.tick_params(axis='y', which='major', labelsize=10)
plt.legend(fontsize=12)
plt.margins(x=0)
plt.savefig('YOUR PATH/TD_INT.png', bbox_inches='tight')

print('------------Data Visuals Created----------')
