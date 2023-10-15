import pygame

# Initialize Pygame
pygame.init()

# Constants and Initialization
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with BFS")

snake_block = 10
snake_speed = 30
font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()
