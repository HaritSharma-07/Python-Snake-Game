from turtle import Screen, Turtle
import time
from project_day_21.snake import Snake
from project_day_21.SnakeFood import Food
from project_day_21.scoreboard import GameScoreboard

game_on = True

screen = Screen()
screen.setup(width = 600 , height = 600)
tillu = Turtle()
image = "grass_for_snake-ezgif.com-avif-to-gif-converter.gif"
screen.addshape(image)
tillu.shape(image)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = GameScoreboard()

screen.listen()
screen.onkey(key = "Up" or "w", fun = snake.up)
screen.onkey(key = "Down" or "s", fun = snake.down)
screen.onkey(key = "Left" or "a", fun = snake.s_left)
screen.onkey(key = "Right" or "d", fun = snake.s_right)

while game_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        snake.reset()
        time.sleep(4)
        scoreboard.reset_game()

    for collide in snake.group[1:]:
        if snake.head.distance(collide) < 15:
            snake.reset()
            time.sleep(4)
            scoreboard.reset_game()

screen.exitonclick()