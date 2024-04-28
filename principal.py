import pygame
import os
import juego
import random


def main():
    pygame.init()
    size = width, height = 300, 300 #Tamaño de la pestañita 
    screen = pygame.display.set_mode(size)
    
    images = juego.cargar_imagenes()
    random.shuffle(images)
    
    for i, image in enumerate(images):
        x = (i % 3) * 100  # Calcula la posición x basada en la columna (3 imágenes por fila)
        y = (i // 3) * 100  # Calcula la posición y basada en la fila
        screen.blit(image, (x, y))
    
    pygame.display.update()
    # Bucle de eventos
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

    
if __name__ == "__main__":
    main()
