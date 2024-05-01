import pygame
import random
import sys
import os
import time

class Tablero:
    def __init__(self, size):
        self.size = size # Nuevamente el tamaño del tablero
        self.tablero = self.generar_tablero()
        self.imagenes = self.cargar_imagenes()
        self.tiempo_inicio = time.time() # Guarda el tiempo desde el inicio 
    def generar_tablero(self):
        tablero = []
        nums = list(range(self.size**2))
        random.shuffle(nums)
        for i in range(0, self.size**2, self.size):
            tablero.append(nums[i:i+self.size])
        return tablero
    
    def cargar_imagenes(self): #Carga las imagenes desde la carpeta y les asigna el orden correspondiente
        imagenes = {}
        file_path = os.path.dirname(os.path.abspath(__file__))+ "\imagenes"
        #print(file_path)
        for num in range(1, self.size**2):
            
            #print(os.getcwd()) # Para encontrar la dirección del archivo pq no encuentra la carpeta de imagenes :c
            imagen_path = os.path.join(file_path, f"imagen{num}.jpeg")  # Ruta de la imagen
            
            imagenes[num] =  pygame.image.load(imagen_path)
        return imagenes
    
    def mover_ficha(self, direccion):
        vacio = self.encontrar_vacio() # Aquí  mueve la ficha negra o pss vacía 
        if direccion == "arriba":
            if vacio[0] < self.size - 1: # Esto se complico y me ayudo el buen gepete, pero lo que hace es que cambia la vacía con la ficha del totem
                self.tablero[vacio[0]][vacio[1]], self.tablero[vacio[0] + 1][vacio[1]] = self.tablero[vacio[0] + 1][vacio[1]], self.tablero[vacio[0]][vacio[1]]
        elif direccion == "abajo":
            if vacio[0] > 0:
                self.tablero[vacio[0]][vacio[1]], self.tablero[vacio[0] - 1][vacio[1]] = self.tablero[vacio[0] - 1][vacio[1]], self.tablero[vacio[0]][vacio[1]]
        elif direccion == "izquierda":
            if vacio[1] < self.size - 1:
                self.tablero[vacio[0]][vacio[1]], self.tablero[vacio[0]][vacio[1] + 1] = self.tablero[vacio[0]][vacio[1] + 1], self.tablero[vacio[0]][vacio[1]]
        elif direccion == "derecha":
            if vacio[1] > 0:
                self.tablero[vacio[0]][vacio[1]], self.tablero[vacio[0]][vacio[1] - 1] = self.tablero[vacio[0]][vacio[1] - 1], self.tablero[vacio[0]][vacio[1]]

    def encontrar_vacio(self): # Esto encuentra la posición de la negra
        for i in range(self.size):
            for j in range(self.size):
                if self.tablero[i][j] == 0:
                    return (i, j) # Nos da la posición
                
    def tiempo(self): # Para mostrar el tiempo que ha pasado desde que se inició 
        tiempo_ahora = time.time() # tiempo actual
        tiempo_total = tiempo_ahora - self.tiempo_inicio
        return round(tiempo_total,2)
    
    def victoria(self):
        for fila in range(self.size):
            for columna in range(self.size):
                if fila == self.size -1 and columna == self.size -1:
                    if self.tablero[fila][columna] != fila * self.size + columna + 1:
                        return False # Si están en desorden no
        return True #Si las fichas están en la posición ordenada muestra la victoria      
        print()  