## Permutations (without repetition)
While the number of permutations of the completing a ballot for the all candidates is factorial(n) or
n!
The number of permutations(P) for r preferences cast, for an election with n candidates is

nPr = P(n,r) = n!/(n-r)!

## All Permutats nPr 

Pref(r)	| n=9	 | n=12	     | n = 14
------: |------: |---------: |-----------:
1	| 9	 | 12	     | 14
2	| 72	 | 132	     |  182
3	| 504	 | 1320	     |  2184
4	| 3024	 | 11880     |	24024
5	| 15120	 | 95040     |	240240
6	| 60480	 | 665280    |	2162160
7	| 181440 | 3991680   |	17297280
8	| 362880 | 19958400  |	121080960
9	| 362880 | 79833600  |	726485760
10	|        | 239500800 |  3632428800
11	|        | 479001600 | 14529715200
12	|        | 479001600 | 43589145600
13	|        |           | 87178291200
14	|        |	     | 87178291200

## Generate All Permutations (nPr) for Constituencies win r=7
Running **[GenAll-nPr.py](/python/py/GenAll-nPr.py)**

Constituency | Candidates | Preferences(r) |    nPr   | Filesize
-------------|:----------:| :------------: | -------: | ---------:
Dublin West  |      9     |      7         |   181440 |   6602200
Dublin North |     12     |      7         |  3991680 | 162547817
Meath        |     14     |      7         | 17297280 | 749969267


### Dublin West (nPr = 9P7)
![Dublin West Run](/images/RunGenAll-9P7.png)

### Dublin North (nPr = 12P7)
![Dublin North Run](/images/RunGenAll-12P7.png)

### Dublin West (nPr = 9P7)
![Meath Run](/images/RunGenAll-14P7.png)
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
