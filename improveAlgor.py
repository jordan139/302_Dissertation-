import nltk
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import random 


documents = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

allWords = []
for w in movie_reviews.words():
	allWords.append(w.lower())

allWords = nltk.FreqDist(allWords)
wordFeatures = list(allWords.keys())[:3000]


def findFeatures(document):
	words = set(document)
	features = {}
	for w in wordFeatures:
		features[w] = (w in words)
	return features
	 

#print((findFeatures(movie_reviews.words('neg/cv000_29416.txt'))))
featureSets = [(findFeatures(rev), category) for (rev, category) in documents ]

new_training_set = featureSets[:100]
testing_set = featureSets[100:]


cl = NaiveBayesClassifier(new_training_set)
print(cl.accuracy(testing_set))


