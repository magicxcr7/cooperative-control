import random

action_name = ['paper', 'scissors', 'stone']
action = [0, 1, 2]

test = False
extense = True # 9 state Q table
S_model = True
class Automaton:
    """
    e.g., 對手: 石頭
    自己: 
    """
    def __init__(self ):
        self.weight = [[0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32]] # Q table
        self.action = random.randint(0, 2)   # last action
        self.lstate = 0
        if extense: # 9*3
            self.weight = [[0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32], [0.35, 0.33, 0.32]]
            self.weight = [init_player1() for i in range(9)]
        # print(self.weight)
    def take_action(self, select_M = False):
        
        if select_M:
            """fake deterministic"""
            if random.random() < 0.7:
                if not extense:
                    best_v = self.weight[self.action].index(max(self.weight[self.action]))
                else:
                    best_v = self.weight[self.lstate].index(max(self.weight[self.lstate]))
            else:
                if not extense:
                    best_v = random.choices(action, weights = self.weight[self.action] , k=1)[0]
                else:
                    best_v = random.choices(action, weights = self.weight[self.lstate] , k=1)[0]
        else:
            """prob distribtion"""
            if not extense:
                best_v = random.choices(action, weights = self.weight[self.action] , k=1)[0]
            else:
                best_v = random.choices(action, weights = self.weight[self.lstate] , k=1)[0]

        self.action = best_v ## 貌似這裡出問題
        return best_v

    def update(self, res, param):
        if test:
            print("{} {} {}".format(self.action, res, param))
            print(self.weight)
        if not S_model:
            if res == 'win' :# 拿別人alpha比例 獎勵自己
                update_v = 0
                for i in range(3):
                    if i != self.action:
                        if not extense: #原本的
                            update_v += param[0] * self.weight[self.action][i]
                            self.weight[self.action][i] = (1-param[0]) * self.weight[self.action][i]
                        else:
                            update_v += param[0] * self.weight[self.lstate][i]
                            self.weight[self.lstate][i] = (1-param[0]) * self.weight[self.lstate][i]

                if test:
                    print("update_v is: ", update_v)
                if not extense:
                    self.weight[self.action][self.action] += update_v
                else:
                    self.weight[self.lstate][self.action] += update_v
            elif res == 'loss':# 拿自己beta比例 獎勵別人
                if not extense:
                    for i in range(3):
                        self.weight[self.action][i] = (1-param[1]) * self.weight[self.action][i]
                        if i != self.action:
                            self.weight[self.action][i] += param[1]/2
                else:
                    for i in range(3):
                        self.weight[self.lstate][i] = (1-param[1]) * self.weight[self.lstate][i]
                        if i != self.action:
                            self.weight[self.lstate][i] += param[1]/2
        else:
            if res=='win':
                beta = 1
            elif res =='draw':
                beta = 0.5
            elif res == 'loss':
                beta = 0
            else:
                import sys
                sys.exit()
            if not extense:
                for i in range(3):
                    p = self.weight[self.action][i]
                    if i != self.action:
                        self.weight[self.action][i] = p - beta*param[0]*p + (1-beta)*(param[0]/2 - param[0]*p)
                    else:
                        self.weight[self.action][i] = p + beta*param[0]*(1-p) - (1-beta)*param[0]*p
            else:
                for i in range(3):
                    p = self.weight[self.lstate][i]
                    if i != self.action:
                        self.weight[self.lstate][i] = p - beta*param[0]*p + (1-beta)*(param[0]/2 - param[0]*p)
                    else:
                        self.weight[self.lstate][i] = p + beta*param[0]*(1-p) - (1-beta)*param[0]*p

        

        for i in range(3):
            if not extense:
                self.weight[self.action][i] = round(self.weight[self.action][i],3)
            else:
                self.weight[self.lstate][i] = round(self.weight[self.lstate][i],3)
        if test:
            print("-----")
            print(self.weight)
            print("====================")
        if extense:
            if res=='win':
                self.lstate = self.action*3
            elif res =='draw':
                self.lstate = self.action*3 + 1
            elif res == 'loss':
                self.lstate = self.action*3 + 2
            else:
                import sys
                sys.exit()

class Enviroment:
    def __init__(self):
        self.action = 1 # random.randint(0, 2)

    def take_action(self, res = 'loss'):

        # its win/loss is for player1
        if res=='win':
            self.action = (self.action+2) % 3
            """if env loss -> next round change strategy"""
        return self.action

def count_expected_winrate(a, b):
    return a[0]*b[2] + a[1]*b[0] + a[2]*b[1]

def init_player1():
    init_list = [0,0,0]
    init_list[0] = round(random.uniform(0,1),3)
    print(init_list[0])
    init_list[1] = round(random.uniform(0,(1-init_list[0])),3)
    print(init_list[1])
    init_list[2] = round((1-init_list[0]-init_list[1]),3)
    print(init_list[2])
    return init_list

def judge(action1, action2): ## input 0,1,2
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

def update(action, result, param, weight):
    """
    win update 0.1* (1-other)
    loss panalty self
    """
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

if __name__ == "__main__":
    player1 = Automaton()