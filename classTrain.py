import csv 
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
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getTrainData():
	negCount = 0
	posCount = 0

	with open('algorData.csv', 'wb') as csvfile:
		file = csv.writer(csvfile, delimiter = ';', quotechar ='"')
		with open('trainingDataSample.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ';', quotechar ='"')
			for line in reader:
				try:
					tweet = line[4].split()
					words = [w for w in tweet]
					print words
					tweet_clean = ' '.join(words)					
					if len(tweet_clean.split()) > 2 and detect(tweet_clean) == 'en':
						if sentAnalyser(tweet_clean)['compound'] >= int(0.65):
							posCount = posCount + 1
							pos = str("('%s','pos')," % str(tweet_clean))
							file.writerow([pos])
						elif sentAnalyser(tweet_clean)['compound'] <= int(-0.65):
							negCount = negCount + 1 
							neg = str("('%s','neg')," % str(tweet_clean))
							file.writerow([neg])
							

					
						print 'Neg : ', negCount
						print 'Pos : ', posCount
				
					
					

				except:
					pass


				

def sentAnalyser(passedTweet):

	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	return ss

getTrainData()
