import tweepy
from credentials import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#dicionary of terms to be subsituted
dic = {'Senator': 'Elf-Lord',
		'shirt': 'robe',
		'Shirt': 'Robe',
		'Attorney': 'Paladin',
		'attorney': 'paladin',
		'officer': 'knight-errant',
		'Officer': 'Knight-errant',
		'Electriciry': 'Magic',
		'electricity': 'magic',
		'Technology': 'Mage-craft',
		'technology': 'mage-craft',
		'Mayor': 'Minor noble',
		'mayor': 'minor noble',
		'Gun': 'Boomstick',
		'gun': 'boomstick',
		'Knife': 'Stabby thing',
		'knife': 'stabby thing',
		'judge': 'big wig man',
		'investigation': 'whodunnit',
		'witnesses': 'these dudes I know',
		'Russia': 'Land of Ice and Snow',
		'Car': 'Chariot',
		'Dog': 'Doggo',
		'dog': 'doggo',
		'Person': 'Human',
		'person': 'human',
		'People': 'Humans',
		'people': 'humans',}

#begin boot loop, opens and writes to the txt file that will hold the last tweet of targeted user
#encodes xyz-tweets.txt in UTF8 format since ASCI can't deal with emojis

for x in range(0, 180):
	f= open("fox_tweets.txt","w+")

	#'tweet_mode' has to be 'extended' otherwise it doesn't get the entire tweet
	#'count' is the number of number of last tweets to fetch
	fox_news_tweets = api.user_timeline('FoxNews', count=1, tweet_mode='extended')
	for tweet in fox_news_tweets:
		#encodes xyz-tweets.txt in UTF8 format since ASCI can't deal with emojis
		f.write(tweet.full_text.encode('utf8'))

	f.close() 

	#opens xyz_tweets.txt in read mode
	my_file = open("fox_tweets.txt", "r")

	#reads the lines of the tweet, turns them into a string, and assignes the string to file_lines
	file_strings = str(my_file.readlines())

	#replaces any keys that match any part of the tweet with the paired values
	def replace_all(file_lines, dic):
   		for i, j in dic.iteritems():
   			file_lines = file_strings.replace(i, j)
    		return file_strings
	try:
		api.update_status(replace_all(file_lines, dic))	#sends out the improved tweet
	except tweepy.TweepError as e:						#unless the last tweet hasn't changed
		print(e.reason)

	#prints out what iteration of the loop it is
	print(x)

	x += 1

	sleep(20)

my_file.close()
