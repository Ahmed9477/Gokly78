from math import log10
import os
import re

def tf(filename:str) -> dict:
    Lwords = []
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            for word in re.split('[-.,\' \n]', line):
                Lwords.append(word)
    tfscore = {}
    for elem in Lwords:
        if elem in tfscore:
            tfscore[elem] += 1
        else:
            tfscore[elem] = 1
    return tfscore
