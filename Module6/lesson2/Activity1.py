import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((500, 400))  
pygame.display.set_caption("pygame demo")
done = False  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (250, 125, 255), pygame.Rect(40, 40, 70, 70))    
  
    pygame.display.flip()  