import csv 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk import tokenize
from langdetect import detect
import re


#sentiment anlaysis librarys 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getTrainData(dataTotal):
	negCount = 0
	posCount = 0

	#write to this file
	with open('algorData.csv', 'wb') as csvfile:
		file = csv.writer(csvfile, delimiter = ';', quotechar ='"')
		#training data within this file to be formatted into correct syntax
		with open('trainingDataSample.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ';', quotechar ='"')
			for line in reader:
				try:

					#clean tweet
					tweet = line[4].split()
					words = [w for w in tweet] 
					tweet_clean = ' '.join(words)
					tweet_clean = re.sub("'","",tweet_clean)


					#even amount os pos/neg tweets for naive bayes algorithm 
					if len(tweet_clean.split()) > 2 and detect(tweet_clean) == 'en':
						if posCount < dataTotal and sentAnalyser(tweet_clean)['compound'] >= int(0.65):
							pos = str("('%s','pos')," % str(tweet_clean))
							file.writerow([pos])
							posCount = posCount + 1
						elif negCount < dataTotal and sentAnalyser(tweet_clean)['compound'] <= int(-0.65):
							neg = str("('%s','neg')," % str(tweet_clean))
							file.writerow([neg])
							negCount = negCount + 1 
						else:
							pass

					print 'Neg : ', negCount
					print 'Pos : ', posCount

					#break when all tweets have been gathered 
					if negCount == dataTotal and posCount == dataTotal:
						break
				except:
					pass


				

def sentAnalyser(passedTweet):

	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	return ss

getTrainData(20)
