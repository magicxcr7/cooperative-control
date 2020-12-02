import sys
import numpy as np
import matplotlib.pyplot as plt
from sdp import sensing_d, _immobile, _mobile

#actions = np.array( [[0,1], [1,0], [0,-1], [-1,0], [0,0]] )
actions = np.array([
                    [-1,1], [0,1], [1,1],
                    [-1,0], [0,0], [1,0],
                    [-1,-1],[0,-1],[1,-1]
                    ])

def compute_action_profile(players, pi, iters):
    beta = 1 + iters/300

    max_u = -999999
    max_i = -1

    for i in range(len(actions)):
        # check how many legal action
        reached = players[pi] + actions[i]
        if(np.max(reached)>99 or np.min(reached)<0):
            continue
        else:
            ui = 0
            for pj in range(_immobile):
                distance = np.linalg.norm(reached - players[pj])
                if distance > sensing_d:
                    ui += 1* (distance**2) ##weighted
                # else:
                #     ui += 0.8*(distance**2)
            for pj in range(_immobile, _immobile+_mobile):
                
                if pj == pi:
                    continue
                distance = np.linalg.norm(reached - players[pj])
                if distance < sensing_d:
                    ui += distance**2

            ui *= -2
            #print(i, ui)
            if ui>max_u:
                max_u = ui
                max_i = i
    #print("------------------max u: {} , max i: {}".format(max_u, max_i))
    return actions[max_i]
    




    

def total_transmission_power(players):

    a1, a2 = 1, 1
    total = 0

    for i in range(17):
        for j in range(17):
            if(j != i):
                distance = np.linalg.norm( players[i] - players[j] )
                if distance < sensing_d:
                    total += a1 + a2 * (distance**2)
        
    #print("Total transimition power: ", total)
    return total
                        
        
if __name__ == "__main__":
    print(20/300)
    a = [ [0,0], [99,99]]
    
    for action in actions:
        t = (a[0]-action)
        print(np.max(t))