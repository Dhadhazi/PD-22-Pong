from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))


screen.listen()
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s")


game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()