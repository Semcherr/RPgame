import pygame as pg
from  helper import Sprite_sheet
from pygame.math import Vector2
class Player(pg.sprite.Sprite):      # создание персонаж
    speed=5
    def __init__(self,sprite_sheet_path,pos):
        super().__init__()
        sprite_sheet=Sprite_sheet(sprite_sheet_path,4)
        self._load_images(sprite_sheet)
        self.image=self.walk_right[0]
        self.rect=self.image.get_rect()
        self.rect.center=pos
    def _load_images(self,sheet):
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []
        w, h = sheet.w // 4, sheet.h // 4
        for x in range(0, w * 4, w):
            self.walk_down.append(sheet.get_image(x, 0, w, h))
            self.walk_left.append(sheet.get_image(x, h, w, h))
            self.walk_right.append(sheet.get_image(x, h * 2, w, h))
            self.walk_up.append(sheet.get_image(x, h * 3, w, h))
    def _move(self):
        self.velocity=Vector2(0,0)
        keys=pg.key.get_pressed()
        if keys [pg.K_w]:
            self.velocity.y=-1
        if keys [pg.K_s]:
            self.velocity.y=1
        if keys [pg.K_d]:
            self.velocity.x=1
        if keys [pg.K_a]:
            self.velocity.x=-1
        if self.velocity.length()>1:
            self.velocity.x=0
        self.velocity*=Player.speed
        self.rect.center+=self.velocity
    def update(self):
        self._move()