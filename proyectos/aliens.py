import pygame
import sys

# creamos la ventana
ventana = pygame.display.set_mode((800,600))

# Mostramos al programa que no se cierre hasta que le des a cerrar
game_over = False
# mientras game_over sea falso repite esta accion
while  game_over==False:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #si el tipo de elemto es igual a darle a la cruz entonces sys sale del programa
            sys.exit()