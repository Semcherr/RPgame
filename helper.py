import pygame as pg
from pathlib import Path
import sys
class Sprite_sheet():
    def __init__(self,file_path,scale=1):
        sheet=pg.image.load(file_path).convert_alpha()
        w,h=sheet.get_size()
        target_size=(int(w*scale),int(h*scale))
        self.sheet=pg.transform.scale(sheet,target_size)
        self.w,self.h=self.sheet.get_size()

    def get_image(self,x,y,width,height):           # задаём картинку персонажу
        return self.sheet.subsurface(x,y,width,height)
res=Path(sys.argv[0]).parent/'res'







