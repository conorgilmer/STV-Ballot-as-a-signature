#!/usr/bin/env python
# coding: utf-8

#read vote data from csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#input file
constituency="DublinWest2002_merged"
in_csv='../../data/processed/'+constituency+'.csv'

#read in data (setting 1st row as header)
print("Opening - ", in_csv)
df = pd.read_csv(in_csv, na_values=["Missing"], header=[0])

#top 10 and tail 10 into dataframes
print("Load top and bottom 10 rows into 2 dataframes")
dfi=df[:10]  # same as df.head(10)
dfj=df[-10:] # same as df.tail(10)

#merge/concatenate two data frames
print("Merge Dataframes")
frames=[dfi,dfj]
result = pd.concat(frames)

#remove 1st colum old numbers
print("Remove old indexes and reset index")
result = result.iloc[: , 1:]
print("Dataframe shape ", result.shape)
result.reset_index(inplace=True, drop=True) 

#write merged dataframe to csv
merged_csv='../../data/processed/'+constituency+'toptail.csv'
print("Saving merged dataframe as ", merged_csv)
result.to_csv(merged_csv)






