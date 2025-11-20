base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
T = int(input())
for t in range(1, T+1):
    s = input()
    s_nums = [base.index(c) for c in s]
    s_bins = ''.join(bin(i)[2:].zfill(6) for i in s_nums)
    answer = ''
    for i in range(0, len(s_bins), 8):
        answer += chr(int('0b' + s_bins[i:i+8], 2))
    print(f"#{t} {answer}")