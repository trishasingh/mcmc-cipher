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


class Transitions:

    def __init__(self, text):
        # transition counts
        count = defaultdict(dict)
        prev = text[0]
        for item in text[1:]:
            count[prev][item] = count[prev].setdefault(item, 0) + 1
            prev = item
        self.count = count

    def transposition(self, old, new):
        # steps: copy over dictionary, check key and swap
        # copy over inner dict, check key and swap 
        # TODO: fix naming in main.py, diff name for transitions

        count = self.count.copy()
        new_count = defaultdict(dict)
        for k,v in count.items():
            new_k = k
            if k == old:
                new_k = new
            if k == new:
                new_k == old 
            for k1,v1 in v.items():
                if k1 == old:
                    v[k1] = new 
                if k1 == new:
                    v[k1] = old
        return(count)



# x = CodingFunc({'a':'b', 'z':'y'})
# print(CodingFunc.initMap().mapping)

# TODO: how to handle if message doesnt have chars found in map

x = "i am so happy today yay"
x_transitions = Transitions(x)
print(x_transitions.count)
print(x_transitions.transposition('i', 'a'))
