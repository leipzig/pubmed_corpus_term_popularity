import nltk
nltk.download('brown')
from nltk import FreqDist
from nltk.corpus import brown #other choices are words, webtext, gutenberg
from eutils import Client
from urllib3.exceptions import MaxRetryError
from secrets import api
import time
import random

ec = Client(api_key=api.apikey) #replace with your NCBI apikey
frequency_list = FreqDist(i.lower() for i in brown.words())

corpi={}
corpi['romance']=random.sample(set(brown.words(categories='romance')),50)
corpi['news']=random.sample(set(brown.words(categories='news')),50)
print("category\tword\tcorpusFreq\tpubmedFreq")
for category in ['romance','news']:
    for word in corpi[category]:
        freq=frequency_list[word.lower()]
        #let's focus on somewhat common words
        if(freq>1):
            try:
                a = ec.esearch(db='pubmed',term=word)
                print("{}\t{}\t{}\t{}".format(category,word,freq,a.count))
            except (TimeoutError, MaxRetryError,ConnectionError):
                time.sleep(5) #slow down buddy
                ec = Client(api_key=api.apikey)
            time.sleep(0.5) #ncbi will complain otherwise