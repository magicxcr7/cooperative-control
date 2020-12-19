import random

action_name = ['paper', 'scissors', 'stone']
action = [0, 1, 2]

def init_player1():
    init_list = [0,0,0]
    init_list[0] = round(random.uniform(0,1),3)
    print(init_list[0])
    init_list[1] = round(random.uniform(0,(1-init_list[0])),3)
    print(init_list[1])
    init_list[2] = round((1-init_list[0]-init_list[1]),3)
    print(init_list[2])
    return init_list

def judge(action1, action2):
    if action1 == action2:
        return 'draw'
    else:
        if action1 == action[0] and action2 == action[2]:
            return 'win'
        elif action1 == action[1] and action2 == action[0]:
            return 'win'
        elif action1 == action[2] and action2 == action[1]:
            return 'win'
        else:
            return 'loss'


"""
win update 0.1* (1-other)
loss panalty self
"""
def update(action, result, param, weight):

    if result =='win':#拿別人alpha比例 獎勵自己
        update_v = 0
        for i in range(len(weight)):
            if i != action:
                update_v += param[0] * weight[i]
                weight[i] = (1-param[0]) * weight[i]
        weight[action] += update_v
    
    
    elif result =='loss':##拿自己beta比例 獎勵別人
        
        for i in range(len(weight)):
            weight[i] = (1-param[1]) * weight[i]
            if i != action:
                weight[i] += param[1]/2
    

    for i in range(len(weight)):
        weight[i] = round(weight[i],3)
    return weight