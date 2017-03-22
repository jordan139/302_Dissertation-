import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk import tokenize
from langdetect import detect


#sentiment anlaysis librarys 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



def removeNoise():
	x = 0
	with open('test.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
		for line in reader:
			tweet = line[4].split() #cut the tweets out of the csv file
	
			#remove noise : stop words
			words = [w for w in tweet if w not in stopwords.words('english')]
			tweet_clean = ' '.join(words)

			#remove links 
			tweet_clean = re.sub(r'\d+', '', tweet_clean)


			#remove single tweets that contain hashtags 
			tweet_clean = re.sub(r'\#\S+','', tweet_clean)


			#remove Tweets greater than the size of 2
			if len(tweet_clean.split()) > 2:						
					if sentAnalyser(tweet_clean)['compound'] == 0:
						#with open('test.csv', 'w') as csvfile:
		
						print (tweet_clean)


					#detect langauge 
					#if detect(tweet_clean) == 'en':
					#	print tweet_clean



def sentAnalyser(passedTweet):

	#analysis on tweet it has been passed
	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	return ss
	

removeNoise()