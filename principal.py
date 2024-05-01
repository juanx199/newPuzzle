import pygame
import os


from juego import Juego

if __name__ == "__main__":
    juego = Juego(3)  # Se define el tamaño del tablero
    juego.iniciar()