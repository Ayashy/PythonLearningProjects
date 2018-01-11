import re

def solve(pw):
    lenght_error=len(pw)<8
    contains_upper=re.search(r"[A-Z]", pw) is not None
    contains_lower=re.search(r"[a-z]", pw) is not None
    contains_num=re.search(r"[0-9]", pw) is not None
    contains_symbols=re.search(r"[\-_@.]", pw) is not None
    isValid=contains_lower and contains_num and contains_symbols and contains_upper
    if isValid:
        print("YES")
    else:
        print("NO")





n=int(input().strip())
for i in range(n):
    pw=input().strip()
    solve(pw)
