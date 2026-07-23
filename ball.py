import pygame
from settings import *
from random import randint

class Ball(pygame.sprite.Sprite):
  def __init__(self , colour , width , height , pos):
    super().__init__()
    self.image = pygame.Surface((width , height))
    self.image.fill(colour)
    self.rect = self.image.get_rect(topleft = (pos[0] , pos[1]))
    self.velocity = [randint(-8,8) , randint(-8,8)]
    
  def boundary_check(self):
    if self.rect.right > screen_width:
      self.velocity[0] = -self.velocity[0]
      return True
    if self.rect.left < 0:
      self.velocity[0] = -self.velocity[0]
      return False
    if self.rect.top < 0:
      self.velocity[1] = -self.velocity[1]
    if self.rect.bottom > screen_height:
      self.velocity[1] = -self.velocity[1]
      
  def bounce(self):
    self.velocity[0] = -self.velocity[1]
    self.velocity[0] = randint(-8,8)
    
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]