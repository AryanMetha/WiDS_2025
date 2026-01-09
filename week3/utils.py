import random
def e_greedy(Q,state,n,n0=100):
    epsilon = n0 / (n0 + n[state])
    if random.random() < epsilon:
        return random.choice([0,1])
    else:
        return max(Q[state],key=Q[state].get)
