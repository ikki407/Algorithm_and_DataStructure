n = int(raw_input())
A = map(int, raw_input().split())
q = int(raw_input())
M = map(int, raw_input().split())

def solve(i,m):
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res

def main():
    for m in M:
        res = solve(0,m)
        if res:
            print 'yes'
        else:
            print 'no'

main()
   
def solve(i, m):
  if dp[i][m] != -1:
    return dp[i][m]
 
  if m == 0:
    dp[i][m] = 1
  elif i >= n:
    dp[i][m] = 0
  elif solve(i+1, m):#使わない
    dp[i][m] = 1
  elif solve(i+1, m-A[i]):#使う
    dp[i][m] = 1
  else:
    dp[i][m] = 0
 
  return dp[i][m]
 
 
 
n = input()
A = map(int, raw_input().split())
p = input()
m = map(int, raw_input().split())
 
dp = [[-1 for col in range(2000)] for row in range(n+1)]
 
for i in range(p):
  if solve(0, m[i]):
    print 'yes'
  else:
    print 'no'
