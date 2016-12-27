def linearSearch(S, key):
    i = 0
    S.append(key)
    while S[i] != key:
        i += 1
    if i == len(S)-1:
        return False
    return True

def main():
    n = int(raw_input())
    S = [int(_) for _ in raw_input().split()]
    q = int(raw_input())
    T = [int(_) for _ in raw_input().split()]
    Sum = 0
    for t in T:
        if linearSearch(S[:], t): Sum += 1
    print Sum
    return 0

main()


