import turtle
window=turtle.Screen()
window.bgcolor("lightblue")
artist=turtle.Turtle()
artist.color("blue")
artist.speed(3)
artist.pensize(5)
artist.pencolor("red")
artist.forward(200)
artist.penup()
artist.forward(20)
artist.pendown()
artist.forward(100)
artist.begin_fill()
artist.circle(100)
artist.end_fill()
window.mainloop()


