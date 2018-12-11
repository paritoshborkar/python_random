"""
People are standing in a circle waiting to be executed. 
Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. 
After a specified number of people are skipped, the next person is executed. 
The procedure is repeated with the remaining people, starting with the next person, 
going in the same direction and skipping the same number of people, until only one person remains, and is freed.

The problem — given the number of people, starting point, direction, and number to be skipped — 
is to choose the position in the initial circle to avoid execution. (From Wikipedia)
"""

def getPosition(n, k):
    start = 0
    for i in range(1, n + 1):
        start = ((start - k) % i) + 1
    result = n - start + 1
    return result


def main():
    n = int(input('Enter number of people: '))
    k = int(input('Enter position of people to be killed: '))
    print('Stand at position: ', getPosition(n, k))


if __name__ == '__main__':
    main()
