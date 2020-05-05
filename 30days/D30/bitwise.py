import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    l = []
    
    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        if k-1 | k <= n:
            l.append(k-1)
        else:
            l.append(k -2)
    
    for r in l:
        print(r)
        # l = range(1,n)
        # m = [0]
        # for i in l:
        #     temp = range(i+1,n)
        #     for j in temp:
        #         if i&j<k:
        #             m.append(i&j)
        # print(max(m))