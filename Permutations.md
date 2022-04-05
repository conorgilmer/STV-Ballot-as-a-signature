## Permutations (without repetition)
While the number of permutations of the completing a ballot for the all candidates is factorial(n) or
n!
The number of permutations(P) for r preferences cast, for an election with n candidates is

nPr = P(n,r) = n!/(n-r)!


## Generate All Permutations (nPr) for Constituencies
Running **[GenAll-nPr.py](/python/py/GenAll-nPr.py)**

Constituency | Candidates | Preferences(r) |    nPr   | Filesize
-------------|------------| -------------- | -------- | ----------
Dublin West  |      9     |      7         |   181440 |   6602200
Dublin North |     12     |      7         |  3991680 | 162547817
Meath        |     14     |      7         | 17297280 | 749969267


#political compass
[pc.csv]!(/data/pc.csv)
