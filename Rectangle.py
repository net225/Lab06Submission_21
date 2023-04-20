class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))

# class Button(Rectangle):
#     def __init__(self, x=0, y=0, w=0, h=0):
#         Rectangle.__init__(self, x, y, w, h)
    
#     def isMouseOn(self):
#         #Implement your code here
#         px,py = pg.mouse.get_pos()
#         if self.x <= px <= self.x+self.w and self.y <= py <= self.y+self.h :
#             return True
#         else:
#             return False

import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(20,20,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    firstObject.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

# import sys 
# import pygame as pg

# pg.init()
# run = True
# win_x, win_y = 800, 480
# screen = pg.display.set_mode((win_x, win_y))
# btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

# while(run):
#     screen.fill((255, 255, 255))
#     if btn.isMouseOn():
#         btn.w = 200
#         btn.h = 300
#     else:
#         btn.w = 100
#         btn.h = 100
#     btn.draw(screen)
    
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False
    