from utils import *
import random
import numpy as np
import matplotlib.pyplot as plt

action_name = ['paper', 'scissors', 'stone']
action = [0, 1, 2]



# player1_weight = [0.34, 0.33, 0.33]#[0.34, 0.33, 0.33]#init_player1()
# player2_weight = [0.334, 0.333, 0.333]
#player2_weight = [0.6, 0.2, 0.2]
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

    hhh = [] # 依param存history
    www = [] # 依param存win rate
    for param in params:

        count = 0
        history = [] # 0,1,2, winrate
        wintory = []
        print("======start=====")
        player1_weight = init_player1()#[0.334, 0.333, 0.333]#init_player1()
        player2_weight = [0.334, 0.333, 0.333]
        # player2_weight = [1, 0, 0]
        last_res = None
        for i in range(iteration):
            
            print("____________   round {}   __________________".format(i))
            print("Player1 機率分佈:", player1_weight, 'total: ', round(sum(player1_weight), 3), round(np.std(player1_weight), 3),  end= '\t|\t')
            print("Player2 機率分佈:", player2_weight)
        
            if i==0:
                choice2 = random.choices(action, weights = player2_weight, k=1)[0]

            # if last_res=='win': ##enviroment loss
            #     choice2 = (choice1+1) %3
            # else:
            #    choice2 = random.choices(action, weights = player2_weight, k=1)[0]

            choice1 = random.choices(action, weights = player1_weight, k=1)[0]

            print('player1: ', action_name[choice1], choice1)
            print('player2: ', action_name[choice2], choice2)


            result = judge(choice1, choice2)
            last_res = result ## record
            print('結果: ', result)
            player1_weight = update(choice1, result, param, player1_weight)

            # e_rate = count_expected_winrate(player1_weight.copy(), player2_weight)
            # print("rateeeeeeee: ",e_rate)
            if result=='win':
                count += 1
            
            history.append(player1_weight.copy())
            wintory.append(count/(i+1))
            # print('!!!!!',history)
        print("________________________________________________________")

        history = np.array(history)
        wintory = np.array(wintory)
        hhh.append(history)
        www.append(wintory)

    print(len(hhh),'--------')
    for i in range(3):
        print(hhh[i][-1,:])
    
            
    for i in range(3):
        print("win rate: ",www[i][-1])
        plt.plot(hhh[i][:,0], label=action_name[0])
        plt.plot(hhh[i][:,1], label=action_name[1])
        plt.plot(hhh[i][:,2], label=action_name[2])
        plt.plot(www[i][:], label='win rate')
        #plt.plot(hhh[1], label="param (0.05, 0.05)")
        #plt.plot(hhh[2], label="param (0.1, 0.1)")
        #plt.plot(hhh[3], label="param (0.2, 0.2)")
        plt.title("Env fixed result : {} ".format(params[i]))
        plt.xlabel("Iter")
        plt.ylabel("prob")
        plt.legend(loc='upper right')
        # plt.savefig("6-2_00{}.png".format(i))
        plt.show()
        plt.clf()

        







