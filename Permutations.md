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


### Dublin West (nPr = 9P7)
![Dublin West Run](/images/RunGenAll-9P7.png)

### Dublin North (nPr = 12P7)
![Dublin North Run](/images/RunGenAll-12P7.png)

### Dublin West (nPr = 9P7)
![Meath Run](/images/RunGenAll-14P7.png)
