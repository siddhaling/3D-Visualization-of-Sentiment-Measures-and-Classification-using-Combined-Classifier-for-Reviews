# 3D Visualization of Sentiment Measures and Classification using Combined Classifier for Reviews

These are set of python program which performs sentiment analysis of the customer reviews and depicts the sentiment information using 3D and 2D visualizations. The python code also writes the detailed statistics about the analyzed sentiment information into the files. Examples for few customer review files are included in the folder of AmazonReviews.

The steps carried out to perform sentiment visualization of customer reviews are shown in the below figure. The customer reviews which are in JSON format are read as input. Word tokenization is carried out and followed by stop words elimination. To remove the stop words, a database of stop words is referred. Then the sentiment analysis of the review is performed using VADER sentiment analyzer. The sentiment information is depicted into various 3D and 2D visualization schemes.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/fig1.jpg)

### 3D Surface Plot of SentimentInfo

The 3D surface plotting of sentiment information is carried out using the python code 3DSurfacePlotOfSentimentInfo_1.py. The surface plot depicts compound sentiment score against a number of positive and negative words. Following is an example for the 3Dsurface plot.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/3DSurface.jpg)

### 3D Scatter Plot of SentimentInfo

The 3D scatter plot is generated as the plot of a number of positive, negative and neutral sentiment words is shown below. The program 3DScatterPlotOfSentimentInfo_2.py makes the 3D scatter plot.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/3DScatter.jpg)

### 3D Column Plot of SentimentInfo

The compound sentiment score is plotted as 3D columns with respect to a number of positive and number of negative words. The python code 3DColumnPlotOfSentimentInfo_3.py displays 3D column plot.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/3DColumn.jpg)

### Sentiment Statistics to Excel

The sentiment statistics such as negative, neutral, positive, compound score and number of positive, negative, neutral words are written to the excel sheet reviewsAndSenti.xls. 

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/reviewsAndSenti.jpg)

The frequency and score related to words are also can be collected using the program sentimentStatisticsToExcel_4.py. AS an example the frequency and score related to words is given in wordFreqScore100.xls

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/wordFreqScore100.jpg)

### Donut Charts for SentimentInfo

Two donut chart can be obtained using the python program donutGraphsForSentimentInfo_5.py. Top ten positive words along with their score and top ten negative words along with their score are depicted using the donut chart. Following are the examples.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/donutPositiveWords.jpg)

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/donutNegativeWords.jpg)

### Review Sentiment Classification

The sentiment classification of Amazon reviews is performed as shown in the figure below. The customer reviews are read from JSON files. Preprocessing of reviews is carried out such as word tokenization and stop word removal. From the collection of reviews, using most common words a bag of words is created. From each review feature vectors are formed and further classification is performed using SVM. The sentiment classification is given in python code reviewSentimentClassification_6.py.

![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/fig2.jpg)
# Research Paper

The full research paper 3D visualization of sentiment information and sentiment classification of reviews is available (OPEN ACCESS): 

http://thesai.org/Publications/ViewPaper?Volume=9&Issue=5&Code=IJACSA&SerialNo=8

# Cite this work

Please cite as 

Siddhaling Urologin, Sunil Thomas, "3D Visualization of Sentiment Measures and Sentiment Classification using Combined Classifier for Customer Product Reviews",  International Journal of Advanced Computer Science and Applications (IJACSA), Volume 9 Issue 5, pp. 60-68, June 2018. 

# Further Projects and Contact

For further reading and other projects please visit

www.researchreader.com

Dr. Siddhaling Urolagin,\
PhD, Post-Doc, Machine Learning and Data Science Expert,\
Passioinate Researcher, Focus on Deep Learning and its applications,\
dr.siddhaling@gmail.com



