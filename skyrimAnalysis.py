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



def tokenizeWord():
	x = 0
	with open('skyrim.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
		for row in reader:
			
			#remove stop words from each row 
			filtWord = [word for word in row if word not in stopwords.words('english')]
			print x,filtWord
			x = x + 1 
			print '\n'




	



tokenizeWord()



#remove links 
#output = re.sub(r'\d+', '', word)


#tokenizer = RegexpTokenizer(r'\w+')
#remove numbers