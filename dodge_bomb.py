import sys
import pygame as pg
import random


WIDTH, HEIGHT = 800, 600 # 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # 背景画
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    # こうかとん画
    kk_img = pg.image.load("ex02/fig/3.png") 
    # 爆弾サークル
    
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0)) # 透明化のためのset_colorkey
    # rect抽出, randomで乱数発生し、座標を決める
    img_baku = enn.get_rect()
    x, y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
    img_baku.center = x, y
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [450, 100]) # 900, 400
        # enn-> 円 img_baku->座標を設定
        screen.blit(enn, img_baku)
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()