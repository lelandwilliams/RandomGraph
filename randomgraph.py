from numpy.random import randint
from numpy import zeros
from math import factorial
from sys import argv

def randomgraph(n=3):
    G = zeros(dtype=int, shape=(n,n))
    for i in range(n):
        for j in range(i, n):
            G[i][j] = G[j][i] = randint(low=0, high=2)
    return G

if __name__ == '__main__':
    if len(argv) == 1:
        print(randomgraph())
    elif len(argv) == 2:
        try:
            n = int(argv[1])
            print(randomgraph(n))
        except ValueError:
            print("Must provide an integer")
    else:
        print("Syntax: randomgraph.py <n>")
            


