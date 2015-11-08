# program that calculates the number of tweets cleaned
import sys
import json

def addTimeStamp(timestamp,unicodeRemovedTweet):
	return unicodeRemovedTweet+ " (timestamp: " + timestamp + ")"

def escapeCharacters(tweet):
	return tweet.strip().replace("\n", " ").replace("\t"," ")

#Clean Tweets - 1. Remove Unicode, 2.Escape Characters 3.Add TimeStamp
def cleanTweets(inputTweets):
	cleanedTweets = []
	noUnicodeTweets = 0
	for tweet in inputTweets:
		tweet = json.loads(tweet)
		if "text" in tweet and "created_at" in tweet:
			originalTweet = tweet["text"]
			unicodeRemovedTweet =  originalTweet.encode("ascii","ignore")
			if unicodeRemovedTweet!= originalTweet:
				noUnicodeTweets+=1
			unicodeRemovedTweet = escapeCharacters(unicodeRemovedTweet)
			unicodeRemovedTweet = addTimeStamp(tweet["created_at"],unicodeRemovedTweet)
			cleanedTweets.append(unicodeRemovedTweet)
	return (cleanedTweets,noUnicodeTweets)

#Print Instructions to run this code
def printUsage():
	print "Usage: python tweets_cleaned.py <input_file> <output_file>"

def main(argv):
	if len(argv) < 2 :
		printUsage()
		sys.exit(2)
	inputTweetsFile = argv[0]
	outputTweetsFile = argv[1]
	inputTweets = []

	#Read Input File, Read all tweets, and invoke cleanTweets()
	with open(inputTweetsFile,"r") as fIn :
		inputTweets = fIn.readlines()
	(cleanedTweets,noUnicodeTweets) = cleanTweets(inputTweets)

	#Clean the Output File if it already exists
	open(outputTweetsFile, 'w').close()

	#Save cleaned tweets and count of tweets with unicode in tweet text in output file.
	with open(outputTweetsFile,"w") as fOut:
		for cleanTweet in cleanedTweets:
			fOut.write(cleanTweet + "\n")
		fOut.write("\n" + str(noUnicodeTweets) +" tweets contained unicode.\n")

if __name__=="__main__":
	main(sys.argv[1:])
	sys.exit(0)