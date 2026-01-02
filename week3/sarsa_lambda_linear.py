import numpy as np
from rules import Easy21
from features import f_vector
import random

def q_value(theta,state,action):
    return np.dot(f_vector(state,action),theta)
def epsilon_greedy_linear(theta,state,epsilon=0.05):
    if random.random() < epsilon:
        return random.choice([0,1])
    else:
        q_hit = q_value(theta,state,0)
        q_stick = q_value(theta,state,1)
        return 0 if q_hit > q_stick else 1

def sarsa_lambda_linear(lmbda,Q_star,episodes=1000,alpha=0.01,epsilon=0.05):
    env = Easy21()
    theta = np.zeros(36)
    mse_per_episode = []
    for ep in range(episodes):
        E = np.zeros(36)
        state = env.reset()
        action = epsilon_greedy_linear(theta,state,epsilon)
        done = False
        while not done:
            next_state,reward,done = env.step(state,action)
            phi = f_vector(state,action)
            q_sa = np.dot(phi,theta)
            if done:
                delta = reward - q_sa
            else:
                next_action = epsilon_greedy_linear(theta,next_state,epsilon)
                q_next = q_value(theta,next_state,next_action)
                delta = reward + q_next - q_sa
            E = lmbda * E + phi
            theta += alpha * delta * E
            if not done:
                state,action = next_state,next_action
        mse = 0.0
        for s in Q_star:
            for a in Q_star[s]:
                q_hat = q_value(theta,s,a)
                mse += (q_hat - Q_star[s][a]) ** 2
        mse_per_episode.append(mse)
    return theta,mse_per_episode