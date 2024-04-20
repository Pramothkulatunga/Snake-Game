import turtle
import random
import time

# Create screen
screen = turtle.Screen()
screen.title('SNAKE GAME BY PRAMOTH')
screen.setup(width=700, height=700)
screen.tracer(0)
turtle.bgcolor('black')

# Border
border = turtle.Turtle()
border.speed(0)
border.penup()
border.pensize(4)
border.color('red')
border.goto(-310, 250)
for _ in range(2):
    border.pendown()
    border.forward(600)
    border.right(90)
    border.forward(500)
    border.right(90)
border.hideturtle()

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Fruit
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))


# Movement functions...
def snake_go_up():
    if snake.direction != "s":
        snake.direction = "w"

def snake_go_down():
    if snake.direction != "w":
        snake.direction = "s"

def snake_go_left():
    if snake.direction != "d":
        snake.direction = "a"

def snake_go_right():
    if snake.direction != "a":
        snake.direction = "d"

def snake_move():
    if snake.direction == "w":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "s":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "a":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "d":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "w")
screen.onkeypress(snake_go_down, "s")
screen.onkeypress(snake_go_left, "a")
screen.onkeypress(snake_go_right, "d")

# Main game loop
while True:
    screen.update()

    # Snake and fruit collisions
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        # Create new fruit
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Add segments to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    snake_move()

    # Snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write("   GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        score = 0
        delay = 0.1
        snake.goto(0, 0)
        snake.direction = "stop"
        for segment in old_fruit:
            segment.goto(1000, 1000)  # Move off screen
        old_fruit.clear()

    # Snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write("   GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
            score = 0
            delay = 0.1
            snake.goto(0, 0)
            snake.direction = "stop"
            for segment in old_fruit:
                segment.goto(1000, 1000)  # Move off screen
            old_fruit.clear()

    time.sleep(delay)