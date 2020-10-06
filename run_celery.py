# from __future__ import absolute_import
from celery import Celery
import os
import re
import json
import itertools
import collections
import matplotlib.pyplot as plt

app = Celery('celery', broker='amqp://v:v@localhost:5672/v', backend='rpc://')

def clean(txt):
    # use regular expression to remove url and emoji
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

@app.task
def count():
    path = "./data/"
    files = os.listdir(path)
    temp = {}
    words = []
    num = 0
    for file in files:
        with open(path + os.sep + file, 'r') as f:
            print("Processing file: " + f.name)
            for line in f:
                # ignore blank lines
                if not line.isspace():
                    # disregard retweets
                    if "retweeted_status" in json.loads(line):
                        continue
                    else:
                        # count unique tweets
                        num += 1
                        # get context without url & emoji
                        pre = clean(json.loads(line)["text"])
                        # transfer into lower letter and split into words
                        words.append(pre.lower().split())
        flat_words = list(itertools.chain(*words))
        countsAll = collections.Counter(flat_words)

        pronouns = 'han', 'hon', 'den', 'det', 'denna', 'denne', 'hen'
        counts = {}
        for p in pronouns:
            if p in countsAll:
                counts[p] = countsAll[p]
            else:
                counts[p] = 0
        if temp == {}:
            temp = counts
        else:
            for k in temp.keys():
                temp[k] = temp.get(k)+counts.get(k)
    with open('result.json', 'w') as j:
       jf =  json.dump(temp, j)

    result = []
    for i in list(temp.values()):
        result.append(i / num)
    
    plt.barh(list(temp.keys()), result)
    plt.xlabel("frequency (the number of metions normalized by the number of unique tweets)")
    plt.ylabel("words")
    plt.title("Frequencies of Swedish Pronouns Found in Tweets (Disregarding Retweets)")
    plt.savefig('visualization.png')
