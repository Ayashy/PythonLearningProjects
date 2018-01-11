
def solve(word):
    if len(word)==1:
        return word
    else:
        result=""
        halfSize=len(word)//2
        for i in range(0,halfSize):
            result+=chr((( ord(word[i]) + ord(word[2*halfSize-1-i]) - 2*97 )%26)+97)
            return solve(result)

if __name__=="__main__":
    T=int(input().strip())
    for i in range(T):
        A,k=input().strip().split(" ")
        word=A*int(k)
        print(solve(word))