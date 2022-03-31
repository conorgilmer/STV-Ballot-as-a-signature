# importing pandas
import pandas as pd


def merge2CSV(constituency):
    (reg_csv, irreg_csv, merged_csv) = ('../data/processed/'+constituency+'_reg.csv','../data/processed/'+constituency+'_irreg.csv','../data/processed/'+constituency+'_merged.csv')

    print(reg_csv)
    print(irreg_csv)
    print(merged_csv)
  
# merging two csv files
    df = pd.concat(map(pd.read_csv, [reg_csv, irreg_csv]), ignore_index=True)

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
    print("merged"+constituency + " into "+ merged_csv)

#input file
merge2CSV("DublinNorth2002")
merge2CSV("DublinWest2002")
merge2CSV("Meath2002")
