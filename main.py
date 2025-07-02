from random import randint
from math import hypot
from pygame import *
init()

window = display.set_mode((750, 750))
clock = time.Clock()
my_player = [0, 0, 20]

class Food:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c
    def check_collision(self, player_x, player_y, player_r):
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx, dy) <= self.radius + player_r
    
foods = [Food(randint(-2000, 2000), randint(-2000, 2000), 10, (randint(0, 255), randint(0, 255), randint(0, 255)))
         for _ in range(300)]

running = True

while running:
    window.fill((0, 0, 0))
    scale = max(0.3, min(50/my_player[2], 1.5))
    for e in event.get():
        if e.type == QUIT:
            running = False
    draw.circle(window, (0, 255, 0), (375, 375), int(my_player[2] * scale))

    to_remove = []
    for food in foods:
        if food.check_collision(my_player[0], my_player[1], my_player[2]):
            to_remove.append(food)
            my_player[2] += int(food.radius * 0.2)
        else:
            sx = int((food.x - my_player[0]) * scale + 500)
            sy = int((food.y - my_player[0]) * scale + 500)
            draw.circle(window, food.color, (sx, sy), int(food.radius * scale))
    for food in to_remove:
        foods.remove(food)
	
    display.update()
    clock.tick(60)

    keys = key.get_pressed()
    if keys[K_w]: my_player[1] -= 15
    if keys[K_s]: my_player[1] += 15
    if keys[K_a]: my_player[0] -= 15
    if keys[K_d]: my_player[0] += 15
quit()