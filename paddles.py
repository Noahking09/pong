import pygame
from settings import *

class Paddle(pygame.sprite.Sprite):
  def __init__(self, colour, width, height, pos):
    super().__init__()
    self.height = height
    self.width = width
    self.image = pygame.Surface((self.width,self.height))
    self.image.fill(colour)
    self.rect = self.image.get_rect(topleft = (pos[0] , pos[1]))
    
    
  def move(self , pixels):
    self.rect.y += pixels
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > screen_height:
      self.rect.bottom = screen_height
  
  def get_input(self , up_key , down_key):
    keys = pygame.key.get_pressed()
    if keys[up_key]:
      self.move(-8)
    if keys[down_key]:
      self.move(8)