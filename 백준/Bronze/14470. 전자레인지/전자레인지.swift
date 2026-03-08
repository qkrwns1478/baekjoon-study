let A = Int(readLine()!)!
let B = Int(readLine()!)!
let C = Int(readLine()!)!
let D = Int(readLine()!)!
let E = Int(readLine()!)!
let time = (A < 0 ? -A * C : 0) + (A <= 0 ? D : 0) + (A > 0 ? (B - A) * E : B * E)
print(time)