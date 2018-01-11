
def solve(elems):
    
    for i in range(1,len(elems)):
        value=elems[i]
        index=i
        for j in range(i,0,-1):
            if elems[j][0]>value[0]:
                elems[index]=elems[j]
                index-=1
            elif elems[j][0]==value[0]:
                if elems[j][1]>value[1]:
                    elems[index]=elems[j]
                    index-=1
            else:
                break
        elems[index]=value
    message=""
    for i in range(0,len(elems)):
        if 0<=elems[i][1]<len(elems)/2:
            message+="- "
        else:
           message+=elems[i][2]+" "
    print(message)


if __name__=="__main__":
    n=int(input().strip())
    elems=[]
    for i in range(n):
        a,b=input().strip().split(' ')
        elems.append( (int(a),i,b) )

    solve(elems)