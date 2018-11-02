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
#       - connecting to sql server -> sqlite3
#       - to pull datetimes
#       - making plots             -> matplotlib.pyplot
#       - performing stats         -> pandas

import sqlite3
import datetime
import matplotlib.pyplot as plt
import pandas

# 2. Receive input
#       - variables:
#              1. site ID
#              2. monthID
#              3. yearID
#              4.

siteID = input('Please input the SiteID to be analyzed: ')
yearID = input('Please select the year to be analyzed: ')
monthID = input('Please select the month to be displayed: ')


# 3. Query database
#    a. establish connection
conn = sqlite3.connect('Logan_River_Temperature_ODM.sqlite')

#   b. build query
#  - filter by month    (do filtering in pandas dataframe)
#       - filter by year
#           - pull all data values
sql_statement = 'SELECT LocalDateTime, DataValue  ' \
                'FROM datavalues ' \
                'WHERE VariableID = 1 AND SiteID = ' + siteID + ' AND DataValue <> -9999 ' \
                'AND QualityControlLevelID = 1'

#    c. execute query
cursor = conn.cursor()
cursor.execute(sql_statement)
rows = cursor.fetchall()



# 4. Transform data into usable lists
#       - pull all data

localDateTimes, dataValues = zip(*rows)

# Convert the localDateTime values from string values
# to date/time values

# First create an empty list for the converted date/time values
plotDates = []
# Loop through the localDateTimes tuple and convert the values to date/time
# Append the converted values to the plotDates list
for x in localDateTimes:
    plotDates.append(datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

#       - get data in over all pandas dataframe
#                -> see class 20 example
#                 - sort by year into dataframes
#

# 5. Perform calculations
#    a. time series plot for month
#       - see class20_example2
#    b. stats
#    c. histogram
#    d. year to year comparison
#           i. use longer time interval

# 6. Import into graph

# Create a plot of the LocalDateTime and
# DataValue lists. Make it a solid grey
# line with no markers.
plt.figure(figsize=(9,5))
plt.plot(plotDates, dataValues, color='grey',
         linestyle='solid', markersize=0)


# 7. Output graph
#    a. seperate window

# Get the current axis of the plot and
# set the x and y-axis labels
ax = plt.gca()
ax.set_ylabel('Temperature ($^\circ$C)')
ax.set_xlabel('Date/Time')
ax.grid(True)

# Set the title
ax.set_title('Water temperature in the Logan '
             'River \n at the Utah Water Research '
             'Laboratory')
#    b. save graph
# Save the plot to a file
plt.savefig('Example_Plot.png')

plt.show()



print('havent burst into flmame yet')