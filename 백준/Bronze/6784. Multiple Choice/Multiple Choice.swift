let N = Int(readLine()!)!

var A = [String]()
for _ in 0..<N {
    A.append(readLine()!)
}

var B = [String]()
for _ in 0..<N {
    B.append(readLine()!)
}

var ans = 0
for i in 0..<N {
    if A[i] == B[i] {
        ans += 1
    }
}

print(ans)