finalRes = []

def findMaxPath(inputList):
    while len(inputList) > 1:
        t0 = inputList.pop()
        t1 = inputList.pop()
        inputList.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
    return inputList[0][0]
 
if __name__ == '__main__':
    T = input()
    for i in range(0,T):
        N = input()
        numList = []
        for k in range(0,N):
            numbers = raw_input().split()
            numList.append(map(int, numbers))
        finalRes.append(findMaxPath(numList))
    print '\n'.join(map(str, finalRes))
