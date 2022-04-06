## Data Generation
To train the data set you need a dataset of "irregular" permutation, to do this the input actual election data was studied for each of the three consittuencies. A overa factorial of 10 is a massive number, it was decided to use nPr using around 7 preference cast while still a large number is still a fraction of the valid input data.

### Dublin West 2002
All possible permutations were generated for Dublin West for 9 candidates n, and 6, 7 and 8 preference votes cast, r. From
these votes votes which had a higher euclid value than the max value for that preference vote from the election data were s
elected.

r   | Euclid Dist | Votes | File
:--:|-------------|------:| -------------------------------------------
all |             | 10335 | DublinWest2002Reg.csv
 6  | >44.5       | 64    | DublinWest2002_9P6_Allgenerated_gen_irreg.cs
 7  | >47.3       | 1280  | DublinWest2002_9P7_Allgenerated_gen_irreg.cs
 8  | >50.05      | 140   | DublinWest2002_9P8_Allgenerated_gen_irreg.cs
all |             | 11819 | DublinWest2002_merged.csv

### Balance of Merged Data Set
Roughly only 1500 of the votes which were generated fulfilled the criteria of irregular, adding these to the 10000 regular vote permutaitons cast gives quite an unbalance dataset

![Data Set Balance](/images/DublinWest2002_merged_dataset_balance_hist.png)
