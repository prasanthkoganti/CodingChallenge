# example of program that calculates the number of tweets cleaned

import json
import re

fin = open('tweet_input/tweets.txt','r')
tweets = [json.loads(line) for line in fin]
fin.close()

cleantweets = []

for tweet in tweets:
    if 'text' in tweet.keys():
        tweet_text = tweet['text'].encode('ascii','ignore')	#remove unicode characters
	tweet_text.replace('\/','/')
	tweet_text.replace("\'", "'")
	tweet_text.replace('\"','"')
	tweet_text.replace('\n',' ')             
	tweet_text.replace('\t',' ')
	' '.join(text.split())             #remove extra whitespace
        cleantweets.append(tweet_text+ ' (timestamp: ' + tweet['created_at'] + ')\n')

fout = open('tweet_output/ft1.txt','w')
for cleantext in cleantweets:
    fout.write(cleantext)
fout.close()