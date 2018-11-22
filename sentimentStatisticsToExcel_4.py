import os
import json
from collections import Counter
from sentimentVisualization import stopwordsRemove
from sentimentVisualization import getWords
from sentimentVisualization import sentimentScoresToMatrix
from sentimentVisualization import writeToExclReviewSentiStat
from sentimentVisualization import getWordFreqAndScore
from sentimentVisualization import writeTopSentiWordsToExcel

from vader import SentimentIntensityAnalyzer

AmazonReviewFldr='AmazonReviews'
#read the reviews from a folder
path = AmazonReviewFldr
filenames=[]
for filenm in os.listdir(path):
    print(filenm)
    filenames.append(filenm)
product=[]
reviewTitle=[]
reviewContent=[]
for i in range(len(filenames)):
    print(filenames[i])
    with open(path+'/'+filenames[i]) as dataFile:
        data=json.load(dataFile)
        product.append(data['ProductInfo'])
        for reviews in data['Reviews']:
            reviewTitle.append(reviews['Title'])
            reviewContent.append(reviews['Content'])

text = reviewContent  #text = read_file_2(3)
reviewTokens = [getWords(asdf) for asdf in text if asdf!=None]
stoppWrdRmdSentence = [stopwordsRemove(sentence) for sentence in reviewTokens]
sents = []
for i in stoppWrdRmdSentence:
    asdf = ''
    for j in i:
        asdf = asdf + j + ' '
    sents.append(asdf)
#perform sentiment analysis on reviews
sid = SentimentIntensityAnalyzer()

sentiment_scores = [sid.polarity_scores(sent) for sent in sents]
##represent sentiment score to matrixs
(matrix,numOfEle)=sentimentScoresToMatrix(sentiment_scores)
#write reviews and sentiments to excel
writeToExclReviewSentiStat(sents,sentiment_scores)

#perform sentiment analysis on all review comments
allReviews=' '.join(sent for sent in sents)
sentiment_scoresAllRevs =sid.polarity_scores(allReviews) # for all reviews
#compute word frequency
wordsAndFreqs= Counter(sentiment_scoresAllRevs['wordsWithEmotion'])
#compute word frequency and score
wordsFreqsScore=getWordFreqAndScore(sentiment_scoresAllRevs,wordsAndFreqs) 
#perform sorting words based on their sentiment score in descending order
sortwordsFreqsScoreTplBySenti=sorted(wordsFreqsScore.items(), key=lambda x: x[1][1],reverse=True)
#write sentiment words to excel
writeTopSentiWordsToExcel(sortwordsFreqsScoreTplBySenti,50)