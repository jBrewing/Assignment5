#
#_____________________________________________________
#
# Assignment 5 - Using Python to Retreive and Visualize Data
# Created by: Joseph Brewer
# FOR: CEE6110 - Hydroinformatics - Horsburgh
# DUE: 11/6/2018
# Description: This script will present a month by month
# water temperature summary from the Logan River ODM database,
# complete with a 4 pane plot describing and
# illustrating a variety of statistics for the selected site and month.
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





# 2. Receive input
#   - variables:
#       1. site ID
siteID = input('Please input the SiteID to be analyzed: ')
#       2. monthID
yearID = input('Please select the year to be analyzed: ')
#       3. yearID
monthID = input('Please select the month to be displayed: ')
#______________________


# 3. Query database
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
#______________________


# 4. Transform data into usable lists
#   a. transfer from lists to indexed dataframe
#   -> pull all data
#   -> use zip to transform query data into rows1
LocalDateTime, DataValue = zip(*rows)
#   -> load into overall pandas dataframe
data_df = pd.DataFrame({'Date': LocalDateTime, 'Temp':DataValue})
# Duplicate date column
# Convert date column to datetime
data_df['index'] = data_df['Date']
data_df['Date'] = pd.to_datetime(data_df['Date'], infer_datetime_format=True)
data_df = data_df.set_index('index')


data_df.plot('Date', 'Temp',kind='line',
         linestyle='solid', markersize=0)

# Generate a plot of the data subset
#data_df.plot(y='Temp', kind='line', use_index=False,
#            style='-', ylim=[-0.5, 90], marker='o',
#            label='Water Temp')

# Get the current axis of the plot and
# set the x and y-axis labels
#ax = plt.gca()
#ax.set_ylabel('Temp (C)')
#ax.set_xlabel('Date/Time')
#ax.grid(True)

plt.show()












print('havent burst into flmame yet')