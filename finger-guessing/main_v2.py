from utils import *
import random
import numpy as np
import matplotlib.pyplot as plt
import copy


action_name = ['paper', 'scissors', 'stone']
action = [0, 1, 2]

params = [[0.01, 0.01], [0.05, 0.05], [0.1, 0.1] ] 
# params = [[0.1, 0.1]]
iteration = 500





if __name__ == "__main__":
    
    hhh = [] # 依param存history
    www = [] # 依param存win rate
    lll = []
    for param in params:
        count = 0
        history = []
        wintory = []
        lcount = 0
        lostory = []

        print("======start=====")
        player1 = Automaton()
        player2 = Enviroment()
        result = None # for saving each round result
        for i in range(iteration):
            """
            """
            choice1 = player1.take_action(select_M = True)
            choice2 = player2.take_action(res = result)
            result = judge(choice1, choice2)
            if(i>400 and i%10==0):
                print("round {} : {}  {}  => 結果: {}".format(i, action[choice1], action[choice2], result))
                print(player1.weight)
            player1.update(res = result, param = param)
            if(i>400 and i%10==0):
                print(player1.weight)
                print("============")

            if result=='win':
                count += 1
            elif result =='loss':
                lcount += 1

            history.append(copy.deepcopy(player1.weight))
            wintory.append(count/(i+1))
            lostory.append(lcount/(i+1))
        print("________________________________________________________")
        history = np.array(history)
        wintory = np.array(wintory)
        hhh.append(history)
        www.append(wintory)
        lostory = np.array(lostory)
        lll.append(lostory)

    print(hhh[0].shape )
    
    for i in range(len(www)):
        print("win rate: ",www[i][-1])
        plt.plot(hhh[i][:,0,0], label=action_name[0])
        plt.plot(hhh[i][:,0,1], label=action_name[1])
        plt.plot(hhh[i][:,0,2], label=action_name[2])
        plt.plot(www[i][:], label='win rate')
        plt.plot(lll[i][:], label='loss rate')
        # plt.plot(hhh[1], label="param (0.05, 0.05)")
        # plt.plot(hhh[2], label="param (0.1, 0.1)")
        # plt.plot(hhh[3], label="param (0.2, 0.2)")
        plt.title("S-model-9-state-Result : {} ".format(params[i]))
        plt.xlabel("Iter")
        plt.ylabel("prob")
        plt.legend(loc='upper right')
        # plt.savefig("ResultE1_00{}.png".format(i))
        plt.show()
        plt.clf()