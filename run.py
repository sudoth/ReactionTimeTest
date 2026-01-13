import pygame
import random
import time
import sys
from config import HEIGHT, WIDTH
from screens import GreenScreen, GreenScreenResult, RedScreen, RedScreenMissclick, BlueScreen


def Run(screen):
  reaction_start_time = 0
  clock = time.time()
  flag = False
  running = True
  RedScreen(screen)

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
          
      elif event.type == pygame.MOUSEBUTTONDOWN and flag:
        reaction_time = int((time.time() - reaction_start_time) * 1000)
        GreenScreenResult(screen, reaction_time)
        running = False

      elif event.type == pygame.MOUSEBUTTONDOWN and not flag:
        reaction_time = int((time.time() - reaction_start_time) * 1000)
        RedScreenMissclick(screen)
        running = False

    if random.randint(0, 100) == 0 and not flag and time.time() - clock > 1:
        GreenScreen(screen)
        reaction_start_time = time.time()
        flag = True

    pygame.time.delay(10)
    
def main():
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Тест на скорость реакции")
  BlueScreen(screen)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:    
        Run(screen)


main()
