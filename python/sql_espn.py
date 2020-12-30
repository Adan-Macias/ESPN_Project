import sqlite3
import pandas as pd
from sqlalchemy import create_engine


# INPUT file to query
file = "YOUR PATH/NFL_Stats.xlsx"
# OUTPUT file of desired queries
output = pd.ExcelWriter("YOUR PATH/NFL_Query.xlsx", engine='xlsxwriter')

# Creating sql engine to use SQL/reading Excel sheets
engine = create_engine('sqlite://', echo=False)
df = pd.read_excel(file, sheet_name='Passing')
df2 = pd.read_excel(file, sheet_name='Standings')
df3 = pd.read_excel(file, sheet_name='Injuries')

# Creating Tables to extract data
df.to_sql('Players', engine, if_exists='replace', index=False)
df2.to_sql('Standings', engine, if_exists='replace', index=False)
df3.to_sql('Injuries', engine, if_exists='replace', index=False)

# Query1 - Data queried for QBR and CMP% data visual
q1 = engine.execute("Select * FROM Players \
                     ORDER BY QBR, [CMP%] ASC \
                     ")
data1 = pd.DataFrame(q1, columns = df.columns)
data1.to_excel(output, sheet_name='Current-Stats', index=False)

# Query2 - QB negative stats
q2 = engine.execute("Select QBName, SACK, INT \
                     From Players \
                     ORDER BY SACK DESC, INT DESC")
data2 = pd.DataFrame(q2, columns = ['QBName', 'SACK', 'INT'])
data2.to_excel(output, sheet_name='Negatives', index=False)

# Query3 - Update current standings for (SNF, MNF, TNF)
q3 = engine.execute("Select Teams, W, L, PCT, PF \
                     From Standings\
                     ORDER BY W DESC")
data3 = pd.DataFrame(q3, columns = ['Teams', 'W', 'L', 'PCT', 'PF'])
data3.to_excel(output, sheet_name='Current-Standings', index=False)

# Query4 - Track worst Teams in the NFL based on wins < 50%
q4 = engine.execute("Select Teams, W , L,  T, PCT \
                     FROM Standings\
                     WHERE W <= '7' \
                     ORDER BY Teams ASC, W ASC ")
data4 = pd.DataFrame(q4, columns = ['Teams', 'W', 'L', 'T', 'PCT'])
data4.to_excel(output, sheet_name='NFL-Worst', index=False)

# Query5 - NFL Athletes who are out with injuries
q5 = engine.execute("Select Name, STATUS , COMMENTS \
                     FROM Injuries \
                     WHERE STATUS = 'Out'\
                     ORDER BY Name ASC")
data5 = pd.DataFrame(q5, columns = ['Name', 'STATUS', 'COMMENTS'])
data5.to_excel(output, sheet_name='Injuries', index=False)

output.save()

print('-------------NFL Query sheets created--------------')




