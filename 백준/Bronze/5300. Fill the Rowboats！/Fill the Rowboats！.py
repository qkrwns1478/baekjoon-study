code = "osvuxz&yyjkl&v{yn.gxx2&ozks/@&&&&gxx4gvvktj.ozks/T&C&otz.yy4yzjot4xkgjrotk./4yzxov.//yzgiq&C&royz./lux&o&ot&xgtmk.72&T17/@&&&&v{yn.yzgiq2&o/&&&&ol&o&+&<&CC&6&ux&o&CC&T@&&&&&&&&v{yn.yzgiq2&(Mu'(/lux&o&ot&xgtmk.rkt.yzgiq//@&&&&vxotz.yzgiqaoc2&ktjC-&-/"

def solution(s, n):
    return ''.join(chr((ord(c) - n) % 128) for c in s)

exec(solution(code, 6))