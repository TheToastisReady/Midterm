# -*- coding: utf-8 -*-
"""
Sonnet Analyzer
Emma Anderson
March 2016
"""

from collections import Counter
import re
stopfile = open("stopwords.txt", "r")
with open("sonnets.txt", "r", errors="ignore") as f:
    textfile = f.read()
stopwords = []
for ii in stopfile:
    ii = ii.replace("\n", "")
    stopwords.append(ii)
textfile = re.split("[CLXVI]+\n\n", textfile)

wordcountlist = []
tflist = []
for sonnet in textfile:
    letters_only = re.sub("[^a-zA-Z]", " ", sonnet)
    letters_only = letters_only.lower()
    words = letters_only.split()
    words = [w for w in words if not w in stopwords]   
    wordcount = Counter(words)
    wordcountlist.append(wordcount)
    tf = {}
    for key in wordcount:
        tf[key] = wordcount[key]/len(wordcount)
    tflist.append(tf)

overall_count = {}
for element in wordcountlist:
    for key in element:
        if key not in overall_count:
            overall_count[key] = 1;
        else:
            overall_count[key]+=1

idft = {}
for key in overall_count:
    idft[key] = len(wordcountlist)/overall_count[key]