import pygame as pg

pg.init()

screen = pg.display.set_mode((200,200),pg.RESIZABLE)

over=False
while not over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            over = True

        if event.type == pg.KEYDOWN:
            Key = event.key
            if Key == pg.K_a:
                print("Left")
            if Key == pg.K_w:
                print("Up")
            if Key == pg.K_s:
                print("Down")
            if Key == pg.K_d:
                print("Right")
pg.quit()