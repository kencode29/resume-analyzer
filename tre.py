import turtle

t=turtle.Turtle()
t.speed(1)
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

screen=turtle.Screen()
screen.bgcolor('black')
screen.tracer(0,0)
def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color('pink')
        t.circle(2)
        t.color('brown')
        t.left(20)
        tree(4*i/5)
        t.right(40)
        tree(4*i/5)
        t.left(20)
        
        t.backward(i)
tree(100)
screen.exitonclick()
turtle.done()