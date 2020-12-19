from utils import *
import random
import numpy as np
import matplotlib.pyplot as plt

action_name = ['paper', 'scissors', 'stone']
action = [0, 1, 2]



player1_weight = [0.34, 0.33, 0.33]#[0.34, 0.33, 0.33]#init_player1()
# player2_weight = [0.34, 0.33, 0.33]
player2_weight = [0.6, 0.2, 0.2]
# player2_weight = [0.5, 0.5 ,0]
params = [[0.01, 0.01], [0.05, 0.05], [0.1, 0.1] ] 
iteration = 300

"""
嘗試解決 固定參數
固定iter 嘗試alpha,beta

固定alpha, beta
固定iter

"""
if __name__ == "__main__":
    expected = []

    hhh = []
    for param in params:

        count = 0
        history = []
        print("======start=====")
        player1_weight = init_player1()#[0.34, 0.33, 0.33]#init_player1()
        player2_weight = [0.34, 0.33, 0.33]
        # player2_weight = [0.6, 0.2, 0.2]
        for i in range(iteration):
            print("____________   round {}   __________________".format(i))
            print("Player1 機率分佈:", player1_weight, 'total: ', round(sum(player1_weight), 3), round(np.std(player1_weight), 3),  end= '\t|\t')
            print("Player2 機率分佈:", player2_weight)
        

            choice1 = random.choices(action, weights = player1_weight, k=1)[0]
            print('player1: ', action_name[choice1], choice1)
            choice2 = random.choices(action, weights = player2_weight, k=1)[0]
            print('player2: ', action_name[choice2], choice2)
            result = judge(choice1, choice2)
            print('結果: ', result)
            player1_weight = update(choice1, result, param, player1_weight)

            if i>20:
                for w in player1_weight:
                    if w>0.6:
                        count +=1 
            
            history.append(player1_weight.copy())
            #print('!!!!!',history)
        print("________________________________________________________")
        
        print("過高次數共 {} 次".format(count))
        history = np.array(history)
        hhh.append(history)
        expected.append(player1_weight.copy())

    print(len(hhh),'--------')
            
    for i in range(3):
        print(i)
        plt.plot(hhh[i][:,0], label=action_name[0])
        plt.plot(hhh[i][:,1], label=action_name[1])
        plt.plot(hhh[i][:,2], label=action_name[2])
        #plt.plot(hhh[1], label="param (0.05, 0.05)")
        #plt.plot(hhh[2], label="param (0.1, 0.1)")
        #plt.plot(hhh[3], label="param (0.2, 0.2)")
        plt.title("---RPS 1-3 Result : {}".format(params[i]))
        plt.xlabel("Iter")
        plt.ylabel("prob")
        plt.legend(loc='upper right')
        plt.savefig("---1-3_00{}.png".format(i))
        plt.show()
        plt.clf()

    print(expected)
        






