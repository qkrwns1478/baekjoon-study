while True:
    try:
        code = input()
        while "BUG" in code:
            code = code.replace("BUG","")
        print(code)
    except:
        break