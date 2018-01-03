import math

def question6(raw_input):
    input=[x for x in raw_input.split(',')]
    C=50
    H=30
    Q=[]
    for item in input:
        Q.append(math.sqrt((2*C*item)/H))
    return Q

def question7(X,Y):
    matrix=[]
    for i in range(X):
        line=[]
        for j in range(Y):
            line.append(int(i*j))
        matrix.append(line)
    return matrix

def question10(raw_input):
    return ' '.join(sorted(set(raw_input.split(","))))

def question11(raw_input):
    nums=raw_input.split(',')
    return  lambda x: int(x)%5==0 ,nums
