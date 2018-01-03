

def solve(k,array):
    if len(array)==1:
        return array
    print("Solving "+str(array))
    best=[]
    for num in array :
        new= solveT(k,array,num)
        if len(new)>len(best):
            print("replaced"+str(len(new)))
            best=new
    return best

def solveT(k,array,T):
    a1=[]
    a2=[]
    for elem in [item for item in array if item not in [T]]:
            if (elem+T)%k==0:
                print("problem in {} + {}".format(elem,T))
                print("---- Exploring first")
                a1=solve(k,[item for item in array if item not in [T]])
                print("---- Exploring second")
                a2=solve(k,[item for item in array if item not in [elem]])
                return a1 if len(a1)>len(a2) else a2
    return array
    

n,k=map(int,input().strip().split(' '))
array=list(map(int,input().strip().split(' ')))
result = solve(k, array)
print(len(result))