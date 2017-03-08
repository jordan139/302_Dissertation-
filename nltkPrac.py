from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer 

from nltk.tag.stanford import StanfordNERTagger

text = "hello my na,me is jordan. I go to cov uni. i study computer science."

st = NERTagger(‘/usr/share/stanford-ner/classifiers/all.3class.distsim.crf.ser.gz’,
… ‘/usr/share/stanford-ner/stanford-ner.jar’)
st.tag("hello my na,me is jordan. I go to cov uni. i study computer science".split())