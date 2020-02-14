View relative frequencies of 100 randomly words in the Brown corpus and Pubmed

```
conda create -n pop nltk r-ggplot2 r-stringr r-dplyr
conda activate pop
chmod +x plot.R compareTwoGroups.R popwords.py twoGroups.py
```

Study words from a corpus
```
./popwords.py --max 50 > results.txt
./plot.R --file results.txt
```

![plot](https://i.imgur.com/4JfbJiy.png)


compare two groups
```

```