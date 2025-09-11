import pygame
import datetime
import time
import sys

# Ancho y alto teórico
ancho_teorico = 900
alto_teorico = 900

# Ancho y alto real
ancho_real = 60
alto_real = 60

# Relation (ratio) de aspecto entre el real y el teórico
delta_x = round(ancho_teorico/ancho_real)
delta_y = round(alto_teorico/alto_real)

# Retardo entre frames (en segundos)
retardo = 0.5

screen = pygame.display.set_mode((ancho_teorico, alto_teorico))
running = True

WHITE = (255, 255, 255)
BLANCO = WHITE
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
GRIS = (80, 80, 80)
ROJO = (255, 10, 10)
VERDE = (10, 255, 10)
AMARILLO = (255, 255, 0)



def dibujar_grilla(screen):

    # Líneas horizontales
    for pos_y in range(0, alto_teorico, delta_y):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (0, pos_y), (ancho_teorico, pos_y))

    # Líneas verticales
    for pos_x in range(0, ancho_teorico, delta_x):
        # print(f'pos_y={pos_y}')
        pygame.draw.aaline(screen, GRIS, (pos_x, 0), (pos_x, alto_teorico))


def pixel(screen, x, y, color):
    x = int(x)
    y = int(y)
    if x < 0 or x > ancho_real or y < 0 or y > alto_real:
        print(f'Punto incorrecto <{x},{y}>')
        return
    #pixel_real = (x*delta_x, (alto_real-y)*delta_y, delta_x, delta_y)
    pixel_real = (x*delta_x, y*delta_y, delta_x, delta_y)
    print(f'Pixel real={pixel_real}')
    # Rectángulo (<origen>,<ancho>,<alto>)
    pygame.draw.rect(screen, color, pixel_real)

if len(sys.argv) != 5:
    print("Usage: python dda01.py <x0> <y0> <x1> <y1>")
    sys.exit(1)

x0=int(sys.argv[1])
y0=int(sys.argv[2])
x1=int(sys.argv[3])
y1=int(sys.argv[4])


# Utilizando la ecuación clasica de la recta.
def dda01(x0,y0,x1,y1,color=AZUL):
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    m = dy*1.0/dx*1.0 # Calculamos la pendiente.

    if m<1: # La linea está "aplastada"

        for x in range(x0, x1+1):
            y = y0 + m*(x - x0)
            pixel(screen, x, round(y), color=color)
            pygame.display.flip()
            time.sleep(retardo)

    else: # La linea está "estirada"

        for y in range(y0, y1+1):
            x = x0 + (y - y0) / m
            pixel(screen, round(x), y, color=color)
            pygame.display.flip()
            time.sleep(retardo)


def dda02(x0,y0,x1,y1,color=VERDE):
    dx = x1 - x0
    dy = y1 - y0
    pasos = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = dx / float(pasos)
    Yinc = dy / float(pasos)
    x = x0
    y = y0
    pixel(screen, round(x), round(y), color)
    for i in range(pasos):
        x += Xinc
        y += Yinc
        pixel(screen, round(x), round(y), color)
        pygame.display.flip()
        time.sleep(retardo)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill(NEGRO)
    dibujar_grilla(screen)

    # Dibujamos la recta "REAL"
    origen_real = (x0*delta_x,y0*delta_y) 
    destino_real = ((x1+1)*delta_x,(y1+1)*delta_y)
    pygame.draw.aaline(screen, AMARILLO, (origen_real), (destino_real))
    dda01(x0,y0,x1,y1,AZUL)
    dda02(x0,y0,x1,y1,VERDE)
    #pygame.draw.aaline(screen, BLANCO, (origen_real), (destino_real))
    #pygame.display.flip()    
    #time.sleep(retardo*3)
    pygame.display.flip()
