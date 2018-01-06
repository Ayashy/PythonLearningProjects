#So the idea is that with swaps you can get any ball anywhere you want
#The only constraint is that the number of balls in the cointainers must match the number of balls of each type
#The sort is required to find a match for each container to a type

def solve(container):
    if sorted(map(sum,container))==sorted(map(sum,zip(*container))):
        return "Possible"
    else:
        return "Impossible"


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    container = []
    for container_i in range(n):
        container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
        container.append(container_t)
    result = solve(container)
    print(result)