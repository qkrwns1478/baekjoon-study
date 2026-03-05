let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0], Q = input[1]
var nums = Set((0..<N).filter { [0, 3, 6].contains($0 % 10) })
for _ in 0..<Q {
    let X = Int(readLine()!)! - 1
    if nums.contains(X) { nums.remove(X) }
    else { nums.insert(X) }
    print(nums.count)
}