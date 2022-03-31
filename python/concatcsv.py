# importing pandas
import pandas as pd

#input file
#constituency="DublinNorth2002"
#constituency="DublinWest2002"
constituency="Meath2002"
reg_csv='../data/processed/'+constituency+'_reg.csv'
irreg_csv='../data/processed/'+constituency+'_irreg.csv'
merged_csv='../data/processed/'+constituency+'_merged.csv'

(reg_csv, irreg_csv, merged_csv) = ('../data/processed/'+constituency+'_reg.csv','../data/processed/'+constituency+'_irreg.csv','../data/processed/'+constituency+'_merged.csv')

print(reg_csv)
print(irreg_csv)
print(merged_csv)
  
# merging two csv files
df = pd.concat(
    map(pd.read_csv, [reg_csv, irreg_csv]), ignore_index=True)

print(df.head(5))

# drop column ( old indexes column )
df = df.drop(df.columns[0], axis = 1)
print(df.columns)
listcols= list(df.columns)
del listcols[-4:]
print(listcols)

df = df.drop_duplicates(listcols, keep='first')
print(df.head(5))

# write dataframe of 2 csv files to csv file
df.to_csv(merged_csv)
