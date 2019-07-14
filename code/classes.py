import string
import numpy as np
from collections import defaultdict

class CodingFunc:

    def __init__(self, mapping):
        self.mapping = mapping

    @classmethod # inital map object
    def initMap(cls):
        chars = list(' ' + string.ascii_lowercase)
        random_chars = list(np.random.choice(chars, len(chars), replace = False))
        init_map = {k: v for k,v in zip(chars, random_chars)}
        return cls(init_map)

    def encrypt(self, mapping):
        d = self.mapping


class Corpus:

    def __init__(self, text):
        # original text
        self.text = text
        # transitions map
        transitions = defaultdict(dict)
        prev = self.text[0]
        for item in self.text[1:]:
            transitions[prev][item] = transitions[prev].setdefault(item, 0) + 1
            prev = item
        self.transitions = transitions


# x = CodingFunc({'a':'b', 'z':'y'})
# print(CodingFunc.initMap().mapping)

# TODO: how to handle if message doesnt have chars found in map

x = Corpus("i am so happy today yay")
print(x.text)
print(x.transitions)
