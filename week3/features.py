import numpy as np
dealer_intervals = [(1,4),(4,7),(7,10)]
player_intervals = [(1,6),(4,9),(7,12),
                    (10,15),(13,18),(16,21)]
def f_vector(state,action):
    dealer,player = state
    f = np.zeros(36)
    index = 0
    for dl,dh in dealer_intervals:
        for pl,ph in player_intervals:
            for a in [0,1]:
                if (dl <= dealer <= dh and
                    pl <= player <= ph and
                    action == a):
                    f[index] = 1
                index += 1
    return f