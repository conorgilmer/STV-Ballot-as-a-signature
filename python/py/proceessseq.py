import pandas as pd


def process(constituency):
    in_csv  = "../../data/processed/"+constituency+"_merged.csv"
    out_csv = "../../data/processed/"+constituency+"_out.csv"
    df = pd.read_csv(in_csv)
    df['Sequence'] = df['Seq'].map({0: "Irregular", 1: "Reg"})
    df = df.drop(['Seq'], axis=1)
    df.to_csv(out_csv)


def main():
    process("Meath2002")
    process("DublinNorth2002")
    process("DublinWest2002")

if __name__ == "__main__":
    main()
