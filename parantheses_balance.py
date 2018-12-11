from stack_implementation import *

def checkBalanced(expression):
    stackP = Stack()
    for bracket in expression:
        if bracket == '(':
            stackP.push(bracket)
        else:
            if stackP.peek() == '(':
                stackP.pop()
            else:
                return False

    if stackP.__sizeof__() == 0:
        return True
    else:
        return False

def main():
    expression = input('Enter parantheses expresssion: ')
    print(checkBalanced(expression))


if __name__ == '__main__':
    main()