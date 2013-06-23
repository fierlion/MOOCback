import sys
import json
import difflib
import StringIO
import string
import re
import ast
from collections import Counter

tweets_text = []
tweets_sing = []
count_dict = {}

def jsonparse(fr):
	f = file(fr, "r")
	lines = f.readlines()
	for line in lines:
		try:
			tweet = json.loads(line)
		
			# Ignore retweets!
			if tweet.has_key("retweeted_status") or not tweet.has_key("text"): 
				continue
		
			pretext = tweet["text"].lower()
			text = pretext.encode("ascii", "ignore")
		
			# Ignore 'manual' retweets, i.e. messages starting with RT		
			if text.find("rt ") > -1:
				continue
		
			tweets_text.append( text )

		except ValueError:
			pass

def singleTweets(twee):
	k = " ".join(twee)
	return k.split()

def tweetFreq(tweSing):
	z = Counter(tweSing)
	for i in tweSing:
		print i.strip(), float(z[i])/len(singleTweets(tweets_text))

def main():
	global filename
    	filename = sys.argv[1]
    	jsonparse(filename)
    	tweets_sing = singleTweets(tweets_text) 
    	tweetFreq(tweets_sing)



if __name__ == '__main__':
    main()