let N = Int(readLine()!)!
var ans = 0
for _ in 0..<N {
    let s = readLine()!
    if s.hasPrefix("C") { ans += 1 }
}
print(ans)