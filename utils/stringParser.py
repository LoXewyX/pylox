def UpperChecker(pswd, max=1):
        c = 0
        l = [ele.isupper() for ele in pswd]
        for x in l:
            if x: c += 1
        if c >= max: return True
        return False