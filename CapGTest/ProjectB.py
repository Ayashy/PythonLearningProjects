

def solve(nums):
    maxindex=0
    for i in nums:
        curr_index=nums.index(i)
        if maxindex<curr_index:
            maxindex=curr_index
    print(maxindex+1)


if __name__=="__main__":
    n=int(input().strip())
    for i in range(n):
        k=int(input().strip())
        nums=list(map(int,input().strip().split(" ")))
        solve(nums)