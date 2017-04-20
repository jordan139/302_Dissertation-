from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from itertools import chain
from textblob.classifiers import NaiveBayesClassifier
from text import training_data
from textblob import TextBlob
import sys
import pickle 

def train():

	classifer = NaiveBayesClassifier(training_data)
	f = open('algorithm.pickle', 'wb')
	pickle.dump(classifer, f)
	f.close()



def analysis():
	test = [
    ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')
 ]
	classObject = open('algorithm.pickle', 'rb')
	classifier = pickle.load(classObject)
	
	
	print(classifier.accuracy(test))
	


analysis()




























# vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))

# feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]

# classifier = nbc.train(feature_set)

# test_sentence = "This game looks so shit!!"
# featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}

# print "test_sent:",test_sentence
# print "tag:",classifier.classify(featurized_test_sentence)