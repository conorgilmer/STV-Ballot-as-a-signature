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

## Generate All Permutations (nPr) for Constituencies
Running **[GenAll-nPr.py](/python/py/GenAll-nPr.py)**

Constituency | Candidates | Preferences(r) |    nPr   | Filesize
-------------|------------| -------------- | -------- | ----------
Dublin West  |      9     |      7         |   181440 |   6602200
Dublin North |     12     |      7         |  3991680 | 162547817
Meath        |     14     |      7         | 17297280 | 749969267


### Dublin West (nPr = 9P7)
![Dublin West Run](/images/RunGenAll-9P7.png)

### Dublin North (nPr = 12P7)
![Dublin North Run](/images/RunGenAll-12P7.png)

### Dublin West (nPr = 9P7)
![Meath Run](/images/RunGenAll-14P7.png)
