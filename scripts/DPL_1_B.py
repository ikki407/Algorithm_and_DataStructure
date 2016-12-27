a = map(int, raw_input().split())
N = a[0]
W = a[1]

class Item(object):
    def __init__(self,v,w):
        self.v = v
        self.w = w

Items = [Item(0,0)]
for i in xrange(N):
    a = map(int,raw_input().split())
    Items.append(Item(a[0],a[1]))

C = [ [0] * (W+1) for _ in xrange(N+1)]
G = [ [''] * (W+1) for _ in xrange(N+1)] 

def knapsack():
    for i in xrange(1,N+1):
        for w in xrange(1,W+1):
            if Items[i].w <= w:
                if Items[i].v + C[i-1][w-Items[i].w] > C[i-1][w]:
                    C[i][w] = Items[i].v + C[i-1][w-Items[i].w]
                    G[i][w] = 'DIAGONAL'
                else:
                    C[i][w] = C[i-1][w]
                    G[i][w] = 'TOP'
            else:
                C[i][w] = C[i-1][w]
                G[i][w] = 'TOP'

    print C[N][W]
    return 0

knapsack()






