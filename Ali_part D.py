  
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime 
import calendar 

# Reading the file as a dataset
file = pd.read_csv('activity.csv')

# Function to check if day is weekday or weekend
def getday(date): 
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_date = datetime.datetime.strptime(date, '%Y-%m-%d').weekday() 
    if calendar.day_name[day_date] in weekdays:
        return 'Weekday:('
    else:
        return 'weekend:)'

# Unfortunately, couldnt find a way of grouping and displayin the weekdays and weekend in time
