import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk import tokenize
from langdetect import detect

#unicode
import sys

#sentiment anlaysis librarys 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#read file as unicode not str
reload(sys)
sys.setdefaultencoding('utf8')

def removeNoise():
	x = 0
	y = 0
	with open('newTestFile.csv', 'wb') as csvfile:			
		file = csv.writer(csvfile, delimiter = ';', quotechar = '"')
		with open('data/skyrim.csv', 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
			for line in reader:

				try:

					#cut the tweets out of the csv file
					tweet = line[4].split() 
			
					#remove noise : stop words
					words = [w for w in tweet if w not in stopwords.words('english')]
					tweet_clean = ' '.join(words)

					#remove links 
					tweet_clean = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet_clean, flags=re.MULTILINE)

					#remove single tweets that contain hashtags 
					tweet_clean = re.sub(r'\#\S+','', tweet_clean)

					#final clean version of the tweet all noise removed 
					finalString = unicode(tweet_clean, errors = 'ignore')

					#rdont consider tweets with a size less than 2 words 


					if len(finalString.split()) > 2:
							if detect(finalString) == 'en':
								

								#write each cleaned tweet to a new file 
								file.writerow([finalString])
				except:
					print tweet_clean;


def sentAnalyser(passedTweet):

	#analysis on tweet it has been passed
	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	return ss
	

removeNoise()