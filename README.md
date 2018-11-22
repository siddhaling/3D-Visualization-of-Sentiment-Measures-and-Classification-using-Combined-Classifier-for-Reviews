# 3D Visualization of Sentiment Measures and Classification using Combined Classifier for Reviews

These are set of python program which perform sentiment analysis of the customer reviews and depict the sentiment information using 3D and 2D visualizations. The python code also support writing of statistics about the analyzed sentiment information into files. Few customer review files are included in the folder of AmazonReviews.

The steps carried out to perform visualization are shown in the below figure. The customer reviews which are in JSON format are read. Word tokenization is carried out and followed by stop words elimination. To remove the stop words, a data base of stop words is referred. Then the sentiment analysis of the review is performed using VADER sentiment analyzer. Then the sentiment information is depicted into various 3D and 2D visualizations.
![alt text](https://github.com/siddhaling/3D-Visualization-of-Sentiment-Measures-and-Classification-using-Combined-Classifier-for-Reviews/blob/master/fig1.jpg)

### 3D Surface Plot of SentimentInfo

The 3D surface plotting of sentiment information is carried out using the python code 3DSurfacePlotOfSentimentInfo_1.py. The surface plot depicts compound sentiment score against number of positive and negative words. Following is an example for 3Dsurface plot.
![alt text]()

### 3D Scatter Plot of SentimentInfo

The 3D scatter plot is scatter plot of number of positive, negative and neutral sentiment words is shown below. The program 3DScatterPlotOfSentimentInfo_2.py makes the 3D scatter plot. 
![alt text]()

### 3D Column Plot of SentimentInfo

The compound sentiment score is plotted as 3D columns with respect to number of positive and number of negative words. The python code 3DColumnPlotOfSentimentInfo_3.py displays 3D column plot.
![alt text]()

### Sentiment Statistics to Excel

The sentiment statistics such as negative, neutral, positive, compound score and number of positive, negative, neutral words are written to a excel sheet reviewsAndSenti.xls. The frequency and score related to words are also can be collected using the program sentimentStatisticsToExcel_4.py. AS an example the frequency and socre related to words is given in wordFreqScore100.xls


# Research Paper

This model of stock status prediction using tweet sentiment information has been appeared in research paper:

https://ieeexplore.ieee.org/document/8079788

https://www.youtube.com/watch?v=9AMdG_bnGFY

# Cite this work

Please cite as 

Siddhaling Urolagin, "Text Mining of Tweet for Sentiment Classification and Association with Stock Prices", IEEE International Conference on Computer and Applications (ICCA), pp 384-388, Dubai, 2017.

# Further Projects and Contact

For further reading and other projects please visit

www.researchreader.com

siddesh_u@yahoo.com


