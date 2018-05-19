import sys

vsize = int(input())
if (vsize % 2 == 0) or (vsize > 100):
    print("invalid")
    sys.exit()

for i in range(vsize,0,-1):
    for j in range(1,vsize+1):
        if i == 1:
            if j == (vsize+1)/2:
                print("v",end="")
            else:
                print(".",end="")
        else:
            if (j == int(vsize/2) - int(i/2) + 1) or (j == vsize - (int(vsize/2) - int(i/2))):
                print("v",end="")
            else:
                print(".",end="")

    print()

