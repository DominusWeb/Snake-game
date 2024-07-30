from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import ScoreBoard
import time


class SnakeGame:

    def __init__(self):
        self.screen = Screen()
        self.game()

    def game(self):

        self.screen.setup(600, 600)

        self.screen.title('My snake game')
        self.screen.bgcolor('black')
        self.screen.tracer(0)

        snake = Snake()
        food = Food()
        scoreboard = ScoreBoard()

        self.screen.listen()
        self.screen.onkey(key='Right', fun=snake.right)
        self.screen.onkey(key='Down', fun=snake.down)
        self.screen.onkey(key='Up', fun=snake.up)
        self.screen.onkey(key='Left', fun=snake.left)
        self.screen.onkey(key='Return', fun=self.reseat)

        game_over = False

        while not game_over:
            self.screen.update()
            time.sleep(0.1)
            snake.move()
            if snake.head.distance(food) < 15:
                food.change_position()
                scoreboard.up_score()
                snake.add_tail()
            if (
                    snake.head.xcor() > 280
                    or snake.head.xcor() < -280
                    or snake.head.ycor() > 280
                    or snake.head.ycor() < -280
            ):
                scoreboard.game_over()
                game_over = True
            for piece in snake.segments[1:]:
                if snake.head.distance(piece) < 10:
                    scoreboard.game_over()
                    game_over = True
        self.screen.exitonclick()

    def reseat(self):
        self.screen.clear()
        SnakeGame()


snake_game = SnakeGame()

'''Thing to impove:
- Turtle hide when game over
- Collapse in the very side of the wall
- Ball doesn´t appear where is a part of the snake
- Organize it to be clearer'''