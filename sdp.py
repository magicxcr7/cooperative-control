import numpy as np
import matplotlib.pyplot as plt



def plot_position(players):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.grid(which='major', axis='both', linestyle='-')
    
    print(players[:,0])
    plt.scatter(players[:6,0], players[:6,1], c='black', s=25)

    plt.show()

''' 
Sensor Deployment Problem
'''
if __name__ == "__main__":
    #----hyperparameter
    size = 100
    players = np.array([ [20,10], [40,10], [60,10], [80,10], [30,90], [70,90] ])

    plot_position(players)
