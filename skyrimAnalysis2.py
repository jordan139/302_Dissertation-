import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize


from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank






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

def demo_liu_hu_lexicon(file, plot = True):

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

	if posWords > negWords:
		print 'Overall Sentiment is : Positive'
	elif posWords < negWords:
		print 'Overall Sentiment is : Negative'


	#debug this
	elif nueWords > posWords and nueWords > negWords:
		print 'Overall Sentiment is : Neutral'
	#if plot == True:
	#	_show_plot(x,y, x_labels= tokenized, y_labels = ['Negative', 'Nuetral', 'Positive'])
	print posWords
	print negWords
	print nueWords

#demo_liu_hu_lexicon("hate love enjoy hat cant wait love you need you must have need want must lust love")

removeNoise()




	






