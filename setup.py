import os, re, math, statistics, random
import string, json
import numpy as np
from collections import defaultdict
from scipy import stats

allowed_chars = list(string.ascii_lowercase + ' ')
sampling_chars = list(string.ascii_lowercase)

N_TRIALS = 100