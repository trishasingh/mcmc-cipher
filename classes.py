# setup
from setup import *


class CodingFunc:

    def __init__(self, mapping):
        self.mapping = mapping

    @classmethod # inital map object
    def initMap(cls):
        """
        initialize map from code space to actual alphabet
        """
        init_map = {k:k for k in allowed_chars}
        return cls(init_map)

    def encrypt(self, text):
        mapping = {v:k for k,v in self.mapping.items()}
        return self.convert(mapping, text)

    def decrypt(self, text):
        return self.convert(self.mapping, text)

    def propose_transpd_func(self, old, new):
        mapping = self.mapping.copy()
        for k,v in mapping.items():
            if v == old:
                mapping[k] = new
                continue
            if v == new:
                mapping[k] = old
        return CodingFunc(mapping)

    @staticmethod
    def convert(mapping, text):
        """
        helper function for encrypt and decrypt
        """
        return "".join([mapping[c] for c in list(text)])


class Transitions:

    def __init__(self, text):
        self.chars = set(x for x in set(text) if x != ' ')
        # transition counts
        count = {k:{k:0 for k in allowed_chars} for k in allowed_chars}
        prev = text[0]
        for item in text[1:]:
            count[prev][item] += 1
            prev = item
        self.count = count

    def propose_transpd_trans(self, old, new):
        """
        returns transition counts after swapping characters
        """
        count = self.count.copy()
        temp_val = count[new]
        count[new] = count[old]
        count[old] = temp_val
        # update transition to old
        for k,v in count.items():
            temp_count = count[k][new]
            count[k][new] = count[k][old]
            count[k][old] = temp_count 
        return(count)

    def transpose_chars(self, old, new):
        self.chars.remove(old)
        self.chars.add(new)

    # @staticmethod
    def calc_plausibility(self, stationary_trans):
        """
        calculate plausibility score given transitions 
        for stationary coding func
        """
        plausibility = 1
        for trans_from,trans_dict in self.count.items():
            for trans_to,count in trans_dict.items():
                plausibility += (stationary_trans[trans_from][trans_to]
                                 * trans_dict[trans_to])
        return plausibility



