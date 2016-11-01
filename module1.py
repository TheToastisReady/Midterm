import statistics as st
#import matplotlib.pyplot as plt
import numpy as np
import math
import re
from collections import Counter
#% matplotlib inline

stopfile = open("stopwords.txt", "r");
with open("test.txt", "r", errors="ignore") as f:
    SCRPT = f.read();

stopwords = [];
sparse = [];
au = {};
ag = {};
speaker = "";

for a in stopfile:
    a = a.replace("\n", "");
    stopwords.append(a);

SCRPT = re.split("[ ]+\n\n", SCRPT);

for line in SCRPT:
    #letters_only = re.sub(r"[^a-zA-Z': ]", " ", line);
    letters_only = line;
    letters_only = letters_only.lower();
    words = letters_only.split();
    words = [w for w in words if not w in stopwords];
    sparse = words;
    
bb = 0;
bc = 0;
bd = 0;
be = 0;
for b in range(len(sparse)):
    #print(sparse[b]);
    if sparse[b] == "davis:":
        speaker = "d";
    elif sparse[b] == "austin:":
        speaker = "a";
    #print(speaker, "first loop");
    bb = b;
    while bb < len(sparse):
        #print(sparse[b][bb]);
        #print(speaker, "sec loop");
        bc = 0;
        temp = "";
        while bb+bc < len(sparse):
            #print(speaker, "third loop");
            if speaker == "d":
                temp+=sparse[bb+bc]+" ";
                ag[bb] = temp;
            elif speaker == "a":
                temp+=sparse[bb+bc]+" ";
                au[bb] = temp;
            bc+=1;
        bb+=1;

print("Dav:", ag);
print("Aus", au);
print(sparse);