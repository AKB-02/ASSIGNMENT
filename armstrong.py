for i in range(100, 1000):
    og = i
    s = 0
    temp = i  
    while temp > 0:
        r = temp % 10
        s = s + r * r * r
        temp = temp // 10
    if s == og:
        print(og)

 