import pygame
from config import WHITE, GREEN, BLUE, RED, HEIGHT, WIDTH


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