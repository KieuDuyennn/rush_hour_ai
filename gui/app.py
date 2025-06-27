import pygame, time, tracemalloc
import os
from utils.constants import *
from utils.utils import *
from gui.assets_loader import load_vehicle_images
from gui.draw import *
from core.problem import Problem

def App():
    pygame.init()
    font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    stats = {"Search Time": "-", "Memory Usage": "-", "Expanded node": "-"}
    status_text = "Idle"
    
    solution = []
    solving = False
    step = 0

    map_files = get_map_files()
    selected_map = map_files[0]
    selected_algo = "BFS"

    problem = Problem(f"assets/maps/{selected_map}")
    state = problem.initial_state
    vehicle_images = load_vehicle_images(state)
    
    solve_btn = pygame.Rect(550, 350, 80, 30)
    reset_btn = pygame.Rect(650, 350, 80, 30)
    algo_box = pygame.Rect(550, 300, 180, 30)
    map_box = pygame.Rect(550, 260, 180, 30)

    running = True;
    while running:
        #ccc
        screen.fill(BACKGROUND_COLOR)
        draw_board(screen, state if not solution else solution[step], vehicle_images, font)
        draw_dropdown(screen, "Map", selected_map, map_box, font)
        draw_dropdown(screen, "Algo", selected_algo, algo_box, font)
        draw_info_panel(screen, stats, status_text, font)

        pygame.draw.rect(screen, (50, 200, 50), solve_btn)
        pygame.draw.rect(screen, (200, 50, 50), reset_btn)
        screen.blit(font.render("Solve", True, (255,255,255)), (solve_btn.x+10, solve_btn.y+5))
        screen.blit(font.render("Reset", True, (255,255,255)), (reset_btn.x+10, reset_btn.y+5))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    