import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    s = str(bin(n))
    l = s[2:].split('0')
    l.sort()
    print(len(l[-1]))