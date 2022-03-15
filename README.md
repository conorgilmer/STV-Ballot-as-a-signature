# STV-Ballot-as-a-signature
PR-STV Irregular voting patterns which could be used as a ballot as a signature attack
## Permutations (without repetition)
nPr = P(n,r) = n!/(n-r)!
## Tasks
- plot irish political parites on the political compass (politicalcompass.org)
- **PlotRegularVoteTransfers.ipynb** - plot regular voting pattern (between similar ideologies)
- **PlotIrregularVoteTransfers.ipynb** - plot irregular voting pattern
- **VoteDataAnalysis.ipynb** - analyse data from e-voting trial from 2002
  - number of preferences cast
  - mode
  - median
  - mean
  - generate histograms
  - calculate duplicates (remove duplicates)
- **RandGen-nPr.ipynb** 
  - generate random permutations nPr
  - generate random permutations for range r values
- classify actual votes as 'regular' and generated as 'irregular'
- split dataset into test and train
- test machine learning algorithms on dataset measure performance

## Data Used from e-voting trial from 2002
- Meath2002.csv
- DublinNorth2002.csv
- DublinWest2002.csv
