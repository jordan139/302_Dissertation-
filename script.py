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



negComp = []
posComp = []
nueComp = []        
#remove all noise from passed files in term sof punct, stop words and links
def removeNoise():
	x = 0
	with open('testFile.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
		for line in reader:
			x = x + 1 
			tweet = line[0].split() #cut the tweets out of the csv file
	
			#remove noise : stop words, punctuation and links usinf reg ex 
			words = [w for w in tweet if w not in stopwords.words('english')]
			tweet_clean = ' '.join(words)
			tweet_clean = re.sub(r'\d+', '', tweet_clean)

			#punctuation remover 
			#tweet_clean = re.sub(r'[!\?\.,;"]', '', tweet_clean)
			

			#print out the clean version of the tweet
			#print x, ':',tweet_clean
			tweet_clean = re.sub(r'\#\S+','', tweet_clean)


			

			#if sentAnalyser(tweet_clean)['compound'] == int(0.0):
			#	print tweet_clean
			print x,'/1973'
			
			sentAnalyser(tweet_clean)

					
					
			#demo_liu_hu_lexicon(tweet_clean, plot = False)
			#print '\n'

#analysis funtion for any passed tweet
def sentAnalyser(passedTweet):

	#analysis on tweet it has been passed
	analyzer = SentimentIntensityAnalyzer()
	ss = analyzer.polarity_scores(passedTweet)
	

		
	if ss["compound"] >= 0.1:
		posComp.append(ss["compound"])
		
		
		
	elif ss["compound"] <= -0.1:
		negComp.append(ss["compound"])
		
		
	elif ss["compound"] == 0:
		nueComp.append(ss["compound"])
		

	return ss

removeNoise()


print "Positive"
print len(posComp)
print sum(posComp) / float(len(posComp))
print '\n'
print 'Negitive'
print len(negComp)
print sum(negComp) / float(len(negComp))
print '\n'
#print 'Nuetral'
#print len(nueComp)
#print sum(nueComp) / float(len(nueComp))


count = negComp + posComp  
count = map(lambda x:round(x,1), count)

## histogram
freq = [0]*21
for v in count:
	freq[int((v+1)*10)] += 1

for i,v in enumerate(freq):
	print '|'*v+'  '+str(i/10.0-1)