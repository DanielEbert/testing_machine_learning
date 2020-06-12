#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


import util

O = [0,0,0]

round = 0

def gradientDescent(O, x, y):
    global round
    tmp = O - 1.7 * cost(x, y)
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
    #return np.array([O]) @ row
    a = np.array([O]) @ row
    #a = float(a[0])
    return 1 / (1 + 2.71828**-a)

# ich glaube das ist die ableitung von der cost function?
def cost(x, y):
    assert len(x) == len(y), 'Data Sets need the same length'
    sum = np.zeros(len(O))
    for i in range(len(x)):
        sum += ((h(x[i]) - y[i]) * x[i])
    sum /= len(x)
    return sum 

data = util.parseCSVAsDict('data/logisticRegressionDataSet.csv')
radius = np.array(data['"radius_mean"'], dtype=np.float)
diagnosisRaw = np.array(data['"diagnosis"'])

diagnosis = np.zeros(len(diagnosisRaw), np.float)
for i in range(len(diagnosis)):
    if diagnosisRaw[i] == "M":
        diagnosis[i] = 1

maxRadius = np.amax(radius)

for i in range(len(radius)):
    radius[i] /= maxRadius
    
xt = np.array([[1]*len(radius), radius, radius**2])
x = np.ndarray.transpose(xt)

#while True:
#    O = gradientDescent(O, x, diagnosis)

def res(value):
    return -10.99484682 + 12.07845395 * value + 16.75953364 * (value ** 2)

a = res(20 / maxRadius)
print(a)
print(1 / (1 + 2.71828**-a))


value = np.linspace(0.2,1,100)
plt.scatter(radius, diagnosis, 0.01)
plt.plot(np.linspace(0,1,100), -10.99484682 + 12.07845395 * value + 16.75953364 * (value ** 2))

plt.show()