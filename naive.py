from nltk import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain
import sys
reload(sys)
sys.setdefaultencoding('utf8')


training_data = [('6 more hours #HALO4','pos'),
('http:// Pornhub.com hits gone be low tonite #nerds #halo4 release 2nite','neg'),
('Since my #Halo4 is coming in the mail tomorrow, Ill be sending #Reach out in an appropriate form instead.','neg'),
('Tomorrow is the biggest day in the history of this country. Please go out and get #Halo4','pos'),
('Over a hundred people at the @GAME_Canterbury Halo4 launch ...and a short dude as Master Chief as predicted. (not 9ft) http:// yfrog.com/gzdewqxoj','pos'),
('#halo4 yes!!!!!!!!! pic.twitter.com/klVy6qg0','pos'),
('whos picking up #Halo4 tonight?','pos'),
('@JaaackPhelps too fucking right mate! #Halo4','pos'),
('The guns are great, they sound amazing. Map design is great and the graphics are amazing. #Halo4 is pretty good.','pos'),
('@Mike_Dege look whats trending bitch #Halo4','neg'),
('WHOS READY FOR HALO 4!? #Halo4 pic.twitter.com/Ia0TPhCO','pos'),
('@BullyBrew Hopefully Ill be picking up Halo4 tomorrow, if so, Ill start with the campaign because I have never played the multiplayer lol','neg'),
('#movember Day 5 #halo4 midnight launch. http:// instagr.am/p/Rqso5gKwG4/','pos'),
('#yeahmygirlfriend #whatsamelbournecup ? #halo4 danna_mac http:// instagr.am/p/RqsoNJi9Pp/','pos'),
('R. I. P. to the competition #Halo4','pos'),
('Gotta fuel up before I return to the fight! #halo4 @Chipotle Mexican Grill http:// instagr.am/p/Rqsm8hqa4K/','neg'),
('The recruits are lined up and ready #HALO4 pic.twitter.com/09NRjORN','pos'),
('Nearly time... #halo4 pic.twitter.com/eCxgbcEl','pos'),
('...and tell me again...why r we counting down the hours until Halo4 hits the streets??','pos'),
('Finally! #halo4 http:// instagr.am/p/Rqsmn4PHhy/','pos'),
('@FurrrSure wanna coop #Halo4 campaign?','pos'),
('Noobs will be tebagged tonight! #halo4','pos'),
('Was great fun playin #Halo4 @4damelane tonight tunes were pumpin @stevencooperdj','pos'),
('Halo4 all night...','pos'),
('5 hours and 1 min tell #halo4 #nerdstatus','pos'),
('5 hours. #Halo4','neg'),
('THE CHIEF IS BACK BABY FUCK YEAH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #Halo4 #AncientEvilAwakens','neg'),
('Dame torrow halo4 cant wait !!','neg'),
('I hate to say it, but Im not leaving my house for awhile after tonight #halo4','neg'),
('I bet #Halo4 will suck.','neg'),
('Time for some Deus Ex: Human Revolution, then the newest episode of #RedvsBlue and finally #EvilAwakens #John -117 in #Halo4 !','neg'),
('@AOTS Master Chief lives in my room #aots #halo4 http:// via.me/-6okrswe','neg'),
('31 & 13... Feeed mee moreee!!! Ahhhh #Halo4 WHO GON STOP ME HUHHHHHH?! http:// instagr.am/p/RqsirOoGlA/','neg'),
('On a misson to carms to get Halo4 with@JDswarez #UNSC #excited','neg'),
('Im queuing in fucking tescos for halo4 what is my life coming to...','neg'),
('#Halo4 in 8 hrs!!','neg'),
('I really cant wait till this game #halo4','neg'),
('Halo 4 Tourney info here! http:// theendgamesblog.com/?p=84 #Halo4 #Charlottesville','neg'),
('Bought #Halo4 back in march, now Im picking up @kpdoee to go grab it #stoked','neg'),
('HALO FUCKING 4 IS OUT IN 1MIN #halo4 #forwarduntodawn #masterchief #343','neg')

]

vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))

feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]

classifier = nbc.train(feature_set)

test_sentence = "This game looks so shit!!"
featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}

print "test_sent:",test_sentence
print "tag:",classifier.classify(featurized_test_sentence)