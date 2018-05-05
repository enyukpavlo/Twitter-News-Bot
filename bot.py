import tweepy
from credentials import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dic = {'Liberal': 'Commie',
		'liberal': 'commie',
		'Conservative': 'Capitalistic pig',
		'conservative': 'capitalistic pig',
		'judge': 'big wig man',
		'investigation': 'whodunnit',
		'Senator': 'Elf-Lord',
		'witnesses': 'these dudes I know',
		'Russia': 'Land of Ice and Snow'}

for x in range(0, 180):
	f= open("fox_tweets.txt","w+")

	fox_news_tweets = api.user_timeline('FoxNews', count=1, tweet_mode='extended')
	for tweet in fox_news_tweets:
		f.write(tweet.full_text.encode('utf8'))

	f.close() 

	my_file = open("fox_tweets.txt", "r")

	file_lines = str(my_file.readlines())

	def replace_all(file_lines, dic):
   		for i, j in dic.iteritems():
   			file_lines = file_lines.replace(i, j)
    		return file_lines
	try:
		api.update_status(replace_all(file_lines, dic))
	except tweepy.TweepError as e:
		print(e.reason)

	print(x)

	x += 1

	sleep(20)

my_file.close()
