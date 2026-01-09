import matplotlib.pyplot as plt
import numpy as np

# p_h=0.7
# iterations=1 # number of iterations for policy iteration(obviously more than 1)

# """
# Initialize parameters
# discount_factor=1
# value_estimates = np.zeros(101) 
# value_estimates[100] = 1  # terminal state value
# policy = np.ones(100,dtype=int)  # initial policy: bet 1,ensure integer type
# policy[0] = 0  # state 0 is terminal,no bet
# """

# for iteration in range(iterations):
#     pass
#     #step 1 :evaluation of policy:inital policy is to bet 1
#     #step 2: new policy = greedy (value function with previous policy)
    
# # Plotting the value function for some iterations to visualize convergence
# # Plot final policy

def fun(p_h,iterations=100):
    V = np.zeros(101)
    V[100] = 1.0   
    data = []

    for iteration in range(iterations):
        v_o = V.copy()

        for s in range(1,100):
            actions = range(1,min(s,100-s)+1)
            action_values = [p_h*v_o[s+a]+(1-p_h)*v_o[s-a] for a in actions]
            V[s] = max(action_values)
        data.append(V.copy())
    policy = np.zeros(101,dtype=int)

    for s in range(1,100):
        actions = range(1,min(s,100-s)+1)
        action_values = [p_h*V[s+a]+(1-p_h)*V[s-a] for a in actions]
        policy[s] = actions[np.argmax(action_values)]

    return V,policy,data




p_values = [0.2,0.4,0.5,0.7,0.9]
for p_h in p_values:
    V,policy,data = fun(p_h)
    # for value function
    for i in [0,1,2,len(data)-1]:
        plt.plot(data[i],label=f"iteration {i+1}")
    plt.xlabel("Capital")
    plt.ylabel("Value")
    plt.title(f"Value Function (p_h = {p_h})")
    plt.legend()
    plt.show()
    
    # for opt policy
    plt.plot(range(101),policy)
    plt.xlabel("Capital")
    plt.ylabel("Stake")
    plt.title(f"Optimal Policy (p_h = {p_h})")
    plt.show()
