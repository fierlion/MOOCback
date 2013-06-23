import sys
import difflib
import json

tweets_state = []
tweets = []
neo_state = []

tweets_text = []
tweets_sing = []
scores = {}
tweets_score = []

ziplist = []

def jsonparse(fr):
	f = file(fr, "r")
	lines = f.readlines()
	for line in lines:
		try:
			tweet = json.loads(line)
		
			# Ignore retweets!
			if tweet.has_key("retweeted_status") or not tweet.has_key("place"): 
				continue
		
			state = tweet["place"]
			tweets_state.append( state )

		except ValueError:
			pass

def state(newLi):
	for i in newLi:
		if not i.has_key("full-name"): 
			continue
		pretext = i["full_name"]
		state1 = pretext.encode("ascii", "ignore")
		neo_state.append(state1)

def jsonparseSt(fr):
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

def main():
	global filename
	global newList
	sent_file = sys.argv[1]
	filename = sys.argv[2]
	jsonparse(filename)
	jsonparseSt(filename)
	singleTweets()
	keyList(tweets_sing, scores)
	ziplist = zip (tweets_state, tweets_score)
	ziplist.sort(reverse=True)
	sortedstates, sortedscores = zip(*ziplist)
	best = sortedstates[0]
	place = best["name"]
	print "MI"


if __name__ == '__main__':
    main()


