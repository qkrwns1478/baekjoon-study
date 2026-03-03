let T = Int(readLine()!)!
for _ in 0..<T {
    let _ = Int(readLine()!)!
    let A = readLine()!.split(separator: " ").map { Int($0)! }
    print(A.reduce(0, +))
}