import numpy as np
import matplotlib.pyplot as plt


def compute_action_profile(players, i):
    empty = np.zero(17,2)

    

def total_transmission_power(players, sensing_d):

    a1, a2 = 1, 1
    total = 0

    for i in range(17):
        for j in range(17):
            if(j != i):
                distance = np.linalg.norm( players[i]-players[j] )
                if distance < sensing_d:
                    total += a1 + a2 * (distance**2)
        
    print("Total transimition power: ", total)
    return total
                        
        

