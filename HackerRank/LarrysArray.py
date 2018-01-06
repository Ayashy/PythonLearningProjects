

def solve(A):
    sets=[]
    sets.append(A)
    findPerms(sets,A)
    sortedA=sorted(A)
    print(sets)
    if sortedA in sets:
        return True
    else:
        return False

def findPerms(sets,A):
    for i in range(len(A)-2):
        new_array= rotate(A,i)
        if new_array not in sets:
            sets.append(new_array)
            findPerms(sets,new_array)

def rotate(array,index):
    new_array=list(array)
    if index+2<len(array):
        new_array[index],new_array[index+1],new_array[index+2] = new_array[index+1],new_array[index+2],new_array[index]
    return new_array
        

T=int(input().strip())
for i in range(T):
    n=int(input().strip())
    A=list(map(int, input().strip().split(" ")))
    result=solve(A)
    if result :
        print('YES')
    else:
        print('NO')