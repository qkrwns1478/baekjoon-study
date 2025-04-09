tile = dict()
tile[2] = 3
tile[4] = 11
tile[6] = 41
tile[8] = 153
tile[10] = 571
tile[12] = 2131
tile[14] = 7953
tile[16] = 29681
tile[18] = 110771
tile[20] = 413403
tile[22] = 1542841
tile[24] = 5757961
tile[26] = 21489003
tile[28] = 80198051
tile[30] = 299303201

n = int(input())
if n not in tile:
    print(0)
else:
    print(tile[n])