import turtle
my_wendow=turtle.Screen()
my_wendow.bgcolor("lightblue")

# # Turtle.done()  # Keep the window 
# # Function to draw text with different colors
# def draw_text():
#     window = turtle.Screen()
#     window.bgcolor("white")

#     # Create a turtle named "artist"
#     artist = turtle.Turtle()
#     artist.speed(2)
    
#     colors = ["red", "green", "blue", "orange", "green", "yellow", "aqua", "magenta"]
#     text = "HI I'M LETA KASAHUN"
    
#     artist.penup()
#     artist.goto(-200, 0)
#     artist.pendown()
    
#     for index, letter in enumerate(text):
#         artist.color(colors[index % len(colors)])
#         artist.write(letter, font=("Arial", 24, "normal"))
#         artist.forward(30)
    
#     window.mainloop()

# draw_text()

# my_turtle=turtle.Turtle()
# my_turtle.color("red")
# my_turtle.pensize(10)
# #square shape
# for i in range(4):
#     my_turtle.forward(200)
#     my_turtle.right(90)
# turtle.done()
# #isosles tringle
# triangle=turtle.Turtle()
# triangle.color("aqua")
# triangle.pensize(10)
# triangle.forward(100)
# triangle.left(120)
# triangle.forward(100)
# triangle.left(120)
# triangle.forward(100)
# turtle.done()
##rectangle height 200px,windth 400px
# rektangle=turtle.Turtle()
# rektangle.color("blue")
# rektangle.pensize(10)
# rektangle.forward(300)
# rektangle.left(90)
# rektangle.forward(150)
# rektangle.left(90)
# rektangle.forward(300)
# rektangle.left(90)
# rektangle.forward(150)
##hexagon with 150 length
# hexagon=turtle.Turtle()
# hexagon.color("grey")
# hexagon.pensize(20)
# for i in range(6):
#     hexagon.forward(150)
#     hexagon.left(60)
# turtle.done()
##right angle triangle
# rightangle_triangle=turtle.Turtle()
# rightangle_triangle.color("orange")
# rightangle_triangle.pensize(15)
# rightangle_triangle.forward(200)
# rightangle_triangle.left(135)
# rightangle_triangle.forward(280)
# rightangle_triangle.left(135)
# rightangle_triangle.forward(200)
# turtle.done()
##my name "T"
# letter_T=turtle.Turtle()
# letter_T.pensize(15)
# letter_T.color("yellow")
# letter_T.speed()
# letter_T.forward(300)
# letter_T.backward(150)
# letter_T.right(90)
# letter_T.forward(600)
# turtle.done()
##star drawing
# stars=turtle.Turtle()
# stars.color("green")
# stars.pensize(8)
# for i in range(5):
#     stars.forward(30)
#     stars.right(144)
# turtle.done()    
# ##square in other squere
# insert_squere=turtle.Turtle()
# insert_squere.pensize(5)
# insert_squere.color("green")
# def drawing_squere(sizes):
#     for  i in range(4):
#         insert_squere.fd(sizes)
#         insert_squere.left(90)
#         sizes-=5
#     turtle.done()
# drawing_squere(240)

# drawing_squere(220)

# drawing_squere(200)
##circle with raduis 100px
# my_cicle=turtle.Turtle()
# my_cicle.pensize(5)
# my_cicle.color("yellow")
# my_cicle.circle(100)
# my_cicle.speed(1)
# turtle.exitonclick()

##ammazing heart
# # Function to draw a heart
# def draw_heart():
#     window = turtle.Screen()
#     window.bgcolor("white")

#     # Create a turtle named "artist"
#     artist = turtle.Turtle()
#     artist.shape("turtle")
#     artist.color("red")
#     artist.speed(2)

#     # Start filling the heart with red color
#     artist.begin_fill()

#     # Draw the left curve
#     artist.left(140)
#     artist.forward(113)
#     artist.circle(-57, 200)

#     # Draw the right curve
#     artist.left(120)
#     artist.circle(-57, 200)
#     artist.forward(113)

#     # End filling the heart with red color
#     artist.end_fill()

#     window.mainloop()

# # Call the draw_heart function to start drawing
# draw_heart()


#arthictic practice
# pen=turtle.Turtle()
# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
# def heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curve()
#     pen.forward(120)
#     curve()
#     pen.forward(112)
#     pen.end_fill()

# for i in range(3):
#         heart()
#         curve()
# turtle.done()