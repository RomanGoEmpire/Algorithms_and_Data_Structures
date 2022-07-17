import random


def find():
    numbers = [0] * 100
    for i in range(100):
        numbers[i] = random.randint(0, 1000)
    biggest = []
    for n in range(10):
        big = (-1, 0)
        for i in enumerate(numbers):
            if int(i[1]) > int(big[1]):
                big = i
        numbers[big[0]] = 0
        biggest.append(big[1])
    return biggest


def find2():
    numbers = [0] * 100
    for i in range(100):
        numbers[i] = random.randint(0, 100)
    biggest = [0] * 100
    counter = 0
    for i in range(100):
        for n in range(10):
            counter += 1
            if numbers[i] > biggest[n]:
                biggest[n] = numbers[i]
                numbers[i] = 0
                break
    return counter


def test():
    arr = [0] * 10
    for n in arr:
        print(n)


if __name__ == '__main__':
    best = [0] * 1000
    for i in range(100000):
        current = find2()
        best[current - 1] += 1
    for v, n in enumerate(best):
        print(n)
