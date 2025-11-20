T = int(input())
for _ in range(T):
    d = [0] * 10
    S = input()
    for c in S:
        d[int(c)] += 1

    def check1():
        for i in range(10):
            if d[i] not in (0, 2):
                return False
        return True

    def check2():
        visited = set()
        for i in range(len(S)):
            c = S[i]
            if c not in visited:
                visited.add(c)
                next_i = i + int(c) + 1
                if next_i >= len(S) or S[next_i] != c:
                    return False
        return True

    print("yes" if check1() and check2() else "no")