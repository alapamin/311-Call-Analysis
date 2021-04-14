#Written by Mohammad Amin
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import folium
import operator
import itertools
from folium import plugins
from collections import Counter
sns.set_theme(style="darkgrid")
low_memory = False
#Using modules needed to represent the data and visualize it efficiently, namely seaborn.

#Setup dataframe
df = pd.read_csv("calls.csv", error_bad_lines=False,quoting=csv.QUOTE_NONE, encoding = 'utf-8') 

#This creates an index for the first column which originally gave us “Series objects are mutable and cannot be hashed” error
typeOnly = df[['Complaint_Type']]
typeOnly = typeOnly.reset_index()

#We drop that first index column to clean the data
typeOnly.drop(['index'],axis = 1,inplace = True)

#This creates a list of all the complain types 
#AS LONG AS they are not empty values.
keys = []
for value in typeOnly.Complaint_Type:
    if pd.notna(value):
        keys.append(value)

#In this new dictionary, we are taking all values in keys and adding them to the dictionary, if it already is in the dict, we add 1 to it
complainDict = {}
for value in keys:
    if value not in complainDict:
        complainDict[value] = 0
    else:
        complainDict[value]+=1

#Here we order the dictionary by descending values of most occuring complaint types
c = (Counter(complainDict).most_common())

#Even though Counter is a sub-section of a dictionary, I converted it back to a dict for visual appeal
d = dict(c)

#We want the top 10 most occuring complaint types
#There's no such thing a the "first n" keys because a dict doesn't remember which keys were inserted first.
#So we use isslice() from itertools to accomplish this.
topTen = dict(itertools.islice(d.items(), 10))

#Time to put them on a barplot!
keys = list(topTen.keys())
# get values in the same order as keys, and parse percentage values
vals = [float(topTen[k]) for k in keys]

plt.figure(figsize=(8,4))


ax = sns.barplot(x=keys, y=vals)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right") #Rotate x-axis text by 40 degrees to fit better
plt.tight_layout() #Adjust text layout to fit better
plt.show()

    

