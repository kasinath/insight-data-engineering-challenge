import sys
import json
import time
import itertools
import datetime

def getHashTags(hashtags):
    tags = []
    for tag in hashtags:
        tag = (tag["text"]).encode("ascii","ignore").lower()
        if len(tag) > 0:
            tags.append(tag)
    return tags

def lessThanAMinute(time1,time2):
    ts1 =  datetime.datetime.strptime(time1,'%a %b %d %H:%M:%S +0000 %Y')
    ts2 =  datetime.datetime.strptime(time2,'%a %b %d %H:%M:%S +0000 %Y')
    tDelta = ts2 - ts1
    return tDelta.total_seconds() <= 60

def extractHashTagsAndTimestamps(inpTweets):
    tweets = [];
    for t in inpTweets:
        t = json.loads(t)
        if not("created_at" in t or "text" in t):
            continue
        tweet = {}
        tweet["created_at"] =  t["created_at"]
        tweet["hashtags"] = getHashTags(t["entities"]["hashtags"])
        tweets.append(tweet)
    return tweets

def getHashTagLinks(tags):
    return itertools.permutations(tags,2)

def generateGraph(tweets):
    avgDegree = []
    graph = {}
    i = 0  # Oldest Tweet within 60 seconds from Current Tweetfo
    j = 0  # Current Tweet
    for j in range(len(tweets)):
        while(not lessThanAMinute(tweets[i]["created_at"],tweets[j]["created_at"])):
            #Remove links
            if len(tweets[i]["hashtags"]) > 1:
                removeEdges = getHashTagLinks(tweets[i]["hashtags"])
                for edge in removeEdges:
                    graph[edge[0]].remove(edge[1])
            i+=1

        #Add Links
        if len(tweets[j]["hashtags"]) > 1:
            addEdges = getHashTagLinks(tweets[j]["hashtags"])
            for edge in addEdges:
                if edge[0] in graph:
                    graph[edge[0]].append(edge[1])
                else:
                    graph[edge[0]] = [edge[1]]

        #Count Degree
        degree = 0.0
        if len(graph) ==0:
            avgDegree.append(format(0.00,'.2f'))
        else:
            for node in graph:
                degree += len(set((graph[node])))
            avgDegree.append(format(round(degree/len(graph),2),'.2f'))
    return avgDegree

#Print Instructions to run this code
def printUsage():
    print "Usage: python average_degree.py <input_file> <output_file>"

def main(argv):
    if len(argv) < 2 :
        printUsage()
        sys.exit(2)
    inputTweetsFile = argv[0]
    outputTweetsFile = argv[1]
    inputTweets = []

    #Read Input File and save all input tweets in memory
    with open(inputTweetsFile,"r") as fIn :
        inputTweets = fIn.readlines()

    #Extract HashTag List and Timestamp for each tweet
    inputTweets = extractHashTagsAndTimestamps(inputTweets)

    #GenerateGraph for every tweet
    output = generateGraph(inputTweets)

    #Clean the Output File if it already exists
    open(outputTweetsFile, 'w').close()

    #Save Avg Degree for each incoming tweet
    with open(outputTweetsFile,"w") as fOut:
        for avgDegree  in output:
            fOut.write(str(avgDegree) + "\n")

if __name__=="__main__":
    main(sys.argv[1:])
