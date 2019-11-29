t = int(input())
while t:
    lo,hi = map(int,input().split())
    int(input())
    while lo<=hi:
        mid = (lo+hi)//2
        print(mid,flush=True)
        response = input()
        if response == 'TOO_BIG':
            hi=mid-1
        elif response == 'TOO_SMALL':
            lo=mid+1
        else:
            break
    t-=1
