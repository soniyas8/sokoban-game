import pygame 

pygame.init()
pygame.display.set_caption("yay")
window= pygame.display.set_mode((640,480))

robot=pygame.image.load("robot.png")



while True:
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
      x=event.pos[0]-robot.get_width()/2
      y=event.pos[1]-robot.get_height()/2

    
      window.fill((0,0,0))
      window.blit(robot,(x,y))
      pygame.display.flip()
      
    if event.type==pygame.QUIT:
     exit()
  
