import sys
import json
import difflib
import StringIO
import string
import re
import ast

tweets_text = []
scores = {}
tweets_sing = []
tweets_score = []

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

def dictBuild(fq):
	afinnfile = open(fq)
	for line in afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = float(score)  # Convert the score to an integer.

def singleTweets():
	for i in tweets_text:
		tweets_sing.append(i.split())

def keyList(twList, seDict):
	for i in twList:
		miniLis = []
		for j in i:
			num = 0.0
			if j in seDict:
				miniLis.append(seDict[j])	
			else:
				miniLis.append(0.0)
		tweets_score.append(sum(miniLis))

def printOut(twList, twScore):
	for i,j in zip(twList, twScore):
		print '%s:%s'%(i, j)

def main():
	global sent_file
	global filename
    	sent_file = sys.argv[1]
    	filename = sys.argv[2]
    	dictBuild(sent_file)
    	jsonparse(filename)
    	singleTweets()
    	keyList(tweets_sing, scores)
    	printOut(tweets_text, tweets_score)
    	print tweets_score
    	

if __name__ == '__main__':
    main()

