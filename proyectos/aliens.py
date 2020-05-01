import pygame
import sys
import random

#Variables ventana
width_window = 800
height_window= 600
#variables jugador
color_green = (0,255,0)
color_black = (0,0,0)
color_red = (255,0,0)
player_size = 50
player_pos = [width_window/2,height_window - player_size * 2.5]
#variables enemigo(s)
enemy_size = 50
enemy_pos = [random.randint(0, width_window - enemy_size * 0.5),0]



# creamos la ventana
window = pygame.display.set_mode((width_window, height_window))

# Mostramos al programa que no se cierre hasta que le des a la cruz
game_over = False
# mientras game_over sea falso repite esta accion
while  game_over == False:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #si el tipo de elemto es igual a darle a la cruz entonces sys sale del programa
            sys.exit() 
        # Si detecta un evento que es igual a una tecla la variable x es igual a la posicion del player, si esa tecla es izquierda muevelo a la izquierda
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            if event.key == pygame.K_RIGHT:
                x += player_size
            player_pos[0] = x
    #Cada vez que esto ocurra vuelve a poner la pantalla en negro
    window.fill(color_black)

    #hacemos que el enemigo baje
    if enemy_pos[1] >= 0 and enemy_pos[1] < height_window:
        enemy_pos[1] += 0.5
    else:
        enemy_pos = [random.randint(0, width_window - enemy_size * 0.5),0]

    def colision(player_pos, enemy_pos):
        px = player_pos[0]
        py = player_pos[1]
        ex = enemy_pos[0]
        ey = enemy_pos[1]
        if (ex >= px and ex <= (px + player_size) or px >= ex and px <= (ex + enemy_size)):
            if (ey >= py and ey <= (py + player_size) or py >= ey and py <= (ey + enemy_size)):
                return True
        else:
            return False

    #colisiones
    if colision(player_pos, enemy_pos):
        enemy_pos = [random.randint(0, width_window - enemy_size * 0.5),0]
   
        


    #crear enemigo
    pygame.draw.rect(window,color_red,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
    #crear jugador
    pygame.draw.rect(window,color_green,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()
    
