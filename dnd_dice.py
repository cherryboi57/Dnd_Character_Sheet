import random

class dice:
    def __init__(self, n):
        self.size = n
        
    def roll(self, times=None):
        # roll once if number of times is not specified
        if times is None:
            return random.choice(range(1, self.size+1))
        # roll number of specified times
        else:
            count = 0;
            for i in range(1, times+1):
                r = random.choice(range(1, self.size+1))
                print(r)
                count = count + r
            return(count)

#create dice
d4 = dice(4)
d6 = dice(6)
d8 = dice(8)
d10 = dice(10)
d12 = dice(12)
d20 = dice(20)
