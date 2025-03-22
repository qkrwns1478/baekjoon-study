a = input()
b = input()
c = input()

t = {"black": 0, "brown": 1, "red": 2, "orange": 3,
      "yellow": 4, "green": 5, "blue": 6, "violet": 7,
      "grey": 8, "white": 9}

n = t[a] * 10 + t[b]
n *= 10 ** t[c]
print(n)