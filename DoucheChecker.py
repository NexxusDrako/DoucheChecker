import random

def doucheFactor():
    factor = random.randint(1, 100)
    return factor
    
def doucheChecker(factor):
    check = 0,
    if factor > 40:
        return 1
    else:
        return 0

def doucheFinder(check):
    if check == 1:
        print('Brian is a douche today, as fucking usual.')
    elif check == 2:
        print('Joshua is a douche today, as fucking usual.')
    elif check == 3:
        print('Both Brian and Joshua are douches today, you are fucked.')
    elif check == 0:
        print('Neither Brian nor Joshua are douches today, you lucky fuck.')

BrianFactor = doucheFactor()
JoshuaFactor = doucheFactor()
BrianCheck = doucheChecker(BrianFactor)
JoshuaCheck = doucheChecker(JoshuaFactor) * 2
DoucheCheck = BrianCheck + JoshuaCheck
doucheFinder(DoucheCheck)
