import SentimentAnalysis as sa
import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\bikas\Desktop\demonetization-tweets.csv', encoding='iso-8859-1')
data.head()
data1 = data.loc[:, ['screenName', 'text', 'retweetCount', 'isRetweet']]
Total, sentiarray = sa.filereader()
average = sa.avg(sentiarray)
fivearray = sa.topfive(sentiarray)
bottom = sa.bottomfive(sentiarray)
data1['sentimentValue'] = sentiarray
retweetarray = np.array([])
retweetarray = np.append(retweetarray, data1.loc[:, 'retweetCount'])
print("maximum retweet count:", max(retweetarray))
print(data1.loc[data1.retweetCount == max(retweetarray), ['screenName', 'sentimentValue']])
retweetscreen_name = np.array([])
retweetscreen_name_new = np.append(retweetscreen_name, data1.loc[data1.retweetCount == max(retweetarray), ['screenName']])
# print(retweetscreen_name_new)
retweet_sentiment_value = np.array([])
retweetsentiment_value_new = np.append(retweetscreen_name, data1.loc[data1.retweetCount == max(retweetarray), ['sentimentValue']])
# print(retweetsentiment_value_new)
print("people with maximum positive sentiment:-\n",
      data1.loc[data1.sentimentValue == max(sentiarray), ['screenName', 'text', 'sentimentValue']])
# print("minimum positive:-\n", min(sentiarray))
print("\npeople with maximum negative sentiment:-\n",
      data1.loc[data1.sentimentValue == min(sentiarray), ['screenName', 'text', 'sentimentValue']])
# print("\naverage sentiment:", average)
# print("\ntop five sentiments:", fivearray)
print("people with top five sentiments:-\n")
print(data1.loc[data1.sentimentValue == fivearray[0], ['screenName', 'text', 'sentimentValue']])
possent = 0
negsent = 0
# print("bottom five sentiments:", bottom)
print("people with bottom five sentiments:\n")
for i in range(5):
    print(data1.loc[data1.sentimentValue == bottom[i], ['screenName', 'sentimentValue']])
for i in range(len(sentiarray)):
    if sentiarray[i] < 0:
        negsent += sentiarray[i]
    else:
        possent += sentiarray[i]
# print("total positive:", possent)
# print("total negative:", negsent)
newfivearray = np.array([])
newfivearray = np.append(fivearray, [1.29986737, 1.29986737, 1.29986737, 1.29986737, 1.29986737, 1.29986737,
                                     1.29986737, 1.29986737, 1.29986737, 1.29986737, 1.29986737])
# print(newfivearray)



