# Inisght Data Engineering  Challenge

## Task 1 Description
Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.
* Remove all unicode characters from tweet text
* Escape \' \" \\ \\/
* Replace \n and \t with a space

## Task 2 Description
The second feature will continually update the Twitter hashtag graph and hence, the average degree of the graph.
The graph should just be built using tweets that arrived in the last 60 seconds as compared to the timestamp of the latest tweet.
As new tweets come in, edges formed with tweets older than 60 seconds from the timstamp of the latest tweet should be evicted.

## Pre Requisites to Run the code
The code for these tasks are written in python. The code uses standard libraries of python 2.7

## Instructions to Run the code
1. clone the git repository
```
mkdir lkasinathan-insight-submission
cd lkasinathan-insight-submission
git clone git@github.com:kasinath/insight-data-engineering-challenge.git
```

2. Run run.sh from project root
```
cd inisght-data-engineering-challenge
./run.sh
```
