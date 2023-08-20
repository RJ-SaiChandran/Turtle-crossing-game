import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move_forward, "Up")
    
    should_generate_car = random.choice([True, False])
    
    if should_generate_car:
        car.create_car()
    
    car.move_cars()
    
    #Detect car collision
    
    for car_obj in car.all_cars:
         if player.distance(car_obj) < 20:
            game_is_on = False
            score.game_over()

        
    if player.ycor() > 280:
        player.goto(0, -280)  
        car.increase_speed()
        score.increase_level()


screen.exitonclick()