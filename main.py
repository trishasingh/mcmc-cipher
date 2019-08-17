# setup
from setup import *

from classes import CodingFunc, Transitions


# reading in transition likelihoods at stationary coding func
# which is the true coding func f
with open('data/transition_likelihood.json', 'r') as reader:
    stationary_trans = json.load(reader)


# Metropolis Hastings

# test text
corpus = (
    "hindhnyrdhrg nd xrdreul uer xerut gtsqmlndx mlihzg nd tor fua ip tout "
    "hlugg ip tondzreg foi oukr mrrd ryshutry ti zdif ditondx ip tor toriea ip "
    "weimumnlntnrg tout toriea ti fonho tor qigt xlienisg imbrhtg ip osqud "
    "ergrueho uer ndyrmtry pie tor qigt xlienisg ip nllsgteutnidg ryxue ullrd "
    "wir tor qseyreg nd tor esr qiexsr qieworsg tong ng aise lugt houdhr uptre "
    "tong torer ng di tsedndx muhz ais tuzr tor mlsr wnll tor gtiea rdyg ais "
    "fuzr sw nd aise mry udy mrlnrkr foutrkre ais fudt ti mrlnrkr ais tuzr tor "
    "ery wnll ais gtua nd fidyreludy udy n goif ais oif yrrw tor eummnt oilr xirg"
)

# initialize random mapping
f = CodingFunc.initMap()
new_corpus = corpus
transitions = Transitions(new_corpus)
f_score = transitions.calc_plausibility(stationary_trans)

decoded = [False] * N_TRIALS
steps_list = [0] * N_TRIALS

for i in range(N_TRIALS):
    steps = 0
    for j in range(5000):
        old, new = np.random.choice(sampling_chars, 2, replace = False)
        f_proposed = f.propose_transpd_func(old, new)
        new_corpus = f_proposed.decrypt(corpus)
        trans_proposed = Transitions(new_corpus)
        f_score_proposed = trans_proposed.calc_plausibility(stationary_trans)
        acceptance_func = math.pow(math.e, f_score_proposed-f_score)
        if f_score_proposed > f_score or np.random.uniform(0,1) <= acceptance_func:
            f = f_proposed
            f_score = f_score_proposed
            steps += 1
    if f_score >= -1462:
        decoded[i] = True
    steps_list[i] = steps
    if i>0 and i%10==0:
        print("sim", i, "done")


print("success rate:", statistics.mean(decoded)) # success rate 40-100%
print("avg steps:", steps) #avg steps 40

# -1362.3854883396061 is the plausibility score of true f
