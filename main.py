# Muhammad Shahab First Game
import pygame as game

game.init()
game.display.set_mode((800,800))
game_running = True

while game_running:
    for event in game.event.get():
        if event.type == game.QUIT:
            game_running = False
