import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize

'''
reg ex library form nltk

from __future__ import devision 
from nltk, re, pprint 
from nltk import word_tokenoze

			for y in filtWord:
				output = re.sub(r'\d+', '', word)
				print x,output
				x = x + 1 
				print '\n'


'''



def removeNoise():
	x = 1
	with open('test.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';', quotechar = '"')
		for line in reader:
			tweet = line[4].split()
			words = [w for w in tweet if w not in stopwords.words('english')]
			tweet_clean = ' '.join(words)
			tweet_clean = re.sub(r'\d+', '', tweet_clean)
			tweet_clean = re.sub(r'[!\?\.,;"]', '', tweet_clean)
			print tweet_clean
			#remove stop words from each row 
			#filtWord = [word for word in row if word ] #not in stopwords.words('english')]
			#print x,filtWord
			#x = x + 1 
			#print '\n'



	



removeNoise()



#remove links 
#output = re.sub(r'\d+', '', word)


#tokenizer = RegexpTokenizer(r'\w+')
#remove punct