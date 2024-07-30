from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.setpos(position)
            self.segments.append(new_segment)

    def add_tail(self):
        new_tail = Turtle(shape='square')
        new_tail.penup()
        new_tail.color('white')
        new_tail.setpos(self.segments[-1].pos())
        self.segments.append(new_tail)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        else:
            pass

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        else:
            pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        else:
            pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
        else:
            pass
