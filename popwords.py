#!/usr/bin/env python

import nltk
nltk.download('brown')
nltk.download('words')
nltk.download('webtext')
nltk.download('gutenberg')
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import gutenberg
corpi = {}
corpi['brown']=brown
from nltk import FreqDist
from eutils import Client
from secrets import api
import time
import random

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--max", help="number of words to test",  nargs='?', const=1, type=int, default=50)
parser.add_argument("-c", "--corpus", help="the corpus (brown,webtext,gutenberg)", default="brown")
args = parser.parse_args()

print(args.corpus)
corpus = eval(args.corpus)

ec = Client(api_key=api.apikey) #replace with your NCBI apikey
frequency_list = FreqDist(i.lower() for i in corpus.words())

print("word\tcorpusFreq\tpubmedFreq")
for word in random.sample(set(corpus.words()),args.max):
    freq=frequency_list[word.lower()]
    #let's focus on somewhat common words
    if(freq>1):
        try:
            a = ec.esearch(db='pubmed',term=word)
            print("{}\t{}\t{}".format(word,freq,a.count))
        except (TimeoutError):
            time.sleep(5) #slow down buddy
            ec = Client(api_key=api.apikey)
        time.sleep(0.1) #ncbi will complain otherwise
