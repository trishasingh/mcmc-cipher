# setup
import os
import re
from collections import defaultdict
import numpy as np
import string

from classes import CodingFunc

# Creating data
transitions = defaultdict(dict)

# read in War and Peace downloaded from Project Gutenberg: http://www.gutenberg.org/ebooks/2600
with open("data/war_and_peace.txt", 'r') as reader:
    start = False
    for line in reader:
        # replace anything that's not a letter with a space, then remove double or more spaces
        line_clean = re.sub('[\s]{2,}', ' ' ,re.sub('[^a-z\s]', ' ', line.lower())).strip()
        # specify starting point
        if line_clean.startswith("well prince so genoa"):
            start = True
        if start:
            # specify ending point
            if line_clean.startswith("end of the project gutenberg ebook of war and peace"):
                break
            # remove empty lines and chapter titles
            if  not (line_clean == '\n' or line_clean == '' or line_clean.startswith('chapter')):
                # Fill in nested dictionary of transitions
                prev = line_clean[0]
                for item in line_clean[1:]:
                    transitions[prev][item] = transitions[prev].setdefault(item, 0) + 1
                    prev = item

# Normalize transition probabilities (round to 4 places)
for i in transitions:
    norm = 1.0/sum(transitions[i].values()) # sum of all transitions from i
    transitions[i] = {j: round(count * norm, 4) for j,count in transitions[i].items()}


# Initialize random mapping
chars = list(' ' + string.ascii_lowercase)
random_chars = list(np.random.choice(chars, len(chars), replace = False))

init_map = dict()

for k,v in zip(chars, random_chars):
    init_map[k] = v

print(init_map)


# clue for transpositions

print({'a': 'b', 'b': 'c'}['a'])


# HELPER FUNCTIONS

def cleanText(x):
    # clean raw text input
    # try with tst from test pipeline
    return [x for x in re.sub('[\s]{2,}', ' ' ,re.sub('[^a-z\s]', ' ', x.lower())).strip()]


#TODO: create function for text cleaning, return none if blank space etc
#TODO: populate setup.py and source all files
