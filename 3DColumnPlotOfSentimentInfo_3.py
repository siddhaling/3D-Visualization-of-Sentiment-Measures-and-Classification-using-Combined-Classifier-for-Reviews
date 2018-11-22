import os
import json
from sentimentVisualization import stopwordsRemove
from sentimentVisualization import getWords
from sentimentVisualization import sentimentScoresToMatrix
from sentimentVisualization import plotMatrix3DColumnByMatPlotLib

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
#perform 3D column chart of sentiment score
plotMatrix3DColumnByMatPlotLib(sentiment_scores,mangifyFactor=5)
