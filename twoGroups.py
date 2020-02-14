from nltk.corpus import brown  # other choices are words, webtext, gutenberg
import sys
import random
import time
from secrets import api
from urllib3.exceptions import MaxRetryError
from eutils import Client
from nltk import FreqDist
import nltk
nltk.download('brown')

ec = Client(api_key=api.apikey)  # replace with your NCBI apikey
frequency_list = FreqDist(i.lower() for i in brown.words())

categories = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies',
              'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

assert(sys.argv[1] in categories and sys.argv[2] in categories)

corpi = {}
corpi[sys.argv[1]] = random.sample(set(brown.words(categories=sys.argv[1])), 50)
corpi[sys.argv[2]] = random.sample(set(brown.words(categories=sys.argv[2])), 50)
print("category\tword\tcorpusFreq\tpubmedFreq")
for category in [sys.argv[1], sys.argv[2]]:
    for word in corpi[category]:
        freq = frequency_list[word.lower()]
        # let's focus on somewhat common words
        if(freq > 1):
            try:
                a = ec.esearch(db='pubmed', term=word)
                print("{}\t{}\t{}\t{}".format(category, word, freq, a.count))
            except (TimeoutError, MaxRetryError, ConnectionError):
                time.sleep(5)  # slow down buddy
                ec = Client(api_key=api.apikey)
            time.sleep(0.1)  # ncbi will complain otherwise
