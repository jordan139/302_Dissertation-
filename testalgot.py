
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from itertools import chain
from textblob.classifiers import NaiveBayesClassifier
from text import training_data
from textblob import TextBlob
import sys
import pickle 

test = [
    ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')
 ]
f = open('algorithm.pickle', 'rb')

classifer = pickle.load(f)

print(classifer.classify('THis is amazing'))
print(classifer.classify('This looks so  good'))

print(classifer.accuracy(test))

f.close()