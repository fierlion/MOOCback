import sys
import json
import difflib
import StringIO
import string
import re
import ast

tweets_text = []
tweets_sing = []

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

def singleTweets():
	for i in tweets_text:
		tweets_sing.append(i.split())

def main():
	global sent_file
	global filename
    	filename = sys.argv[1]
    	jsonparse(filename)
    	singleTweets()
    	print tweets_text
    	print tweets_sing
    	
if __name__ == '__main__':
    main()
