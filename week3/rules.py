import random

class Easy21:
    def __init__(self):
        self.reset()

    def draw_card(self):
        value = random.randint(1,10)
        color = random.choice(["black","black","red"])  
        return value if color == "black" else -value

    def reset(self):
        self.dealer = random.randint(1,10)
        self.player = random.randint(1,10)
        return (self.dealer,self.player)

    def step(self,state,action):
        dealer,player = state
        if action == 0:
            player += self.draw_card()
            if player < 1 or player > 21:
                return None,-1,True
            return (dealer,player),0,False
        else:
            dealer_sum = dealer
            while dealer_sum < 17:
                dealer_sum += self.draw_card()
                if dealer_sum < 1 or dealer_sum > 21:
                    return None,1,True
            if player > dealer_sum:
                return None,1,True
            elif player < dealer_sum:
                return None,-1,True
            else:
                return None,0,True