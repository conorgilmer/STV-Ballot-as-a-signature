import pandas as pd

#process for constituency change Seq to Sequence, and 1/0 to Regular /Irregular
def process(constituency):
    print("Processing ", constituency)
    in_csv  = "../../data/processed/"+constituency+"_merged.csv"
    out_csv = "../../data/processed/"+constituency+"_merged_out.csv"
    print("Reading in ", in_csv)
    df = pd.read_csv(in_csv)
    df['Sequence'] = df['Seq'].map({0: "Irregular", 1: "Regular"})
    df = df.drop(['Seq'], axis=1)
    #drop the old numbers column
    df = df.drop(df.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
    #reset index to start a 1 and not 0
    df.index = df.index + 1

    print("Writing ", out_csv)
    df.to_csv(out_csv)


# main function
def main():
    consList =['Meath2002','DublinWest2002', 'DublinNorth2002']
    print("Constituencies to process - ", consList)
    for cons in consList:
        process(cons)
    print("Complete")

# call main
if __name__ == "__main__":
    main()
