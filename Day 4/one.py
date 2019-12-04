def check_baguette(v: str):
    dbl = False
    d = 0
    for i in v:
        if int(i) >= d:
            d = int(i)
            dbl = dbl or v.count(i) >= 2
        else:
            return False
    return dbl

print(sum([int(check_baguette(str(v))) for v in range(357253, 892942 + 1)]))