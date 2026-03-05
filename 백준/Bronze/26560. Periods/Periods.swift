let N = Int(readLine()!)!
for _ in 0..<N {
    var s = readLine()!
    if !s.hasSuffix(".") { s += "." }
    print(s)
}