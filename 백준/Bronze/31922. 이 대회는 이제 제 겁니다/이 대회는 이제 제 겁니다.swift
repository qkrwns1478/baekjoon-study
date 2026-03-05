let input = readLine()!.split(separator: " ").map { Int($0)! }
let A = input[0], P = input[1], C = input[2]
print(max(A+C, P))