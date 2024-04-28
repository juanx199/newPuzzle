import pygame
import os

def cargar_imagenes():
    imagenes = []
    for i in range(1,9):
        bob = f"imagen{i}.jpeg"
        image = pygame.image.load(os.path.join("imagenes", bob))
        imagenes.append(image)
    return imagenes
