from math import sqrt
class PrimeNumber():
    def __init__(self):
        super().__init__()
    
    def isPrimeNumber(self, num):
        if num == 1 or num == 0:
            return 'Not prime'
        for i in range(2,  round(num / 2) + 1):
            if num % i == 0:
                return 'Not prime'
        return 'Prime'


T = int(input())
c = PrimeNumber()
l = []

for n in range(T):
    l.append(int(input()))

for x in l:
    print(c.isPrimeNumber(x))