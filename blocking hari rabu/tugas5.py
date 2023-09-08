import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  # Set the drawing speed

# Function to draw a petal
def draw_petal():
    flower.color("red")
    flower.begin_fill()
    flower.circle(50, 60)
    flower.left(120)
    flower.circle(50, 60)
    flower.end_fill()

# Draw the flower
for _ in range(6):
    draw_petal()
    flower.left(60)

# Draw the flower's stem
flower.color("green")
flower.penup()
flower.goto(0, -200)
flower.pendown()
flower.right(90)
flower.forward(200)

# Close the Turtle graphics window on click
screen.exitonclick()
