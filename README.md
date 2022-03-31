# STV-Ballot-as-a-signature
PR-STV Irregular voting patterns which could be used as a ballot as a signature attack
## Permutations (without repetition)
nPr = P(n,r) = n!/(n-r)!
## Tasks
### Data Gathering and Generation
- plot irish political parites on the Political Compass ([politicalcompass.org](https://politicalcompass.org/ireland2020))
- **[PlotRegularVoteTransfers.ipynb](/python/PlotRegularVoteTransfers.ipynb)** - plot regular voting pattern (between similar ideologies)
- **[PlotIrregularVoteTransfers.ipynb](/python/PlotIrregularVoteTransfers.ipynb)** - plot irregular voting pattern
- **[VoteDataAnalysis.ipynb](/python/VoteDataAnalysis.ipynb)** - analyse data from e-voting trial from 2002
  - number of preferences cast
  - mode
  - median
  - mean
  - generate histograms
  - calculate duplicates (remove duplicates)
  - calculate number of unique votes for each vote sequence
  - caclulate possible permutations for each pref nonPr and % used
  - calculate "votes" euclidean distance and average euclidean distance for each transfer
  - classify as "regular" write to regular csv file
- **[RandGen-nPr.ipynb](/python/RandGen-nPr.ipynb)** 
  - generate random permutations nPr
- **[RandGen-nPr-O.ipynb](/python/RandGen-nPr-O.ipynb)** 
  - generate O, random permutations nPr (n=candidates, r=preferences, O=number of permutations to generate)
  - calculate "votes" euclidean distance and average euclidean distance for each transfer
  - classify as "irregular" write to irregular csv file
- **[RandGen-nPr-range-of-r.ipynb](/python/RandGen-nPr-range-of-r.ipynb)** 
  - generate random permutations for range r values
- **[concatBatch.py](/python/concatBatch.py)**
  -concatenate(merge) regular and irregular csv files
  -remove duplicates keeping sequence classified as regular
  -writes to merged csv file
###Machine Learning
- split dataset into test and train
- test machine learning algorithms on dataset measure performance
- tune model
- evaluate performance

## Data Used from e-voting trial from 2002
- [Meath2002.csv](/data/Meath2002.csv)
- [DublinNorth2002.csv](/data/DublinNorth2002.csv)
- [DublinWest2002.csv](/data/DublinWest2002.csv)

## Data from Political Compass [pc.csv](/data/pc.csv)
Data from 2002, when eVoting trial was conducted
![Irish parties on the political compass](/images/PCplot.png)

| Party | X    | Y     |
|-------|------|-------|
| SP    | -7   | -2.5  |
| SF    | -4.5 | 1     |
| GP    | -1   | -2    |
| NP    | 0    | 0     |
| LB    | 1.5  | -0.5  |
| FF    | 2.5  | 2.4   |
| FG    | 3.5  | 2.5   |
| PD    | 4    | 3     |

### Plot of transfers of a regular vote
![Plot of transfers of a regular vote](/images/RegularVoteTransferplot.png)

### Plot of transfers of an irregular vote
![Plot of transfers of a irregular vote](/images/IrregularVoteTransfersplot.png)

## Technology and software used
- python 3.8 - [python.org](https://python.org)
- Anaconda 1.10 with Juypter Notebook 6.1.4 [Anaconda Individual Edition](https://www.anaconda.com/products/individual)
- macOS Sierra 10.12.6
- Vim 7.4 (MacVim) [www.vim.org](https://vim.org)
- Thonny 3.3.1 (with Python 3.7.9) [www.thonny.org](https://thonny.org)
- Atom Editor - [atom.io](https://atom.io/)
