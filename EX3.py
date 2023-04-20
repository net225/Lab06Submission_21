import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)
font = pg.font.Font('freesansbold.ttf', 24) # font and fontsize
text1 = font.render('Name', True,(0, 0, 0)) # (text,is smooth?,letter color,background color)
text2 = font.render('Surname', True,(0, 0, 0))
text3 = font.render('Age', True,(0, 0, 0))
text4 = font.render('Submit', True,(0, 0, 0))


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,color=(0,0,0)):
        Rectangle.__init__(self, x, y, w, h,color)
    
    def isMouseOn(self):
        #Implement your code here
        px,py = pg.mouse.get_pos()
        if self.x <= px <= self.x+self.w and self.y <= py <= self.y+self.h :
            return True
        else:
            return False
    
    def isMousePress(self):
        mouse_presses = pg.mouse.get_pressed()
        if mouse_presses[0] == 1:
            return True
        else:
            return False

btn = Button(350,390,132,50,(220,20,20)) # สร้าง Object จากคลาส Rectangle ขึ้นมา

class InputBox:

    def __init__(self, x, y, w, h, eyejung ,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.eyejung = eyejung
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                txt = event.unicode
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.eyejung:
                    if txt.isnumeric(): # is numberr
                        self.text += txt
                    else:
                        pass
                else:
                    self.text += event.unicode # 'k' '1'
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


input_box1 = InputBox(310, 100, 140, 32 ,False) # สร้าง InputBox1
input_box2 = InputBox(310, 200, 140, 32 ,False) # สร้าง InputBox2
input_box3 = InputBox(310, 300, 140, 32 ,True)

input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
val = 0

while run:
    
    screen.fill((255, 255, 255))
    text5 = font.render("Hello " + input_box1.text +' ' + input_box2.text + "!" + " You are " + input_box3.text + " years old.", True,(0, 0, 0))
    btn.draw(screen)
    screen.blit(text1,(310,72))
    screen.blit(text2,(310,172))
    screen.blit(text3,(310,272))
    screen.blit(text4,(370,400))
    if val == 1:
        screen.blit(text5,(300,350))

    if btn.isMousePress() and btn.isMouseOn():
        val = 1 
        btn.color = (120,20,220)
        text5 = font.render("Hello " + input_box1.text +' ' + input_box2.text + "!" + " You are " + input_box3.text + " years old.", True,(0, 0, 0))
        

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()