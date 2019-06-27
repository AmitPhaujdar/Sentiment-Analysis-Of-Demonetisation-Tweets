import csv
import re
from nltk.tokenize import word_tokenize
import math
import numpy as np
afinn = {}


with open(r'C:\Users\bikas\Downloads/sentiments.txt') as SentimentFile:
    for row in SentimentFile:

        afinn[row.split('\t')[0]] = int(row.split('\t')[1].strip())


emoticons_str = r'(?:[:=;][oO\-]? [D\)\]\(\]/\\OpP])'

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    # URLs
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')',
                       re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$',
                         re.VERBOSE | re.IGNORECASE)


def sentiment(words):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence.
    """
    # words = pattern_split.split(text.lower())

    sentiments = map(lambda word: afinn.get(word, 0), words)

    if sentiments:
        # How should you weight the individual word sentiments?
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        # sntmnt = float(sum(sentiments)) / math.sqrt(len(sentiments))
        sntmnt = float(float(sum(sentiments)) / math.sqrt(29))
        # print("doing inside func:", sntmnt)
        # print("sum: ", float(sum(sentiments)))

        # print("doing inside func:", sntmnt)
    else:
        sntmnt = 0
    return sntmnt


def tokenize(s):
    # return tokens_re.findall(s)
    return word_tokenize(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(
            token) else token.lower() for token in tokens]
    return tokens


def filereader(total=0):
    """
    This has been used to read the csv file
    :return read handler
    """
    sentiarr = np.array([])
    with open(r'C:\Users\bikas\Desktop\demonetization-tweets.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                tweet = row['text']
                total += sentiment(preprocess(tweet))
                sentiarr = np.append(sentiarr, sentiment(preprocess(tweet)))
            except UnicodeDecodeError:
                # There are some characters which can not be handled by Python
                # We need to ignore those characters
                pass

        return total, sentiarr


def avg(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]

    avg = result / len(arr)
    return avg


def topfive(arr):
    arr.sort()
    arr1 = np.array([])
    for i in range(len(arr)-5, len(arr)):
        arr1 = np.append(arr1, arr[i])

    return arr1


def bottomfive(arr):
    arr.sort()
    arr1 = np.array([])
    for i in range(0, 5):
        arr1 = np.append(arr1, arr[i])

    return arr1


def main():
    """
    main paragraph to handle the processes
    :return:
    """
    negsent = 0
    possent = 0
    Total, sentiarray = filereader()
    print("Total:", Total)
    print("final array:", sentiarray)
    for i in range(len(sentiarray)):
        if sentiarray[i] < 0:
            negsent += sentiarray[i]
        else:
            possent += sentiarray[i]
    average = avg(sentiarray)
    fivearray = topfive(sentiarray)
    bottom = bottomfive(sentiarray)
    print("size of array:", len(sentiarray))
    print("maximum positive:", max(sentiarray))
    print("maximum negative:", min(sentiarray))
    print("average sentiment:", average)
    print("top five sentiments:", fivearray)
    print("bottom five sentiments:", bottom)
    print("total positive:", possent)
    print("total negative:", negsent)
    if Total > 0:
        print(" General sentiment is Positive sentiments")
    else:
        print(" General sentiment is Negative sentiments")


if __name__ == "__main__":
    main()
