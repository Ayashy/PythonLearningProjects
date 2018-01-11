

def kaprekarNumbers(p, q):
    for i in range(p,q+1):
        d= len(i)
        square=list(map(int,str(i**2)))
        nums=[]
        if square[0:d-1]==square[d:]:
            nums.append(i)


if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    print (" ".join(map(str, result)))


