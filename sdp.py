import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sdp_func import *
import os, sys, shutil
import imageio


def plot_position(players, no=0):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.grid(which='major', axis='both', linestyle='-')
    
    #print(players[:,0])
    plt.title("time {:04d}".format(no))
    plt.scatter(players[:6,0], players[:6,1], c='k', s=25)
    plt.scatter(players[6:,0], players[6:,1], c='b', s=20)
    
    if no == iteration:
        for i in range(len(players)):
            for j in range(len(players)):
                if(i != j):
                    distance = np.linalg.norm(players[i]-players[j])
                    if distance < sensing_d:
                        plt.plot( [players[i,0], players[j,0]], [players[i,1], players[j,1]], 'r-')
        for i in range(1,15):
            plt.savefig("./imgs/{:04d}.png".format(no+i))
    plt.savefig("./imgs/{:04d}.png".format(no))
    plt.close()
    #plt.show()
''' 
Sensor Deployment Problem
'''
#----hyperparameter
size = 100
_immobile = 6
_mobile = 11
sensing_d = 40
iteration = 500

path = "./imgs"

if __name__ == "__main__":
    try:
        os.mkdir(path)
    except:
        shutil.rmtree(path)
        os.mkdir(path)
    
    curve = []
    #----initialize
    players = np.array([ [20,10], [40,10], [60,10], [80,10], [30,90], [70,90] ])
    #print(players.shape)
    for i in range(_mobile):
        t = [ random.choice(range(size)), random.choice(range(size)) ]
        players = np.append(players, [t], axis=0)

    t_u = total_transmission_power(players)
    curve.append(t_u)
    plot_position(players)

    #----update
    for iters in range(iteration):
        if iters%10==0:
            print(iters)
        #1-random choice
        pi = random.randint(_immobile, _immobile +_mobile-1) ##(6,16)
        #print("select: ",players[pi])

        #2-compute utility & argmax(ai)
        ai = compute_action_profile(players, pi, iters)
        
        #3-select action with best response & update
        #print("----------")
        #print("select pi: ",pi, " move: ",ai)
        # print("origin pi: ",players[pi])
        players[pi] += ai
        # print("after pi: ",players[pi])
        #4-compute total utility & plot position
        t_u = total_transmission_power(players)
        curve.append(t_u)
        plot_position(players, no=iters+1)


    print("removing....")
    #----make gif and remove file
    images = []
    writer = imageio.get_writer("./sdp.mp4", fps=20)
    for filename in os.listdir(path):
        images.append(imageio.imread("{}/{}".format(path, filename)))
        writer.append_data(imageio.imread("{}/{}".format(path, filename)))
    imageio.mimsave("./sdp.gif", images)
    writer.close()

    shutil.rmtree(path)


    plt.close('all')
    fig, ax = plt.subplots()
    plt.plot(curve)
    plt.xlabel("time")
    plt.ylabel("transmission power")
    plt.savefig("./sdp.png")
    plt.show()

    #----
