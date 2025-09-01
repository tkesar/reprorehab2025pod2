#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 21:30:07 2025

@author: jinseok
"""
import pandas as pd

# %% Read sample data
csv_folder = '/home/jinseok/Downloads/'
data = pd.read_csv(csv_folder + 'mental_health_wearable_data.csv', sep=',')

data

data = pd.read_csv('/home/jinseok/Downloads/mental_health_wearable_data.csv',
                   sep=',', header=0)

data = pd.read_csv('mental_health_wearable_data.csv', 
                   names=['my_column_A', 'my_column_B',
                          'my_column_C', 'my_column_D', 'my_column_E'])

# Rename
data.rename(columns={'Heart_Rate_BPM': 'HR_BPM'}, inplace=True)
# %% DataFrame.plot

# Histogram
data.plot.hist(column='Heart_Rate_BPM',
               alpha=0.6, edgecolor='k',
               facecolor='pink', title='Heart Rate BPM', legend=False)

# Boxplot
data.plot.box(column='Heart_Rate_BPM', by="Mood_Rating",
              title='Heart Rate BPM by Mood Rating',
              xlabel='Mood Rating')

# Scatterplot
data.plot.scatter(x='Heart_Rate_BPM', y='Sleep_Duration_Hours',
                  s=4, edgecolor='k', color='None')

# Hexbin
data.plot.hexbin(x="Heart_Rate_BPM", y='Sleep_Duration_Hours',
                 gridsize=30, cmap='cividis')
