# STV-Ballot-as-a-signature
PR-STV Irregular voting patterns which could be used as a ballot as a signature attack
## Permutations (without repetition)
nPr = P(n,r) = n!/(n-r)!
## Tasks
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
- **[RandGen-nPr.ipynb](/python/RandGen-nPr.ipynb)** 
  - generate random permutations nPr
- **[RandGen-nPr-O.ipynb](/python/RandGen-nPr-O.ipynb)** 
  - generate O, random permutations nPr (n=candidates, r=preferences, O=number of permutations to generate)
- **[RandGen-nPr-range-of-r.ipynb](/python/RandGen-nPr-range-of-r.ipynb)** 
  - generate random permutations for range r values
- calculate eculidean distance travelled by transfers for each vote - classify high values as irregular
- classify actual votes as 'regular' and generated as votes with high  'irregular'
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
