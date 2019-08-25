from collections import Counter
class DisjointSet:
    def __init__(self,N):
        #Uses 1 based Indexing, so size is N+1
        self.parent = [i for i in range(0,N+1)]
        self.rank = [0 for _ in range(0,N+1)]
        
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,x,y):
        xRoot,yRoot = self.find(x),self.find(y)
        if(xRoot==yRoot):
            return
        if self.rank[xRoot]<self.rank[yRoot]:
            self.parent[xRoot]=yRoot
        elif self.rank[xRoot]>self.rank[yRoot]:
            self.parent[yRoot]=xRoot
        else:
            self.parent[yRoot]=xRoot
            self.rank[xRoot]+=1
t = int(input())
for k in range(0,t):
    n,m = map(int,input().split())
    ds = DisjointSet(n)
    for _ in range(m):
        x,y=map(int,input().split())
        ds.union(x,y)
    #Grouping as per connected components, ie. Every vertex belongs to the component of it's highest level parent
    for i in range(0,len(ds.parent)):
        ds.parent[i]=ds.find(i)
    c = Counter(ds.parent)
    ans = 2*(len(c)-2) # An extra -1 because we get an additional vertex 0 which is not valid.
    for x in c:
        ans+=c[x]-1
    print('Case #{}: {}'.format(k+1,ans))
