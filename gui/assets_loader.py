import pygame
import os
from core.vehicle import Vehicle
from utils.constants import *

def load_vehicle_images(state):
    vehicle_images = {}
    folder = "assets/img"

    for vehicle in state.vehicles.values():
        name = vehicle.name
        image_path = os.path.join(folder, f"{name}.png")

        if not os.path.exists(image_path):
            continue
            
        img = pygame.image.load(image_path)

        if vehicle.direction == "H":
            size = (CELL_SIZE * vehicle.length, CELL_SIZE)
        else:
            size = (CELL_SIZE, CELL_SIZE * vehicle.length)
        
        vehicle_images[name] = pygame.transform.scale(img, size)

    return vehicle_images