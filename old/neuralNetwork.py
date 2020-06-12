#!/usr/bin/env python3

import numpy as np
from secrets import randbelow


def g(value):
    return 1 / (1 + np.exp(-value))

def h(x, y) -> float:
    a = [(a*[0]) for a in layerSizes]

    a[0] = x

    a[1][0] = 1
    a[1][1] = g(weights[0][1] @ a[0])
    a[1][2] = g(weights[0][2] @ a[0])

    a[2][0] = 1
    a[2][1] = g(weights[1][1] @ a[1])

    #print(a)
    ###########

    #c = [(a*[0]) for a in layerSizes]
    deltas = [ [], [0,0], [0] ]

    deltas[2] = [1, a[2][1] - y]
    # c[2][0] discarded

    #c1 = np.transpose(np.array(weights[1][1:])) @ np.array(deltas[2])
    #print("-->",c1)
    #c1 = c1 * (np.array(a[1]) * (1-np.array(a[1])))

    c = (np.transpose(np.array(weights[1])) @ np.array(deltas[2])) * \
         np.array(a[1] * (1-np.array(a[1])))
    print(c)

    exit(0)

    deltas[1][0] = weights[1][1][1] * deltas[2][0] * a[1][1] * (1-a[1][1])
    deltas[1][1] = weights[1][1][2] * deltas[2][0] * a[1][2] * (1-a[1][2])


    capDeltas[2][0] += deltas[2][0]

    capDeltas[1][1] += a[1][1] * deltas[2][0]
    capDeltas[1][2] += a[1][2] * deltas[2][0]
    
    return a[2][1]
    #deltas[0][0] = a[0]

    i = 0

    for layer in range(3):
        for unit in range(3):   # exclude bias unit?
            if layer <= 1:
                capDelta[layer][i] += a[layer][unit] * deltas[layer+1][0]
            else:
                capDelta[layer][i] += deltas[layer+1][0]

    print(c1,'\n---\n', deltas)

    return a[2][1]

def cost(x, y):
    assert len(x) == len(y), 'Data Sets need the same length'
    sum = 0
    for i in range(len(x)):
        sum += (h(x[i], y[i]) - y[i])**2
    sum /= len(x)
    return sum 



layerSizes = (3,3,2)

# TODO: change from 0 to -e <-> +e
weights = [(np.random.randint(-3, 3, size=(a,b))) for a,b in zip(layerSizes[1:],layerSizes[:-1])]
print(weights)

# l = 3  i = len(xs)  j = unit in layer l (including bias unit)
# in another slide: ai⁽j⁾ is activation of unit i in layer j
#deltas = [ [ [0,0,0] ], [ [0,0,0] ], [ [0,0] ] ]
capDeltas = [ [], [0,0,0], [0] ]

#print(h([1,1,0]))

xs = [[1,0,0]]
ys = [1]
#xs = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
#ys = [1,0,0,1]

cost(xs, ys)

print(capDeltas)

