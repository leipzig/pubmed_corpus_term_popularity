## View relative frequencies of random words in a English corpus and Pubmed

```
conda create -n pop nltk r-ggplot2 r-stringr r-dplyr
conda activate pop
chmod +x plot.R compareTwoGroups.R popwords.py twoGroups.py
```

### Study words from a nltk corpus
```
./popwords.py --corpus brown --max 50 > results.txt
./plot.R --file results.txt
```

![plot](https://i.imgur.com/4JfbJiy.png)


### Compare two groups
```
./twoGroups.py humor science_fiction > compare.txt
./compareTwoGroups.R --file compare.txt
```

![comp](https://imgur.com/BrDEKEH.png)