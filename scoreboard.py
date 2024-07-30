from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open('high_score.txt') as high_score:
            self.high_score = int(high_score.read())
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.up_score()

    def up_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            with open('high_score.txt', mode='w') as high_score:
                high_score.write(str(self.score))
        self.write(arg=f'Score: {self.score} High Score:{self.high_score}', align='center',
                   font=('Arial', 15, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.write(arg=f'Game Over', align='center', font=('Arial', 30, 'normal'))
        self.goto(0, 0)
        if self.score > self.high_score:
            self.write(arg=f'Congrats!. You have beated your record with: {self.score}', align='center',
                       font=('Arial', 15, 'normal'))
        else:
            self.write(arg=f'Final Score: {self.score}', align='center', font=('Arial', 15, 'normal'))
        self.goto(0, -20)
        self.write(arg=f'ENTER to star again', align='center', font=('Arial', 10, 'normal'))
