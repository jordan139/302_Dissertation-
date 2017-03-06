import csv 
import re 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords  	
from nltk import word_tokenize


def tokenizeWord():
	with open('skyrim.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
		for row in reader:


			for word in row:
				#remove stop words from each row 
				filtWord = [word for word in row if word not in stopwords.words('english')]
				
				print '\n'.join(row)



tokenizeWord()



#remove links 
#output = re.sub(r'\d+', '', word)


#tokenizer = RegexpTokenizer(r'\w+')
#remove numbers