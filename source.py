#
#_____________________________________________________
#
# Assignment 5 - Using Python to Retreive and Visualize Data
# Created by: Joseph Brewer
# FOR: CEE6110 - Hydroinformatics - Horsburgh
# DUE: 11/6/2018
# Description: This script will present a comparison of monthly
# water temperature data on a yearly basis for the Logan River ODM database
# for the month of September.  Site selection input will be a feature.
#____________________________________________


#PseudoCode

# 1. Import packages
#   - connecting to sql server  -> sqlite3
import sqlite3
#   - to pull datetimes         -> datetime
import datetime
#   - making plots              -> matplotlib.pyplot as plt
import matplotlib.pyplot as plt
#   - performing stats          -> pandas as pd
import pandas as pd
#______________________




# 3. Receive input
#   - variables:
#       1. site ID
siteID = input('Please input the SiteID to be analyzed: ')
#       2. monthID
#yearID = input('Please select the year to be analyzed: ')
#       3. yearID
#month = input('Please select the month to be displayed: ')
#______________________


# 4. Query database
#    a. establish connection
conn = sqlite3.connect('Logan_River_Temperature_ODM.sqlite')

#   b. build query
#   - query all data values for SiteId = ?          (do filtering in pandas dataframe)
sql_statement = 'SELECT LocalDateTime, DataValue  ' \
                'FROM datavalues ' \
                'WHERE VariableID = 1 AND SiteID = ' + siteID + ' AND DataValue <> -9999 ' \
                'AND QualityControlLevelID = 1'

#    c. execute query
cursor = conn.cursor()
cursor.execute(sql_statement)
rows = cursor.fetchall()



# 5. Transform data into usable lists
#   a. transfer from lists to indexed dataframe
# pull all data
# use zip to transform query data into rows1
LocalDateTime, DataValue = zip(*rows)
# load into overall pandas dataframe
data_df = pd.DataFrame({'Date': LocalDateTime, 'Temp':DataValue})
# Duplicate date column
data_df['index'] = data_df['Date']
# Convert date column to datetime
data_df['Date'] = pd.to_datetime(data_df['Date'], infer_datetime_format=True)
# Set index for slicing
data_df = data_df.set_index('index')

# 6. Slice months out of all yearly blocks
df_2014 = data_df['2014-09-01 00:00:00':'2014-09-30 23:59:59']
df_2015 = data_df['2015-09-01 00:00:00':'2015-09-30 23:59:59']
df_2016 = data_df['2016-09-01 00:00:00':'2016-09-30 23:59:59']
df_2017 = data_df['2017-09-01 00:00:00':'2017-09-30 23:59:59']

# Convert date format so values will plot over each other.
df_2014['Date'] = df_2014['Date'].dt.strftime('%m-%d')
df_2015['Date'] = df_2015['Date'].dt.strftime('%m-%d')
df_2016['Date'] = df_2016['Date'].dt.strftime('%m-%d')
df_2017['Date'] = df_2017['Date'].dt.strftime('%m-%d')

#fig, ax = plt.subplots(2,2)
#plt.subplot(2,2,1)
df_2014.plot('Date', 'Temp',kind='line',
       linestyle='solid', markersize=0,
           label='Water Temp')
#Set the x and y-axis labels
ax = plt.gca()
ax.set_ylabel('Temp (C)')
ax.set_xlabel('Date/Time')
ax.grid(True)


# 7. Generate plot
#fig, ax = plt.subplots(2,2)

#plt.subplot(2,2,1)
#plt.plot(df_2014['Date'],df_2014['Temp'])

#plt.subplot(2,2,2)
#plt.plot(df_2015['Date'],df_2014['Temp'])

#plt.subplot(2,2,3)
#plt.plot(df_2016['Date'],df_2014['Temp'])

#plt.subplot(2,2,4)
#plt.plot(df_2017['Date'],df_2014['Temp'])


#data_df.plot('Date', 'Temp',kind='line',
#         linestyle='solid', markersize=0,
#            label='Water Temp')
#Set the x and y-axis labels
#ax = plt.gca()
#ax.set_ylabel('Temp (C)')
#ax.set_xlabel('Date/Time')
#ax.grid(True)





plt.show()












print('havent burst into flmame yet')