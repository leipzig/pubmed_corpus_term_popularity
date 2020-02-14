import nltk
nltk.download('brown')
from nltk import FreqDist
from nltk.corpus import brown #other choices are words, webtext, gutenberg
from eutils import Client
from secrets import api
import time
import random

ec = Client(api_key=api.apikey) #replace with your NCBI apikey
frequency_list = FreqDist(i.lower() for i in brown.words())

print("word\tcorpusFreq\tpubmedFreq")
for word in random.sample(set(brown.words()),100):
    freq=frequency_list[word.lower()]
    #let's focus on somewhat common words
    if(freq>1):
        try:
            a = ec.esearch(db='pubmed',term=word)
            print("{}\t{}\t{}".format(word,freq,a.count))
        except (TimeoutError):
            time.sleep(5) #slow down buddy
            ec = Client(api_key=api.apikey)
        time.sleep(1.5) #ncbi will complain otherwise