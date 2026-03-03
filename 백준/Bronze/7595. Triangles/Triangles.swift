while true {
    let N = Int(readLine()!)!
    if N == 0 { break }
    for i in 1...N {
        print(String(repeating: "*", count: i))
    }
}