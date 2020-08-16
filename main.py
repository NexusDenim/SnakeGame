# Muhammad Shahab First Game
import pygame as game
import config
import Player

game_running = True
screen = None


def game_start():
    global screen
    game.init()
    screen = game.display.set_mode((config.game_config['width'], config.game_config['height']))
    game.display.set_caption(config.game_config['game_name'])
    game_icon = game.image.load(config.game_config['game_icon'])
    game.display.set_icon(game_icon)


def main_loop():
    global game_running
    while game_running:
        player.set_player_speed(10)
        for event in game.event.get():
            if event.type == game.QUIT: game_running = False
            if event.type == game.KEYDOWN or event.type == game.KEYUP:
                if event.key == game.K_LEFT:
                    player.move_left()
                elif event.key == game.K_RIGHT:
                    player.move_right()
                elif event.key == game.K_UP:
                    player.move_up()
                elif event.key == game.K_DOWN:
                    player.move_down()

        game.display.update()


game_start()
player = Player.Player(game, screen)
main_loop()
