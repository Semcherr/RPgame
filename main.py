import pygame as pg #
from settings import *
from player import Player
from helper import res

class Game: # переносим весь код в класс и немного дополняем
    def __init__(self):
        pg.init()  # инициализация
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((sreen_width, screen_height))
        pg.display.set_caption(game_title)
        pg.display.set_icon(pg.image.load('res/sprites/frog_1.png'))
        self.running=True
    def new(self):
        player = Player(r'res/sprites/player_sheet.png', (100, 100))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):  # выключение игры
                self.running = False
    def _update(self):
        self.all_sprites.update()
    def _draw(self):
        self.screen.fill((0, 0, 0))  # настройка экрана
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def run(self):
        while self.running:
            self.clock.tick(fps)
            self._events()
            self._draw()
            self._update()
if __name__=='__main__':  #теперь при запуске игра запускает класс
     game=Game()
     game.new()
     game.run()


