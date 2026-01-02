from collections import defaultdict
from rules import Easy21
from utils import e_greedy

def sarsa_lambda(lmbda,Q_star,episodes=1000,n0=100):
    env = Easy21()
    q = defaultdict(lambda: {0: 0.0,1: 0.0})
    n = defaultdict(int)
    N_sa = defaultdict(lambda: {0: 0,1: 0})
    mse_per_episode = []
    for ep in range(episodes):
        E = defaultdict(lambda: {0: 0.0,1: 0.0})
        state = env.reset()
        action = e_greedy(q,state,n,n0)
        done = False
        while not done:
            next_state,reward,done = env.step(state,action)
            n[state] += 1
            N_sa[state][action] += 1
            alpha = 1 / N_sa[state][action]
            if done:
                delta = reward - q[state][action]
            else:
                next_action = e_greedy(q,next_state,n,n0)
                delta = reward + q[next_state][next_action] - q[state][action]
            E[state][action] += 1
            for s in q:
                for a in q[s]:
                    q[s][a] += alpha * delta * E[s][a]
                    E[s][a] *= lmbda
            if not done:
                state,action = next_state,next_action
        mse = 0.0
        for s in Q_star:
            for a in Q_star[s]:
                mse += (q[s][a] - Q_star[s][a]) ** 2
        mse_per_episode.append(mse)
    return q,mse_per_episode
