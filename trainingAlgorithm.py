import nltk 
import random 
from nltk.corpus import movie_reviews 
import csv 




def naive():
	documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]	
	random.shuffle(documents)
	allWords = []
	for words in movie_reviews.words():
		allWords.append(words.lower()) 
	allWords = nltk.FreqDist(allWords)
	wordFeatures = list(allWords.keys())[:3000]
	findFeatures()

def findFeatures(document):
	words = set(document)
	features = {}
	for w in wordFeatures:
		features[w] = (w in words)

	return features 



print((findFeatures(movie_reviews.words('neg/c'))))


naive()