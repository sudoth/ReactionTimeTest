import pygame
import random
import time
import sys


WHITE = (255, 255, 255)
RED = (203, 40, 60)
GREEN = (83, 219, 108)
BLUE = (55, 134, 207)
WIDTH, HEIGHT = 1500, 500


def GreenScreenResult(screen, result):
  screen.fill(GREEN)
  font = pygame.font.Font(None, 150)
  text = font.render(f"{result} мс", True, WHITE)
  screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
  pygame.display.flip()


def RedScreenMissclick(screen):
  screen.fill(BLUE)
  font = pygame.font.Font(None, 150)
  text = font.render("Too soon!", True, WHITE)
  screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
  pygame.display.flip()


def RedScreen(screen):
  screen.fill(RED)
  font = pygame.font.Font(None, 150)
  text = font.render("Wait for green", True, WHITE)
  screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
  pygame.display.flip()


def GreenScreen(screen):
  screen.fill(GREEN)
  font = pygame.font.Font(None, 150)
  text = font.render("Click!", True, WHITE)
  screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
  pygame.display.flip()


def BlueScreen(screen):
  screen.fill(BLUE)
  font = pygame.font.Font(None, 150)
  text = font.render("Reaction Time Test", True, WHITE)
  screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
  pygame.display.flip()


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
