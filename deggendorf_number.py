dict1 = {0: 1, 1: 1, 2: 1}


def deg(n):
    if n not in dict1:
        dict1[n] = deg(n - 1) + deg(n - 2) + deg(n - 3)
    return dict1[n]


def easy_deg(n):
    if n < 3:
        return 1
    return easy_deg(n - 1) + easy_deg(n - 2) + easy_deg(n - 3)


if __name__ == '__main__':
    for i in range(34):
        print(i, easy_deg(i))
    # for i, k in dict1.items():
    #  print(i, k)
