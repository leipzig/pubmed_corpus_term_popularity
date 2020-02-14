View relative frequencies of words in corpuses and Pubmed

```
conda create -n pop nltk r-ggplot2
conda activate pop
python popwords.py > compare.txt
cat plot.R | R --vanilla
```

![plot](https://i.imgur.com/LuRGZNn.png)
