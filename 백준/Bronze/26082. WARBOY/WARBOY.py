def 가격대비성능(성능, 가격):
    return 성능 // 가격

경쟁사가격, 경쟁사제품성능, WARBOY가격 = map(int, input().split())
경쟁사가격대비성능 = 가격대비성능(경쟁사제품성능, 경쟁사가격)
WARBOY가격대비성능 = 경쟁사가격대비성능 * 3
WARBOY성능 = WARBOY가격대비성능 * WARBOY가격
print(WARBOY성능)