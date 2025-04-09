import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_val = 0
for i in range(k):
    if arr[i] > max_val:
        max_val = arr[i]
cnt = [0] * (max_val+1)
for i in arr:
    cnt[i] += 1
tap = list()

answer = 0
for i in range(k):
    item = arr[i]
    if item not in tap:
        if len(tap) < n:
            tap.append(item)
            cnt[item] -= 1
        else:
            tmp = set()
            for j in tap:
                if cnt[j] == 0:
                    tap.remove(j)
                    break
                else:
                    tmp.add(j)
            if len(tap) == n:
                future = arr[i+1:]
                for j in future:
                    if len(tmp) == 1:
                        break
                    if j in tmp and j in tap:
                        tmp.remove(j)
                tap.remove(tmp.pop())
            
            '''tmp = tap
            idx = i+1
            while len(tmp) > 1 and idx < k:
                if arr[idx] in tmp:
                    tmp.remove(arr[idx])
                idx += 1
            if len(tmp) == 1:
                tap.remove(tmp[0])
            else:
                out_can = list()
                for j in tmp:
                    heappush(out_can, (cnt[j], j))
                _, bye = heappop(out_can)
                tap.remove(bye)'''
            
            '''future = arr[i+1 : i+n+1]
            out_can = list()
            for j in tap:
                if j not in future:
                    heappush(out_can, (cnt[j], j))
            if out_can:
                _, bye = heappop(out_can)
                tap.remove(bye)
            else:
                #tap.remove(future[-1])
                tmp = tap
                idx = i+1
                while len(tmp) > 1 and idx < k:
                    if arr[idx] in tmp:
                        tmp.remove(arr[idx])
                    idx += 1
                tap.remove(tmp[0])'''
                
            tap.append(item)
            cnt[item] -= 1
            answer += 1
    else:
        cnt[item] -= 1
print(answer)
