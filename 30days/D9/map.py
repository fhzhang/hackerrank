# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
d = {}
for n in range(t):
   x = input().split()
   d[x[0]] = x[1]

while True:
    try:
        keyword = input()
        if keyword in d:
            print (keyword, "", d[keyword], sep="")
        else:
            print ('Not found')
    except: break