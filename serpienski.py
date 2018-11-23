import turtle

WINDOW_HEIGHT = 1500
WINDOW_BREADTH = 1500
t = turtle.Turtle()


def initialize():
    turtle.Screen().screensize(WINDOW_BREADTH, WINDOW_HEIGHT)
    turtle.Screen().title("Serpienski")
    base_length = 200
    turtle.Screen().tracer(0)

    t.up()
    t.left(90)
    t.backward(base_length / 2)
    t.right(90)
    t.backward(base_length / 2)
    t.speed(0)


def draw_serpienski(depth, base_length):
    if depth == 0:
        return
    t.down()

    t.begin_fill()
    for index in range (4):
        t.forward(base_length)
        t.left(90)
    t.end_fill()

    t.up()
    t.left(90)
    t.forward(base_length/3)
    t.right(90)
    t.forward(base_length*4/3)

    for index in range(4):
        t.down()
        draw_serpienski(depth - 1,base_length/3)
        t.up()
        t.left(90)
        t.forward(base_length)
        t.right(90)
        draw_serpienski(depth - 1, base_length/3)
        t.up()
        t.backward(base_length*2/3)
        t.left(90)

    t.backward(base_length*4/3)
    t.left(90)
    t.backward(base_length/3)
    t.right(90)




def main():
    initialize()

    depth = int(input("Enter depth of Serpienski carpet: "))
    base_length = 200

    draw_serpienski(depth,base_length)

    turtle.Screen().update()
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()
