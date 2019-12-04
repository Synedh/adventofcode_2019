min = 357253
max = 892942

def check_baguette(v: str):
    dbl = False
    d = 0
    for i in v:
        for j in v:
            if i == j:
                dbl = True
        if int(i) >= d:
            d = int(i)
        else:
            return False
    return dbl

i = 0
for v in range(min, max + 1):
    i += int(check_baguette(str(v)))
print(i)
