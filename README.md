# 311-Call-Analysis
WIP Project that utilizes 311 call data from nycopendata to create visual representations of it.

A project I'm working on solo that utilizes modules like seaborn, matplotlib, pandas, etc to create an appealing visual representation of 311 call data 
in the year 2020, written in a jupyter notebook for efficiency.

So far, I've cleaned the data for specific columns that I'm utilizing, namely the complaint_type column. 
I was able to utilize seaborn to create a bar graph which shows the top 10 complaint types in 311 calls, in descending order.

FUTURE ROADMAP:

-Get the software onto a website that I create to allow for user input online, so that someone can find whatever data they want in regards to 311 calls.
  --This will be in June once I finish a .NET course
-Create a visual representation of which borough in the 5 boroughs gets the most calls using folium
-Show how call quantity changes throughout the months using a regression graph
  --In order to do this the column for date_created must be cleaned and set as integers so that we can order the dates.
  --Since there are several calls made daily, must add calls for each month individually.
