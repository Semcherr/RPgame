import pygame as pg
from  helper import Sprite_sheet
from pygame.math import Vector2
class Player(pg.sprite.Sprite):      # создание персонаж
    speed=5
    def __init__(self,sprite_sheet_path,pos):
        super().__init__()
        sprite_sheet=Sprite_sheet(sprite_sheet_path,4)
        self.cycle_len = 4
        self._load_images(sprite_sheet)
        self.image=self.walk_right[0]
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.last_update=0
        self.frame=0
        self.velocity=Vector2(0,0)
    def _load_images(self,sheet):
        self.walk_right = []
        self.walk_left = []
        self.walk_up = []
        self.walk_down = []
        w, h = sheet.w // self.cycle_len, sheet.h // self.cycle_len
        for x in range(0, w * 4, w):
            self.walk_down.append(sheet.get_image(x, 0, w, h))
            self.walk_left.append(sheet.get_image(x, h, w, h))
            self.walk_right.append(sheet.get_image(x, h * 2, w, h))
            self.walk_up.append(sheet.get_image(x, h * 3, w, h))
    def _move(self):
        self.velocity.update(0,0)
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
        self._animate()
    def _animate(self,frame_len=100):     # анимация
        now=pg.time.get_ticks()
        if now-self.last_update>frame_len and self.velocity.length()>0:
            self.last_update=now
            if self.velocity.y>0:
                self.animations_cycle=self.walk_down
            elif self.velocity.y<0:
                self.animations_cycle=self.walk_up
            elif self.velocity.x>0:
                self.animations_cycle=self.walk_right
            elif self.velocity.x<0:
                self.animations_cycle=self.walk_left
            self.frame=(self.frame+1)%self.cycle_len
            self.image=self.animations_cycle[self.frame]
