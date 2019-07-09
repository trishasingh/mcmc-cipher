import string
import numpy as np

class CipherMap:

    def __init__(self, mapping):
        self.mapping = mapping

    @staticmethod
    def staticTest(self):
        print(self.mapping)

    @classmethod # inital map object
    def initMap(cls):
        chars = list(' ' + string.ascii_lowercase)
        random_chars = list(np.random.choice(chars, len(chars), replace = False))
        init_map = {k: v for k,v in zip(chars, random_chars)}
        return cls(init_map)

    def encrypt(self, mapping):
        d = self.mapping
        

x = CipherMap({'a':'b', 'z':'y'})
# using static method for namespace
CipherMap.staticTest(x)
print(CipherMap.initMap().mapping)