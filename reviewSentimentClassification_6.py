import os
import nltk
import random
from nltk import word_tokenize
from vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sklearn.model_selection import cross_val_score
from sklearn import svm
#path containing customer reviews
amazonRevFldr='AmazonReviews'

#obtain the words in a sentence
def getWords(sentence):
	return word_tokenize(sentence)
#remove stopwords and retun the list
def stopwordRemove(wordlist):
	stopword_list = set(stopwords.words('english'))
	return [stopped for stopped in wordlist if stopped not in stopword_list]
#form the feature vector from the given text files
def formFeaturesFromDocs(document):
    words=set(document)
    features={}
    for w in wordsCollectAsFeatures:
        features[w]=(w in words)
    return features
#collect all file name from the given path
def collectAllFileNms(path):
    filenames=[]
    for filenm in os.listdir(path):
        filenames.append(filenm)
    return filenames
#collect all the reviews from the files
def collectAllReviews(filenames,amazonRevFldr):
    reviewContent=[]
    for i in range(len(filenames)):
        print(filenames[i])    
        with open(amazonRevFldr+'/'+filenames[i]) as dataFile:
            reviewContent.extend(dataFile.read().splitlines())
    return reviewContent


filenames=collectAllFileNms(amazonRevFldr)

reviewContent=collectAllReviews(filenames,amazonRevFldr)
#preprocessing the customer reviews        
reviewTokens = [getWords(asdf) for asdf in reviewContent if asdf!=None]
stopWordRmdLst = [stopwordRemove(sentence) for sentence in reviewTokens]

sents = []
for i in stopWordRmdLst:
    asdf = ''
    for j in i:
        asdf = asdf + j + ' '
    sents.append(asdf)

sid = SentimentIntensityAnalyzer()

sentimentScores=[]
#choose valid sentiment oputput
for sent in sents:
    if(len(sent)>0):
        sentimentScores.append(sid.polarity_scores(sent))

#make the sentiment classes as positive and negative
documents=[]
for si in sentimentScores:    
    if si['compoundScore']>=0:
        category=1#'pos'
    else:
        category=0#'neg'
    documents.append((list(si['wordsWithEmotion']),category))

random.shuffle(documents)

allWords=[]
for si in sentimentScores:
    lowerCaseWords=[w.lower() for w in si['wordsWithEmotion']]
    allWords.extend(lowerCaseWords)
#collect frequency of all words
allWords=nltk.FreqDist(allWords)
print(allWords.most_common(15))
#choose most common word to create feature vector
wordsCollectAsFeatures=[ai[0] for ai in allWords.most_common(6000)]

print((formFeaturesFromDocs(sentimentScores[0]['wordsWithEmotion'])))

featuresets=[(formFeaturesFromDocs(rev),category) for (rev,category) in documents]

#prepare the data for training
X=[]
y=[]
for i in range(len(featuresets)):
    X.append(list(featuresets[i][0].values()))
    y.append(featuresets[i][1])

clf=svm.SVC()
#perform the cross validation
scores=cross_val_score(clf,X,y,cv=5)
print(scores)
print('Accuracy=',scores.mean(),'Std deviation=',scores.std()*2)