import pygame 
from SnakeM import *
pygame.init()

screen=pygame.display.set_mode((450,450))
runing =True
sn=serpiente();
Fps=pygame.time.Clock()
a="white"
fin=True
while runing:
   # selecionar algun boton
    vp=8
    for event in pygame.event.get():
        #izq =3: der=1:arib=4:abajo=1
        if event.type == pygame.QUIT:
            runing = False
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_UP):
                vp=4
            if event.key==pygame.K_DOWN:
                vp=2
            if event.key==pygame.K_LEFT:
                vp=3
            if event.key==pygame.K_RIGHT:
                vp=1    
            if event.key==pygame.K_SPACE:
                sn.reiniciar();
                
    screen.fill(a)
    
  
    if sn.vivo :
        sn.mover(vp)
        lP=sn.getCola();
        pygame.draw.rect(screen,'RED',[sn.pi[0]*30,sn.pi[1]*30,30,30],0,2)
        for x in lP:
                pygame.draw.rect(screen,'BLUE',[x[0]*30,x[1]*30,30,30],0,2)
        # flip() the display to put your work on screen
        
        pygame.display.flip()
        Fps.tick(int(len(lP)+5)/4)  # creacion de fixels
    else:
        #escribir mensaje 
        letra30 = pygame.font.SysFont("Arial", 28)
        imagenTextoPresent = letra30.render(("Fin de juego "),
        True,(0,0,0), (200,200,200)  )
        rectanguloTextoPresent = imagenTextoPresent.get_rect()
        screen.blit(imagenTextoPresent, (150,100))
        img2=letra30.render(("tu puntuacion es: %d")%len(sn.queue),True,(0,0,0), (200,200,200) )
        screen.blit(img2, (150,200))
        
        pygame.display.flip()
        
pygame.quit()