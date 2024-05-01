import pygame
import sys
from tablero import Tablero

class Juego:
    def __init__(self, size):
        self.tablero = Tablero(size) # Se inicializa el juego con el tamaño del tablero
        self.size = size
        self.cargar_imagenes() # Cargamos las fichas para el tablero 
        
    def cargar_imagenes(self): # Aquí este metodo lo uso para cargar imagenes y ajustarles el tamaño
        
        for imagen in self.tablero.imagenes.values():
            imagen = pygame.transform.scale(imagen,(100,100)) # Aquí se ajustan a 100x100 pixeles :)

    def iniciar(self):
        pygame.init()
        pantalla = pygame.display.set_mode((self.size*100, self.size*100)) # Se crea la ventanita 
        pygame.display.set_caption("Puzzle Deslizante")
        reloj = pygame.time.Clock() # Velocidad para la actualización de la pantalla

        corriendo = True # Se controla el bucle del juego 
        while corriendo:
            for evento in pygame.event.get(): # Eventos
                if evento.type == pygame.QUIT: # Para salir 
                    corriendo = False
                elif evento.type == pygame.KEYDOWN: # Para mover las fichas
                    if evento.key == pygame.K_UP:
                        self.tablero.mover_ficha("arriba")
                    elif evento.key == pygame.K_DOWN:
                        self.tablero.mover_ficha("abajo")
                    elif evento.key == pygame.K_LEFT:
                        self.tablero.mover_ficha("izquierda")
                    elif evento.key == pygame.K_RIGHT:
                        self.tablero.mover_ficha("derecha")
            
            pantalla.fill((0, 0, 0)) # Se limpia pantalla 
            for fila in range(self.size):
                for columna in range(self.size):
                    pygame.draw.rect(pantalla, (0, 0, 0), (columna*100, fila*100, 100, 100), 1) #Borde del triqui
                    if self.tablero.tablero[fila][columna] != 0: # Detecta si el cuadrito no esta ocupado
                        imagen = self.tablero.imagenes[self.tablero.tablero[fila][columna]]
                        pantalla.blit(imagen, (columna*100, fila*100)) # Se dibuja el totem rcorrespondiente 
                        # texto = pygame.font.SysFont(None, 48).render(str(self.tablero.tablero[fila][columna]), True, (0, 0, 0))
                        # texto_rect = texto.get_rect(center=(columna*100+50, fila*100+50))
                        # pantalla.blit(texto, texto_rect)
            if self.tablero.victoria():
                mensaje_victoria = pygame.font.SysFont(None, 48).render("¡Has ganado!", True, (255, 255, 255))
                pantalla.blit(mensaje_victoria, (50, 50))  # Muestra el mensaje de victoria en la posición (50, 50)
                pygame.display.flip()  # Muestra el mensaje de victoria en la pantalla antes de salir del bucle
                pygame.time.wait(2000)  # Espera 2 segundos antes de salir del juego
                corriendo = False
            
            tiempo_letrero = pygame.font.SysFont(None,24).render("Llevas " + str(self.tablero.tiempo()), True,(225,225,225))
            pantalla.blit(tiempo_letrero,(10,10))
            
            if self.tablero.victoria():
                mensaje_victoria = pygame.font.SysFont(Nonee, 48).render("GANASTE",True, (255, 255, 255))
                pantalla.blit(mensaje_victoria, (60,60))
                
            pygame.display.flip() # Actualiza 
            reloj.tick(10)

        pygame.quit()
        sys.exit()