#!/bin/bash

#TEST TASK 1 ESCAPE CHARACTERS
#python src/tweets_cleaned.py tweet_input/TEST_TASK1_escape.txt weet_output/TEST_TASK1_escape.txt

#TEST TASK 1 unicode characters
#python src/average_degree.py tweet_input/TEST_TASK1_unicode.txt tweet_output/TEST_TASK1_unicode.txt

#TEST TASK 2 GRAPH -TEST CASES INCLUDE ZERO NODES
#python src/average_degree.py tweet_input/TEST_TASK2_graph.txt tweet_output/TEST_TASK2_graph.txt

#ACTUAL INPUT
echo -e '##############################################################################'
echo '                            TASK 1                   '
echo -e '##############################################################################'
echo 'Starting Task 1'
echo -e 'Input File : tweet_input/tweets.txt'
python src/tweets_cleaned.py tweet_input/tweets.txt tweet_output/ft1.txt
echo 'Task 1 Completed'
echo -e 'Output File : tweet_output/ft1.txt\n\n'

echo -e '##############################################################################'
echo '                            TASK 2                  '
echo -e '##############################################################################'

echo 'Starting Task 2'
echo 'Input File : tweet_input/tweets.txt'
python src/average_degree.py tweet_input/tweets.txt tweet_output/ft2.txt
echo 'Task 2 Completed'
echo -e 'Output File : tweet_output/ft2.txt\n'