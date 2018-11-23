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
    t.forward(base_length / 2)
    t.right(90)
    t.backward(75)
    t.speed(0)


def draw_spikes(depth, length):
    t.down()
    if depth == 0:
        t.forward(length)
        return

    draw_spikes(depth - 1, length / 3)
    t.left(60)
    draw_spikes(depth - 1, length / 3)
    t.right(120)
    draw_spikes(depth - 1, length / 3)
    t.left(60)
    draw_spikes(depth - 1, length / 3)


def main():
    initialize()

    depth = int(input("Enter depth of pattern"))
    base_length = 150

    for index in range(6):
        draw_spikes(depth, base_length)
        t.right(60)

    turtle.Screen().update()
    turtle.Screen().mainloop()


if __name__ == "__main__":
    main()
