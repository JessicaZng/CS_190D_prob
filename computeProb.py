import math

def nChooseK(n,k):
    fac = math.factorial
    return f(n) / f(k) / f(n-k)
    
def compute_prob(nTrials, numObserved): 
    return nChooseK(nTrials, numObserved) / (2**nTrials)
