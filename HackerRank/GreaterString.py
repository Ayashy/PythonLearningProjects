

def solve(word):

    #Finding the longest suffix that is non-increasing
    max_index=len(word)-1
    for i in range(len(word)-1,-1,-1):
        if(word[i]>=word[max_index]):
            max_index=i
        else:
            break

    #If the suffix spans the whole list, then its already solved
    if max_index==0:
        return "no answer"

    #Finding the right-most value that's bigger than pivot
    pivot=max_index-1
    swap_index=len(word)-1
    for j in range(len(word)-1,pivot,-1):
        if word[j]>word[pivot]:
            swap_index=j
            break
    
    #Swap that value with pivot, then sort the new suffix
    result=list(word)
    result[pivot], result[swap_index]=result[swap_index],result[pivot]
    result[pivot+1:]=sorted(result[pivot+1:])
    return ''.join(result)
        






n=int(input().strip())
for i in range(n):
    w=input().strip()
    result=solve(w)
    print(result)