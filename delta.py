import sys
import subprocess
import subprocess
import re


def DD(p, c):
    #base case
    #print('dd: p = ', p, ' c = ', c)
    if len(c) == 1:
        return c
    #splits list in half
    p1 = c[:len(c)//2]
    p2 = c[len(c)//2:]
    #get arguments to pass to subprocess
    #has to be a long string 
    l = sys.argv[2] + " "
    l2 = sys.argv[2] + " "
    for i in p+p1:
        l = l + i + " "
    for i in p+p2:
        l2 = l2 + i + " "
    if subprocess.run(l, shell = True).returncode == 1:
        return DD(p, p1)
    if subprocess.run(l2, shell = True).returncode == 1:
        return DD(p, p2)
    return DD(p + p2, p1) + DD(p + p1, p2)



def main():
    #delta debug
    n = int(sys.argv[1])
    c = []
    p = []
    for i in range(0,n):
        c.append(str(i))
    #splits the lists in half
    li = DD(p, c)
    li = [int(i) for i in li]
    li.sort()
    print(li)

    


if __name__ == '__main__':
    main()

