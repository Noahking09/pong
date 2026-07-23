import pygame , sys
from settings import *
from paddles import Paddle
from ball import Ball

class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.size = (screen_width , screen_height)
        self.screen = pygame.display.set_mode(self.size)
        self.paddleA = Paddle(WHITE , 18 , 100 , (20 , 300))
        self.all_sprites.add(self.paddleA)
        self.paddleB = Paddle(WHITE , 18 , 100 , (660 , 20))
        self.all_sprites.add(self.paddleB)
        self.ball = Ball(WHITE , 10 , 10 , (350 , 250))
        self.all_sprites.add(self.ball)
        self.scoreA = 0
        self.scoreB = 0
        
    def update_score(self , font):
      if self.ball.boundary_check():
        self.scoreA += 0.5
      elif self.ball.boundary_check() == False:
        self.scoreB += 0.5
      text = font.render(str(self.scoreA) , 1 , WHITE)
      self.screen.blit(text , (200 , 20))
      text = font.render(str(self.scoreB) , 1 , WHITE)
      self.screen.blit(text , (400 , 20))
      
      
      
    
    def play(self):
        pygame.init()
        font = pygame.font.Font(None , 74)
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        run == False

            self.paddleA.get_input(pygame.K_w , pygame.K_s)
            self.paddleB.get_input(pygame.K_UP , pygame.K_DOWN)
            self.ball.boundary_check()
            self.paddle_collide()
            
            self.all_sprites.update()
            self.screen.fill(BLACK)
            self.update_score(font)
            self.update_score(font)
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            
            clock.tick(60)

    def paddle_collide(self):
        if pygame.sprite.collide_mask(self.ball , self.paddleA) or pygame.sprite.collide_mask(self.ball , self.paddleB):
          self.ball.bounce()

    def check_score(self):
        pass
