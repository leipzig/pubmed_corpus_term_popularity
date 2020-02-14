View relative frequencies of 100 randomly words in the Brown corpus and Pubmed

```
conda create -n pop nltk r-ggplot2
conda activate pop
python popwords.py > compare.txt
cat plot.R | R --vanilla
```

![plot](https://i.imgur.com/4JfbJiy.png)
