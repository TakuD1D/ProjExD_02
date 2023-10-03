import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900 # 1600, 900

delta = { # 移動量の辞書
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, 5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (5, 0),
}

""" 画面外判定 """
def check_bound(img_rect: pg.Rect) -> tuple:
    """
    引数：こうかとん、爆弾Rect
    戻り値 ：タプル、横方向判定、縦方向判定
    画面内なら: True, 画面外なら；False
    """
    width_check = True
    height_check =True
    # 横判定
    if img_rect.left < 0 or WIDTH < img_rect.right:
        width_check = False
    #　縦判定
    if img_rect.top < 0 or HEIGHT < img_rect.bottom:
        height_check = False
    return width_check, height_check

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    
    # 背景画
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    
    # こうかとん画
    kk_img = pg.image.load("ex02/fig/3.png") 
    
    """ 爆弾サークル """
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0)) # 透明化のためのset_colorkey
    img_baku = enn.get_rect()
    x, y = random.randint(0,WIDTH), random.randint(0,HEIGHT)
    img_baku.center = x, y
    
    """こうかとん Rect"""
    kk_rect = kk_img.get_rect()
    kk_rect.center = (900, 400)
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    
    """ 設定 """
    clock = pg.time.Clock()
    tmr = 0
    vx, vy = 5, 5 # 爆弾移動量
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        """ 背景画のblit """
        screen.blit(bg_img, [0, 0])
            
        """" キーを取得してこうかとんを動かす """
        key_lst = pg.key.get_pressed()
        sum_move = [0, 0]
        for key,value in delta.items():
            if key_lst[key]:
                sum_move[0] += value[0] # 横方向
                sum_move[1] += value[1] # 縦方向
        kk_rect.move_ip(sum_move[0], sum_move[1])
        screen.blit(kk_img, kk_rect) # 900, 400
        
        """爆弾"""
        img_baku.move_ip(vx, vy)
        screen.blit(enn, img_baku) # enn-> 円 img_baku->座標を設定
        
        """ 設定 """
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()