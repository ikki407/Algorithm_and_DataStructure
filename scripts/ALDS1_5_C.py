import math

n = int(raw_input())

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

th = math.pi/3.0

def koch(n, p1, p2):
    if n == 0:
        return
    s = Point()
    t = Point()
    u = Point()

    s.x = (2*p1.x + 1*p2.x) / 3.0
    s.y = (2*p1.y + 1*p2.y) / 3.0
    t.x = (1*p1.x + 2*p2.x) / 3.0
    t.y = (1*p1.y + 2*p2.y) / 3.0
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y

    koch(n-1,p1,s)
    print s.x, s.y
    koch(n-1,s,u)
    print u.x, u.y
    koch(n-1,u,t)
    print t.x,t.y
    koch(n-1,t,p2)
    
def main():
    p1 = Point()
    p2 = Point()

    p1.x = 0.0
    p1.y = 0.0
    p2.x = 100.0
    p2.y = 0.0

    print p1.x, p1.y
    koch(n,p1,p2)
    print p2.x, p2.y

    return 0

main()


