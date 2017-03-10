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


testArray = ["VADER is smart, handsome, and funny i hate driving."]

def removeNoise():
	x = 0
	with open('test.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
		for line in reader:
			x = x + 1 
			tweet = line[4].split() #cut the tweets out of the csv file
	
			#remove noise : stop words, punctuation and links usinf reg ex 
			words = [w for w in tweet if w not in stopwords.words('english')]
			tweet_clean = ' '.join(words)
			tweet_clean = re.sub(r'\d+', '', tweet_clean)
			tweet_clean = re.sub(r'[!\?\.,;"]', '', tweet_clean)

			#print out the clean version of the tweet
			print x, ':',tweet_clean

def demo_liu_hu_lexicon(file, plot = False):

	#tokenizer funtion
	tokenizer = treebank.TreebankWordTokenizer()

	posList = []
	negList = []
	nueList = []

	posWords = 0
	negWords = 0
	nueWords = 0 
	
	tokenized =  [word.lower() for word in tokenizer.tokenize(file)]

	#plot to graph 
	x = list(range (len (tokenized)))
	y = []

	for word in tokenized:
		if word in opinion_lexicon.positive():
			posWords  = posWords + 1
			posList.append(word)
			#plot 
			y.append(1)
		elif word in opinion_lexicon.negative():
			negWords = negWords + 1 
			negList.append(word)
			#plot 
			y.append(-1)
		else:
			nueWords = nueWords + 1 
			nueList.append(word)
			#plot 
			y.append(0)

	print 'Positive Word No:',posWords, '\n', 'Positive Word List:',posList,'\n'
	print 'Negative Word No:',negWords, '\n','Negative Word List:',negList, '\n'
	print 'Nuetral Word No:', nueWords, '\n','Nuetral Word List:', nueList, '\n'

	if nueWords > posWords and nueWords > negWords:
		print 'Overall Sentiment is : Nuetral'
	elif posWords < negWords:
		print 'Overall Sentiment is : Negative'
	elif posWords > negWords:
		print 'Overall Sentiment is : Positive'




def sentAnalyser(a):
	 
	analyzer = SentimentIntensityAnalyzer()
	for sentence in testArray:

		ss = analyzer.polarity_scores(sentence)
		print ss 


	#if plot == True:
	#	_show_plot(x,y, x_labels= tokenized, y_labels = ['Negative', 'Nuetral', 'Positive'])


#test instance 1 Pos:16 Neg:23 Nue:15 --> ouput = overall sentiment is: Negitive 
#demo_liu_hu_lexicon("my name love love love love love hate hate hate hate hate hate hate hate hate hate hate hate hate hate hate hate hate hate love love love love love love love love love love is jordan, hit, kill rape murder flowers bang love need hate bang n and i hate programming")


sentAnalyser(testArray)


	






