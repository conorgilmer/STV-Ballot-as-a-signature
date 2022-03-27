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
  
# merging two csv files
df = pd.concat(
    map(pd.read_csv, [reg_csv, irreg_csv]), ignore_index=True)

#print(df)

# drop column ( old indexes column )
df = df.drop(df.columns[0], axis = 1)


# write dataframe of 2 csv files to csv file
df.to_csv(merged_csv)
