from collections import defaultdict
from rules import Easy21
from utils import e_greedy

def mc_control(episodes=200000,N0=100):
    env = Easy21()
    q = defaultdict(lambda:{0:0.0,1:0.0})
    n = defaultdict(int)
    N_sa = defaultdict(lambda:{0:0,1:0})
    for i in range(episodes):
        episode = []
        state = env.reset()
        done = False
        while not done:
            n[state] += 1
            action = e_greedy(q,state,n,N0)
            next_state,reward,done = env.step(state,action)
            episode.append((state,action))
            state = next_state
        G = reward 
        for (s,a) in episode:
            N_sa[s][a] += 1
            alpha = 1/N_sa[s][a]
            q[s][a] += alpha * (G - q[s][a])
    return q