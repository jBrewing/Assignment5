#
#_commit______________________________________
#
# Assignment 5 - Using Python to Retreive and Visualize Data
# Created by: Joseph Brewer
# FOR: CEE6110 - Hydroinformatics - Horsburgh
# DUE: 11/6/2018
# Description: This script will present a comparison of monthly
# water temperature data on a yearly basis for the Logan River ODM database
# for the month of September.  Site selection input will be a feature.
#____________________________________________




# 1. Import packages
#   - connecting to sql server
import sqlite3
#   - making plots
import matplotlib.pyplot as plt
#   - performing stats
import pandas as pd



# 3. Receive input
# Thoroughly describe input format.
siteID = input('\n\nPlease input the SiteID to be analyzed.\n\n '
               'Options are: \n'
               ' \tSite 1\n'
               ' \tSite 2\n'
               ' \tSite 3\n'
               ' \tSite 9. \n\n'
               'Please input as "1", "2", "3," etc:  ')



# 4. Query database
# a. establish connection with database. Filepath not necessary as
#  database is in same directory.
conn = sqlite3.connect('Logan_River_Temperature_ODM.sqlite')

# b. build query
# query all data values for SiteId = X
sql_statement = 'SELECT LocalDateTime, DataValue  ' \
                'FROM datavalues ' \
                'WHERE VariableID = 1 AND SiteID = ' + siteID + ' AND DataValue <> -9999 ' \
                'AND QualityControlLevelID = 1'

# c. execute query with cursor object and fetch all
#  query results with .fetchall()
cursor = conn.cursor()
cursor.execute(sql_statement)
rows = cursor.fetchall()



# 5. Transform data into usable lists
# a. transfer from lists to indexed dataframe
# pull all data and use zip to transform query data into rows
LocalDateTime, DataValue = zip(*rows)

# load 'LocalDateTime' & 'DataValue' into overall pandas dataframe
# with column titles "Date" and "Temp"
data_df = pd.DataFrame({'Date': LocalDateTime, 'Temp':DataValue})

# Duplicate "Date" column
data_df['index'] = data_df['Date']

# Convert "Date" column to datetime format with pandas function
data_df['Date'] = pd.to_datetime(data_df['Date'], infer_datetime_format=True)

# Set data frame index for slicing using duplicated "Date" column
data_df = data_df.set_index('index')


# 6. Slice september data out of all yearly blocks in over all data frame
df_2014 = data_df['2014-09-01 00:00:00':'2014-09-30 23:59:59']
df_2015 = data_df['2015-09-01 00:00:00':'2015-09-30 23:59:59']
df_2016 = data_df['2016-09-01 00:00:00':'2016-09-30 23:59:59']
df_2017 = data_df['2017-09-01 00:00:00':'2017-09-30 23:59:59']

# Convert date format so values will plot over each other.
df_2014['Date'] = df_2014['Date'].dt.strftime('%m-%d')
df_2015['Date'] = df_2015['Date'].dt.strftime('%m-%d')
df_2016['Date'] = df_2016['Date'].dt.strftime('%m-%d')
df_2017['Date'] = df_2017['Date'].dt.strftime('%m-%d')


# 7. Plot results
# Set colors, graph type, marker type, limits, and label
# 2014 data
df_2014.plot('Date', 'Temp',color ='green',kind='line',
             linestyle='solid', markersize=0, ylim=[4, 22],
             marker = 'o', label='2014')
ax = plt.gca()
ax.set_ylabel('Temp (C)')
ax.set_xlabel('Date/Time [Septembet 1-30]')
plt.title('Site ' + siteID + ': September 2014')
ax.grid(True)

# 2015 data
df_2015.plot('Date', 'Temp',color='red',kind='line',
             linestyle='solid', markersize=0,ylim=[4, 22],
             marker = 'o', label='2015')
ax = plt.gca()
ax.set_ylabel('Temp (C)')
ax.set_xlabel('Date/Time[Septembet 1-30]')
plt.title('Site ' + siteID + ': September 2015')
ax.grid(True)

# 2016 data
df_2016.plot('Date', 'Temp',color='blue',kind='line',
             linestyle='solid', markersize=0, ylim=[4, 22],
             marker = 'o', label='2016')
ax = plt.gca()
ax.set_ylabel('Temp (C)')
ax.set_xlabel('Date/Time[Septembet 1-30]')
plt.title('Site ' + siteID + ': September 2016')
ax.grid(True)

# 2017 data
df_2017.plot('Date', 'Temp',color='black',kind='line',
             linestyle='solid', markersize=0, ylim=[4, 22],
             marker = 'o', label='2017')
ax = plt.gca()
ax.set_ylabel('Temp (C)')
ax.set_xlabel('Date/Time[Septembet 1-30]')
plt.title('Site ' + siteID + ': September 2017')
ax.grid(True)

plt.show()



print('Done!')












