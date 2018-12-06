import turtle

def draw_square():

    window= turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle() # creacion del objeto de la clase Turtle, llamando a la lib turtle
    brad.color("yellow")
    brad.speed(50)
    i=0
    j=0
    while i<40:
        brad.right(9)
        while j<4:
            brad.forward(100)
            brad.right(90)
            j+=1
        j=0
        i+=1
        print(i)

    window.exitonclick()

draw_square()
