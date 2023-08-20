from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2.0

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.penup()
        new_car.goto(270, random.randint(-250, 250)) 
        new_car.setheading(90)
        self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE * MOVE_INCREMENT
            car.goto(new_x, car.ycor())
            
    def increase_speed(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 0.3
            