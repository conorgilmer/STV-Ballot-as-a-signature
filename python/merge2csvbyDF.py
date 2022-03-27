# importing pandas
import pandas as pd

#input file
constituency="Test2002"
#constituency="DublinNorth2002"
#constituency="DublinWest2002"
#constituency="Meath2002"
reg_csv='../data/'+constituency+'.csv'
irreg_csv='../data/'+constituency+'gen.csv'
merged_csv='../data/'+constituency+'merged.csv'
 
#read in csv reg into dfR
dfR = pd.read_csv(reg_csv)
#print(dfR)

#read in csv reg into dfR
dfI = pd.read_csv(irreg_csv)
print(dfI)

# merging two csv files using dataframe
df = dfR.append(dfI, ignore_index=True)

print(df.tail())
# drop "2nd" column old indexes
#df = df.drop(df.columns[0], axis = 1) 

# write dataframe of 2 csv files to csv file
df.to_csv(merged_csv)
