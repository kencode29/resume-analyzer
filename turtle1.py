#the turtle library in python is used for drawing pictures, shapes, and designs on the screen
import turtle
# t=turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(100)

# turtle.done()


#making a sq
'''
t=turtle.Turtle()

# for i in range(4):
#     t.forward(100)
#     t.left(90)
# turtle.done()



t.speed(5)

#square
for i in range(4):
    t.forward(100)
    t.left(90)

#roof
t.left(45)
t.forward(70)

t.right(90)
t.forward(70)

#go to center
t.home()

#move using coordinates
t.setx(-150)
t.sety(-50)

#draw a line
t.seth(0)
t.forward(100)

#move backward 
t.backward(50)

turtle.done()   '''
'''
t=turtle.Turtle()
t.hideturtle()
t.speed(1)

t.dot(10,"red")

t.forward(100)

print("X=",t.xcor())
print("Y=",t.ycor())
print("Heading=",t.heading())  #heading -- current direction
t.undo()
turtle.done() '''
'''
t=turtle.Turtle()
t.pencolor("blue")
t.fillcolor("yellow")

t.begin_fill()

for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()
print("filling: ",t.filling())
turtle.done()'''

'''
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("lightblue")
t.speed(1)
turtle.tracer(4,0)
colors=["#FFE0B2","#FFA726","#FB8C00","#3D00E6","#6A0888"]
for i in range(360):
    t.color(colors[i%5])
    t.circle(140)
    t.left(1)
turtle.done()'''


'''
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.tracer(3,0)
t.color("#E0F7FA")
t.width(1)
for i in range(600):
    t.forward(i*1.3)
    t.left(144)
    t.forward(i*0.2)
    t.left(2)
turtle.done()

'''
 
def setup_screen():
    screen=turtle.Screen()
    screen.bgcolor("black")
    screen.title("Mesh effect")
    screen.setup(width=800, height=800)
    return screen   

def setup_turtle():
    t=turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.hideturtle()
    return t

def draw_mesh(t):
    colors=["red","purple","blue","cyan","green","yellow","orange"]
    
    for i in range(150):
        t.pencolor(colors[i%7])
        t.circle(i,180)
        t.left(90)
        t.forward(i)
        t.left(45)
         
def main():
    screen= setup_screen()
    t=setup_turtle()
    
    draw_mesh(t)
    
    screen.exitonclick()
main()    