class Char:
    def __init__(self, value):
        self.value = value
        self.child = dict()
    def add_child(self, child):
        self.child[child.value] = child

end = Char('#')

def solution(cur, p):
    if cur == end:
        global answer
        answer += p
        return
    for nc in cur.child:
        dp = 1 if len(cur.child) > 1 else 0
        np = p + dp if nc != '#' else p
        solution(cur.child[nc], np)

while True:
    try:
        n = int(input())
        d = dict()
        for _ in range(n):
            word = input()
            if word[0] not in d:
                d[word[0]] = Char(word[0])
            cur = d[word[0]]
            for i in range(1, len(word)):
                if word[i] not in cur.child:
                    cur.add_child(Char(word[i]))
                cur = cur.child[word[i]]
            cur.add_child(end)
        answer = 0
        for c in d:
            solution(d[c], 1)
        print("%0.2f" % (answer / n))
    except EOFError:
        break