import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk import tokenize

#sentiment anlaysis librarys 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


            
#remove all noise from passed files in term sof punct, stop words and links
def removeNoise():
	x = 0
	with open('../skyrim.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
		for line in reader:
			x = x + 1 
			tweet = line[4].split() #cut the tweets out of the csv file
	
			#remove noise : stop words, punctuation and links usinf reg ex 
			words = [w for w in tweet if w not in stopwords.words('english')]
			tweet_clean = ' '.join(words)
			tweet_clean = re.sub(r'\d+', '', tweet_clean)

			#punctuation remover 
			#tweet_clean = re.sub(r'[!\?\.,;"]', '', tweet_clean)
			

			#print out the clean version of the tweet
			print x, ':',tweet_clean
			sentAnalyser(tweet_clean)
			demo_liu_hu_lexicon(tweet_clean, plot = False)
			print '\n'

			
			


#sort into pos/neg/nuetral sets 
def demo_liu_hu_lexicon(text, plot = False):

	#tokenizer funtion
	tokenizer = treebank.TreebankWordTokenizer()

	posList = []
	negList = []
	nueList = []

	posWords = 0
	negWords = 0
	nueWords = 0 
	
	tokenized =  [word.lower() for word in tokenizer.tokenize(text)]


	for word in tokenized:
		if word in opinion_lexicon.positive():
			posWords  = posWords + 1
			posList.append(word)
			
			#plot 
			#y.append(1)
		elif word in opinion_lexicon.negative():
			negWords = negWords + 1 
			negList.append(word)
			
			#plot 
			#y.append(-1)
		else:
			nueWords = nueWords + 1 
			nueList.append(word)
			
			#plot 
			#y.append(0)

	#print 'Positive Word No:',posWords #, '\n', 'Positive Word List:',posList,'\n'
	#print 'Negative Word No:',negWords #, '\n','Negative Word List:',negList, '\n'
	#print 'Nuetral Word No:', nueWords #, '\n','Nuetral Word List:', nueList, '\n'

	if nueWords > posWords and nueWords > negWords:
		print 'Overall Sentiment is : Nuetral'
	elif posWords < negWords:
		print 'Overall Sentiment is : Negative'
	elif posWords > negWords:
		print 'Overall Sentiment is : Positive'


#analysis funtion for any passed tweet
def sentAnalyser(passedTweet):

	#analysis on tweet it has been passed
	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	print ss



removeNoise()



