from setup import *

# get transition counts, normalize to probability, then log transform

# Creating dictionary of transition counts
allowed_chars = string.ascii_lowercase + ' '
transition_dict = {k1:{k2: 0 for k2 in allowed_chars} for k1 in allowed_chars}

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
                # Fill in nested dictionary of transition_dict
                prev = line_clean[0]
                for item in line_clean[1:]:
                    transition_dict[prev][item] += 1
                    prev = item

# Normalize transition counts to get probability and then log transform
for i in transition_dict:
    norm = 1.0/sum(transition_dict[i].values()) # sum of all transition_dict from i
    transition_dict[i] = {j: math.log(count * norm)
                           if count != 0 else math.log(1e-20)
                           for j,count in transition_dict[i].items()
                           }
                          
# writing the dictionary of transition log likelihoods
with open('data/transition_likelihood.json', 'w') as writer:
  json.dump(transition_dict, writer, indent= 4)