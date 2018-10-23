#Tara Makarowski, CompSci1026B, Assignment 3
#This code perform simple sentiment analysis on Twitter data to determine which timezone is the “happiest"

# This function removes punctuation
# @ param is word to be removed of punctuation
def removePunctuation(word):
    newWord = ""
    for ch in word:
        if ch.isalpha():
            newWord += ch
    return newWord

# This function calculates the value of all the sentiment keywords found in the tweet
def processTweets(keys, words):
    #create variable for the total value of sentiment keywords in the tweet
    happyscore = 0
    #sentwords is the sentiment keywords
    sentwords = keys
    tweet = words
    #check to see if word in tweet is a sentinel keyword and calculates total value of sentiment keywords in tweet
    for i in range(len(tweet)):
        if tweet[i].lower() in sentwords:
            happyscore += sentwords[tweet[i].lower()]

    return happyscore


# create dictionary
##key = word
###value = sentiment value

keywords = {}
infile = input("Please enter file name here: ")
text = open(infile, "r", encoding="utf-8")
for line in text:
    element = line.split(",")
    keywords[element[0]] = int(element[1])

text.close()

#Create variables, set values for number of tweets, the total sentiment value for each timezone
tweetsEst, EstValue = 0, 0
tweetsCst, CstValue = 0, 0
tweetsMst, MstValue = 0, 0
tweetsPst, PstValue = 0, 0

#open and read the tweets file, find which timezone the tweet is in
file = input("Please enter file name here: ")
tweets = open(file, "r", encoding="utf-8")
for line in tweets:
    data = line.split()
    lat = float(data[0].strip("[,"))
    long = float(data[1].strip("]"))


    #find combined happiness value and calculate number of tweets in each timezone
    if 24.660845 <= lat <= 49.1897875:
        # est
        if -87.518395 <= long <= -67.444574:
            EstValue += processTweets(keywords, data)
            tweetsEst += 1
        # cst
        if -101.998892 <= long <= -87.518395:
            CstValue += processTweets(keywords, data)
            tweetsCst += 1
        # mst
        if -115.236428 <= long <= -101.998892:
            MstValue += processTweets(keywords, data)
            tweetsMst += 1
        # pst
        if -125.242264 <= long <= -115.236428:
            PstValue += processTweets(keywords, data)
            tweetsPst += 1
#finished reading tweets file, close tweets file
tweets.close()

#calculate average "happiness" value for each timezone
East = EstValue / tweetsEst
Cent = CstValue / tweetsCst
Mst = MstValue / tweetsMst
Pst = PstValue / tweetsPst

#print "happiness" score and number of tweets for each timezone
print("Eastern: ")
print(" happiness score: ", East, )
print(" number of tweets: ", tweetsEst)
print("Central: ")
print(" happiness score: ", Cent, )
print(" number of tweets: ", tweetsCst)
print("Mountain: ")
print(" happiness score: ", Mst, )
print(" number of tweets: ", tweetsMst)
print("Pacific: ")
print(" happiness score: ", Pst, )
print(" number of tweets: ", tweetsPst)

from happy_histogram import *
open("happy_histogram.py", "r")
drawSimpleHistogram(East, Cent, Mst, Pst)
