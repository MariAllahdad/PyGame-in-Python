import pygame
pygame.init()
sr = pygame.display.set_mode((800,500))
pygame.display.set_caption('My Py_Game')
# pygame.image.load('player.png')
GameOver = False
px,py = 200,400
bx,by = 10,10
mx,my = 0.1,0.1
score = 0
fnt = pygame.font.SysFont('Arial',40)
while(not GameOver):
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            GameOver = True
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_LEFT:
                px -= 50
            elif evnt.key == pygame.K_RIGHT:
                px += 50
    sr.fill((0, 0, 255))
    # pygame.time.Clock().tick(50)
    # pygame.draw.circle(sr,(250,250,250),(200,200),50,3)
    # pygame.draw.line(sr,(250,250,250)(10,10),(200,300),3)
    bx += mx
    by += my
    if (bx < 10 or bx > 750):
        mx *= -1
    if (by < 10 or by > 450):
        my *= -1
    if( by > 400):
        GameOver = True
    prt = pygame.Rect(px,py,80,40)
    brt = pygame.Rect(bx, by, 30, 30)
    if (prt.colliderect(brt)):
        my *= -1
        score += 1
        print(score)
    pygame.draw.rect(sr,(250,250,0),prt,20)
    pygame.draw.ellipse(sr, (250, 250, 255), brt, 15)
    txt = fnt.render(f'Score: {score}',True,(0,250,0))
    sr.blit(txt,(10,10))
    pygame.display.update()
