import pygame



size=(320,320)
screen= pygame.display.set_mode(size)
width = height = 100
bel = (255, 255, 255)
blue=(0, 0, 255)
red=(255, 0, 0)
otstyp = 10
mas=[[0]*3 for i in range(3)]
igrok=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym =pygame.mouse.get_pos()
            print(f'x={xm}, y={ym}') 
            col= xm//(shir+width)
            row= ym//(dlin+height)
            if mas[row][col]==0:
                if igrok%2==0:
                    mas[row][col]=1
                else:
                    mas[row][col]=2
                igrok+=1
        elif event.type== pygame.KEYDOWN and event.key == pygame.K_SPACE:
            mas=[[0]*3 for i in range(3)]
            igrok=0


            
    for dlin in range(3):
        for shir in range(3):
            if mas[dlin][shir]==1:
                color=blue
            elif mas[dlin][shir]==2:
                color=red
            else:
                color=bel

        
            x =shir*width + (shir)*otstyp
            y =dlin*height +(dlin)*otstyp
    
    
            pygame.draw.rect(screen, color, (x,y, width, height))    
    pygame.display.update()

