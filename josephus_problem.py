from queue_implementation import *


def getPosition(n, k):
    start = 0
    for i in range(1, n + 1):
        start = ((start - k) % i) + 1
    result = n - start + 1
    return result


def main():
    n = int(input('Enter number of people: '))
    k = int(input('Enter position of people to be killed: '))
    print(getPosition(n, k))


if __name__ == '__main__':
    main()
