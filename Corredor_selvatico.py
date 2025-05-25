#pgzero
import random
WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Corredor de Alienígenas" # Título para la ventana de juego
FPS = 30 #  Número de fotogramas por segundo


# Objetos
alien = Actor('stand', (50, 240))
background = Actor("Background5")
box = Actor('piranha', (850, 265))
bee = Actor('fly', (850, 175))
go = Actor("GO")
game_over = 0
count = 0
aparicion = random.randint(1,2)
altura = random.randint(120,180)
velocidad = 5
def draw():
    background.draw()
    alien.draw()
    box.draw()
    bee.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    if game_over == 1:
        go.draw()
        screen.draw.text('Presiona Enter', pos=(170, 150), color= "white", fontsize = 36)
def bees():
    global aparicion
    global count
    global velocidad
    global altura
    bee.y = altura
    if bee.x > -20:
        bee.x = bee.x - velocidad
    else:
        bee.x = WIDTH + 20
        count = count + 1
        aparicion = random.randint(1,2)
        velocidad += 1
        altura = random.randint(120,180)
def boxes():
    global count
    global aparicion
    global velocidad
    if box.x > -20:
        box.x = box.x - velocidad
    else:
        box.x = WIDTH + 20
        count = count + 1
        aparicion = random.randint(1,2)
        velocidad += 1
def update(dt):
    global game_over
    global count
    global velocidad
    
    if aparicion == 1:
        bees()
        
    # Movimiento de la caja
    if aparicion == 2:
        boxes()
        
    # Controles
    if (keyboard.left or keyboard.a) and alien.x >= 20:
        alien.x = alien.x - 5
        alien.image = 'left'
        
    elif (keyboard.right or keyboard.d) and alien.x <= 580:
        alien.x = alien.x + 5
        alien.image = 'right'
    elif keyboard.down or keyboard.s:
            alien.image = 'duck'
            alien.y = 250
    else:
        alien.image = 'stand'
        if alien.y > 250:
            alien.y = 240
    
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        alien.pos = (50, 240)
        box.pos = (850, 265)
        bee.pos = (850, 175)
        velocidad = 5
        
    
    # Colisión
    if alien.colliderect(box) or alien.colliderect(bee):
        game_over = 1
        
def on_key_down(key):
    # Salto
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)
