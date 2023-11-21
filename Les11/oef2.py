import random

class Dobbelsteen:
    MIN_AANTAL = 1
    MAX_AANTAL = 6

    def __init__(self, min_aantal = 1, max_aantal = 6):
        if min_aantal < max_aantal:
            self.min_aantal = min_aantal
            self.max_aantal = max_aantal
        else:
            self.min_aantal = Dobbelsteen.MIN_AANTAL
            self.max_aantal = Dobbelsteen.MAX_AANTAL

    def gooi(self):
        self.worp = random.randint(self.min_aantal, self.max_aantal)

    def get(self):
        if self.worp == None:
            return self.min_aantal
        else:
            return self.worp
    
    def __str__(self):
        waarde = str(self.worp)
        return waarde

def tel_aantal_worpen(max_aantal, aantal_ogen):
    dobbelsteen = Dobbelsteen(0, aantal_ogen * 2)

    for aantal in range(max_aantal):
        dobbelsteen.gooi()
        print(dobbelsteen)
        if dobbelsteen.get() == aantal_ogen:
            return aantal + 1
    return -1

gewenst = 4
max_worpen = 10
aantal = tel_aantal_worpen(max_worpen,gewenst)
print(f'In {aantal} pogingen werd een {gewenst} gegooid' if aantal > 0
      else f'Er werd geen {gewenst} gegooid binnen de {max_worpen} beschikbare pogingen')