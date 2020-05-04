import math
import os
import random
import re
import sys

listArr=[]
listSum=[]

def findSum(arr):
    return sum(map(sum,arr))

def getListArray(row, column, arr):
    listtemp=[]
    for i in range(row, row+3):
        listtemp.append(arr[i][column:column+3])
        if i == row + 1:
            listtemp[1][0]=0
            listtemp[1][2]=0
    listArr.append(listtemp)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for r in range(4):
        for c in range(4):
            getListArray(r, c, arr)
    
    for array in listArr:
        listSum.append(findSum(array))
    listSum.sort()
    print(listSum[-1])