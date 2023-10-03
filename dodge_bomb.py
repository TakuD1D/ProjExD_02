import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900  # 1600, 900
delta = {  # 移動量の辞書
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
    height_check = True
    # 横判定
    if img_rect.left < 0 or WIDTH < img_rect.right:
        width_check = False
    # 　縦判定
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
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_flip = pg.transform.flip(kk_img, True, False)
    kk_rect = kk_img.get_rect()
    kk_rect.center = (900, 400)
    kk_dic = { # こうかとんいろんな角度
        (0, 0): kk_img,
        (0, -5) : pg.transform.rotozoom(kk_img_flip, 90, 1.0),
        (5, -5) : pg.transform.rotozoom(kk_img_flip, 45, 1.0),
        (5, 0) : pg.transform.rotozoom(kk_img_flip, 0, 1.0),
        (5, 5) : pg.transform.rotozoom(kk_img_flip, -45, 1.0),
        (0, 5) : pg.transform.rotozoom(kk_img_flip, -90, 1.0),
        (-5, 5) : pg.transform.rotozoom(kk_img, 45, 1.0),
        (-5, 0) : pg.transform.rotozoom(kk_img, 0, 1.0),
        (-5, -5) : pg.transform.rotozoom(kk_img, -45, 1.0),
        
    }

    """ 爆弾サークル """
    # bb_imgs = []
    # for r in range(1, 11):
    #     enn = pg.Surface((20*r, 20*r))
    #     pg.draw.circle(enn, (255, 0, 0), (10*r, 10*r), 10*r)
    #     enn.set_colorkey((0, 0, 0))
    #     bb_imgs.append(enn)
    #   # 透明化のためのset_colorkey
    
    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    img_baku = enn.get_rect()
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    img_baku.center = (x, y)
    vx, vy = +5, +5  # 爆弾移動量
    accs = [a for a in range(1,11)]
    """ 設定 """
    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        if kk_rect.colliderect(img_baku): #ぶつかり判定
            print("game over")
            return 

        """ 背景画のblit """
        screen.blit(bg_img, [0, 0])
        """" キーを取得してこうかとんを動かす """
        key_lst = pg.key.get_pressed()
        sum_move = [0, 0]
        for key, value in delta.items():
            if key_lst[key]:
                sum_move[0] += value[0]  # 横方向
                sum_move[1] += value[1]  # 縦方向
            
        kk_rect.move_ip(sum_move[0], sum_move[1])
        if check_bound(kk_rect) != (True, True):
            kk_rect.move_ip(-sum_move[0], -sum_move[1])
        for key_, value_ in kk_dic.items():
                if key_ == tuple(sum_move):
                    kk_img = value_
        screen.blit(kk_img, kk_rect)  # 900, 400

        """爆弾"""
        # avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        # bb_img = bb_imgs[min(tmr//500, 9)]
        img_baku.move_ip(vx, vy)
        yoko, tate = check_bound(img_baku)
        if not yoko:  # 横方向はみ出し
            vx *= -1
        if not tate: # 縦方向はみ出し
            vy *= -1
        screen.blit(enn, img_baku)  # enn-> 円 img_baku->座標を設定

        """ 設定 """
        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
