#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


import util

O = [0,0,0]

round = 0

def gradientDescent(O, x, y):
    global round
    tmp = O - 1.9 * cost(x, y)
    round += 1
    if round % 100 == 0:
        print(tmp)
    return tmp

def h(row) -> float:
    #ret = 0
    #for i in range(len(O)):
    #    ret += O[i] * row[i]
    #tmp = np.array([O]) @ row
    #print(ret, O, tmp, row)
    #assert abs(ret - float(tmp[0])) < 0.01
    return np.array([O]) @ row

def cost(x, y):
    assert len(x) == len(y), 'Data Sets need the same length'
    sum = np.zeros(len(O))
    for i in range(len(x)):
        sum += ((h(x[i]) - y[i]) * x[i])
    sum /= len(x)
    return sum 

data = util.parseCSVAsDict('data/train.csv')

area = np.array(data['LotArea'], dtype=np.float)
price = np.array(data['SalePrice'], dtype=np.float)

maxArea = np.amax(area)

for i in range(len(area)):
    area[i] /= maxArea

xt = np.array([[1]*len(area), area, area**0.5])
x = np.ndarray.transpose(xt)

while True:
    O = gradientDescent(O, x, price)



def res(area):
    return 15408 -688292 * area + 938525 * area ** 0.5

for i in range(len(area)):
    print('area: {}; predicted: {}; real: {}'.format(area[i] * maxArea, res(area[i]), price[i]))

a = np.linspace(0,1,100)

plt.scatter(area, price, s=0.1)
plt.plot(np.linspace(0,1,100), 15406.579881078336 -688307.836233405 * a + 938536.8311935553 * a ** 0.5)

plt.show()