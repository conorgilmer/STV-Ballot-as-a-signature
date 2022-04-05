import pandas as pd

#process for constituency change Seq to Sequence, and 1/0 to Regular /Irregular
def process(constituency):
    in_csv  = "../../data/processed/"+constituency+"_merged.csv"
    out_csv = "../../data/processed/"+constituency+"_merged_out.csv"
    df = pd.read_csv(in_csv)
    df['Sequence'] = df['Seq'].map({0: "Irregular", 1: "Regular"})
    df = df.drop(['Seq'], axis=1)

# main function
def main():
    process("Meath2002")
    process("DublinNorth2002")
    process("DublinWest2002")

# call main
if __name__ == "__main__":
    main()
