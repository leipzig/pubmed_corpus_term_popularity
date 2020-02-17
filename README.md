## View relative frequencies of random words in a English corpus and Pubmed

```
conda create -n pop nltk r-ggplot2 r-stringr r-dplyr
conda activate pop
chmod +x plot.R compareTwoGroups.R popwords.py twoGroups.py
```

### Study words from a nltk corpus
See [https://www.nltk.org/book/ch02.html](https://www.nltk.org/book/ch02.html) for a guide to the corpus feature. We compare their frequency in Pubmed texts to the sources used to compile the corpus.
```
./popwords.py --corpus brown --max 50 > results.txt
./plot.R --file results.txt
```

![plot](https://i.imgur.com/4JfbJiy.png)


### Compare any two categories available in the Brown corpus
These include 'adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction'

Using equally sized samples from each category, we compare the frequencies of these terms in Pubmed.
```
./twoGroups.py humor science_fiction > compare.txt
./compareTwoGroups.R --file compare.txt
```

![comp](https://imgur.com/BrDEKEH.png)
