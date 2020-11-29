import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation
from sdp_func import *


def plot_position(players):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.grid(which='major', axis='both', linestyle='-')
    
    print(players[:,0])
    plt.scatter(players[:6,0], players[:6,1], c='k', s=25)
    plt.scatter(players[6:,0], players[6:,1], c='b', s=20)

    plt.show()
''' 
Sensor Deployment Problem
'''
#----hyperparameter
size = 100
_mobile = 6
_immobile = 11
sensing_d = 30
iteration = 10

if __name__ == "__main__":
    #----initialize
    players = np.array([ [20,10], [40,10], [60,10], [80,10], [30,90], [70,90] ])
    print(players.shape)
    for i in range(_immobile):
        t = [ random.choice(range(size)), random.choice(range(size)) ]
        players = np.append(players, [t], axis=0)

    total_transmission_power(players, sensing_d)
    plot_position(players)

    
    for iters in range(iteration):

        new_players = np.array([])
        for i in range(_mobile, _immobile):
            compute_action_profile( players, i)



    #----
