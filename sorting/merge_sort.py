def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[: mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

    return S


def merge(S1, S2, S):
    for i in range(len(S)):
        if len(S1) == 0:
            S[i] = S2.pop(0)
        elif len(S2) == 0:
            S[i] = S1.pop(0)
        else:
            if S1[0] < S2[0]:
                S[i] = S1.pop(0)
            else:
                S[i] = S2.pop(0)
    return S


if __name__ == '__main__':
    arr2 = [4, 2, 1, 6, 50, 8, 0, 60]
    print(merge_sort(arr2))
