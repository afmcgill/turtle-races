import turtle
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')

def create_racing_turtle(color ='black', shape='turtle'):
  my_turtle = turtle.Turtle()
  my_turtle.shape(shape)
  my_turtle.color(color)
  my_turtle.pensize(3)
  my_turtle.speed(8)
  return my_turtle

def draw_finish(a_list):
  inv_turtle = turtle.Turtle()
  inv_turtle.hideturtle()
  inv_turtle.pensize(5)
  inv_turtle.speed(10)
  inv_turtle.color('purple')
  inv_turtle.penup()
  inv_turtle.forward(220) #changed from 200 so they don't cross line
  inv_turtle.pendown()
  inv_turtle.left(90)
  inv_turtle.forward((len(a_list)-1) *50)
  # penup, pendown and movement methods to move the turtle forward 200 pixels and then draw a vertical line up towards the top of the screen

def start_positions(a_list):
  for index in range(len(a_list)): 
    a_list[index].penup()
    a_list[index].goto(-200,(index *50))
    a_list[index].pendown()


def main():
  turtle_1 = create_racing_turtle('blue','circle')
  turtle_2 = create_racing_turtle('green')
  turtle_3 = create_racing_turtle('yellow')
  turtle_4 = create_racing_turtle('red')
  
  racers = [turtle_1, turtle_2, turtle_3, turtle_4]

  draw_finish(racers)
  start_positions(racers)

# Run the Race
  racing = True
  while racing == True:
    for turtle in racers:
      num_steps = random.randint(5,20)
      turtle.forward(num_steps)
      # print(turtle.xcor())
    if turtle.xcor() >= 200:
      turtle.write("I win!\t", align='right')
      racing = False
    

main()

# ann = turtle.Turtle()
# bob = turtle.Turtle()
# mae = turtle.Turtle()
# syd = turtle.Turtle()

# trtl_list = [ann, bob, mae, syd] 

# Randomly assign a shape to a turtle.
# def assign_turtle_shape(name):
#   shapes = ['circle', 'square', 'classic', 'turtle', 'triangle']
#   name.shape(random.choice(shapes))

# Randomly assign a color to a turtle.
# def assign_turtle_color(name):
#   colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#   name.color(random.choice(colors))

# Assign a specified speed to a turtle, or use the default.
# def assign_turtle_speed(name, rate = 8):
#   name.speed(rate)

# Start different turtles in different locations on the screen.
# def place_turtles(turtles, distance = 120):
#   angle = 360.0/len(turtles)
#   for index in range(len(turtles)):
#     turtles[index].penup()
#     turtles[index].left(angle*index)
#     turtles[index].forward(distance)
#     turtles[index].right(angle*index)
#     turtles[index].pendown()

# Set the shape, speed, and pensize of each turtle in the list.
# for entry in trtl_list:
#   assign_turtle_shape(entry)
#   assign_turtle_speed(entry, 10)
#   entry.pensize(4)

# Call the function to place the turtles.
# place_turtles(trtl_list, 150)


# Nested loop to make the turtles draw simultaneous polygons, rather than sequential. The turtle colors also change for each side of the polygons.

# for side in range(num_sides):
#   for entry in trtl_list:
#     assign_turtle_color(entry)
#     entry.forward(80)
#     entry.left(360.0/num_sides)

# screen.clearscreen()
screen.exitonclick()