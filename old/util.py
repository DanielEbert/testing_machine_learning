
def parseCSV(filename: str) -> list:
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            data.append(lines[i].split(','))

    return data

def parseCSVAsDict(filename: str) -> list:
    from collections import defaultdict
    import re
    data = defaultdict(list)
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        headers = lines[0].split(',')
        for i in range(1, len(lines)):
            line = lines[i].split(',')
            for i in range(len(line)):
                value = line[i]
                if value.isdigit():
                    data[headers[i]].append(int(value))
                elif re.match("^\d+?\.\d+?$", value) is not None:
                    data[headers[i]].append(float(value))
                else:
                    data[headers[i]].append(line[i])

    return data

def normalEquation(m, m2):
    import numpy as np
    mt = np.ndarray.transpose(m)
    #a = np.dot(mt,m)
    a = mt @ m
    b = np.linalg.pinv(a)
    #c = np.dot(b, mt)
    c = b @ mt
    #d = np.dot(c, m2)
    d = c @ m2
    return d