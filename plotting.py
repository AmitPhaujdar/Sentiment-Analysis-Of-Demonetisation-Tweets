import EssentialData as ex
import matplotlib.pyplot as plt
import numpy as np
# for plotting total positive/ total negative against sentiment values
print("data set for Total Sentiment: Positive/Negative :\n")
sentimentplot = [ex.possent, ex.negsent]
xlabel = ['Total Positive', 'Total Negative']
print(sentimentplot)
plt.bar(xlabel, sentimentplot, align='center')
plt.xlabel('Total Sentiment')
plt.ylabel('Sentiment Value')
plt.title("Total Sentiment: Positive/Negative ")
plt.show()
# for plotting Sentiment Extremities: Positive/Negative
print("data set for Sentiment Extremities: Positive/Negative:\n")
maxminplot = [max(ex.sentiarray), ex.average, min(ex.sentiarray)]
xlabel = ['Max Positive', 'average', 'Max Negative']
print(maxminplot)
plt.bar(xlabel, maxminplot, align='center')
plt.xlabel('Sentiment Label')
plt.ylabel('Sentiment Value')
plt.title(" Sentiment Extremities: Positive/Negative ")
plt.show()
# for plotting Top 5 Negative Influences
print("data set for Top 5 Negative Influences:\n")
bottomlabel = np. array([])
for i in range(5):
    bottomlabel = np.append(bottomlabel, ex.data1.loc[ex.data1.sentimentValue == ex.bottom[i], ['screenName']])
bottomlabel = np.unique(bottomlabel)
print(bottomlabel)
plt.bar(bottomlabel, ex.bottom)
plt.xticks(rotation='vertical')
plt.xlabel('ScreenName')
plt.ylabel('Sentiment Value')
plt.title(' Top 5 Negative Influences ')
plt.show()
# for plotting Top  Positive Influences
print("data set for Top  Positive Influences:\n")
toplabel = np. array([])
toplabel = np.append(toplabel, ex.data1.loc[ex.data1.sentimentValue == ex.fivearray[0], ['screenName']])
toplabel = np.unique(toplabel)
print(toplabel)
print(ex.newfivearray)
plt.bar(toplabel, ex.newfivearray)
plt.xticks(rotation='vertical')
plt.xlabel('ScreenName')
plt.ylabel('Sentiment Value')
plt.title('Top  Positive Influences')
plt.show()
# for plotting Top  Re-tweeted Users' sentiment Values
print("data set for Top  Re-tweeted Users' sentiment Values:\n")
print(ex.retweetscreen_name_new)
print(ex.retweetsentiment_value_new)
plt.bar(ex.retweetscreen_name_new, ex.retweetsentiment_value_new)
plt.xticks(rotation='vertical')
plt.xlabel('ScreenName')
plt.ylabel('Sentiment Value')
plt.title("Top  Re-tweeted Users' sentiment Values ")
plt.annotate("Re-tweetCount=5170.0", xy=(0, 0.2))
plt.show()
