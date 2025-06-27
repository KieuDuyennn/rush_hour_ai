import pygame
from utils.constants import *

def draw_board(screen, state, vehicle_images, font):
    for r in range(6):
        for c in range(6):
            rect = pygame.Rect(BOARD_ORIGIN[0]+c*CELL_SIZE, BOARD_ORIGIN[1]+r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (CELL_COLOR), rect)
            pygame.draw.rect(screen, (BLACK_COLOR), rect, 1)

    for v in state.vehicles.values():
        for r, c in v.cells():
            if v.row == r and v.col == c:
               screen.blit(vehicle_images[v.name], (BOARD_ORIGIN[0]+c*CELL_SIZE, BOARD_ORIGIN[1]+r*CELL_SIZE))


def draw_dropdown(screen, label, value, rect, font):
    pygame.draw.rect(screen, DROPDOWN_COLOR, rect)
    screen.blit(font.render(f"{label}: {value}", True, (0, 0, 0)), (rect.x+5, rect.y+5))

def draw_info_panel(screen, stats, status, font):
    x, y = 550, 400
    for label, val in stats.items():
        line = font.render(f"{label}: {val}", True, (0, 0, 0))
        screen.blit(line, (x, y))
        y += 25
    color = (50,200,50) if status == "Success" else (200,50,50)
    screen.blit(font.render(f"Status: {status}", True, color), (x, y+10))