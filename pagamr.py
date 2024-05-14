import pygame
pygame.init() #Pygame'i tööli rakendamiseks
ekraani_pind=pygame.display.set_mode( (640, 480 )) #akna pind, 640 on akna laius, 480- kõrgus
ekraani_pind.fill( (105,105,105) ) #värvime tekitatud pinna grey
pygame.display.set_caption("YOOOOO")

ristkylik1=pygame.Rect(100, 50, 100, 100) #Argumentid: x koordinaat, y koordinat, laius, kõrgus
pygame.draw.rect(ekraani_pind, (211,211,211), ristkylik1)#surface, color, rect

pygame.draw.circle(ekraani_pind, (211,211,211), [150,210], 100, 100 )

pygame.draw.line(ekraani_pind,(211,211,211), [215,145],[270,270], 50)
pygame.draw.line(ekraani_pind, (211, 211, 211), [80, 150], [30, 280], 50)

pygame.draw.rect(ekraani_pind, (47,79,79), [1, 400, 640, 200], 100)

pygame.draw.ellipse(ekraani_pind, (211, 211, 211), [100, 290, 50, 180], 50)
pygame.draw.ellipse(ekraani_pind, (211, 211, 211), [150, 290, 50, 180], 50)


pilt1=pygame.image.load("chad.jpg")
pilt1=pygame.transform.scale(pilt1,(90,90))
ekraani_pind.blit(pilt1, (105, 55))#pilt1 (x,y)

tekst="Tere, Pygame! x_x"
pygame.draw.circle(ekraani_pind, (139, 128, 0), [580,20], 50, 100 )
meie_font=pygame.font.SysFont("Verdana", 36)
teksti_pilt=meie_font.render(tekst, False, (0,0,0))
ekraani_pind.blit(teksti_pilt, (300,30))

pygame.display.flip() #soovime pilt kasutajale näidata
while True:
    event=pygame.event.poll()
    if event.type==pygame.quit:
        break
pygame.quit()
