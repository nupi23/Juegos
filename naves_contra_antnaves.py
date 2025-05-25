#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Naves vs antinaves"
FPS = 30
def ap():
    for i in range(5):
        x = random.randint(0, 600)
        antinave = Actor("enemy", (x, -50))
        antinave.speed = random.randint(2, 8)
        antinaves_lista.append(antinave)
    for i in range(5):
        x = random.randint(0, 600)
        protoplaneta = Actor("meteor", (x, -50))
        protoplaneta.speed = random.randint(2, 8)
        protoplanetas.append(protoplaneta)
# Objetos y variables
nave = Actor("ship", (300, 400))
nave1 = Actor("ship1", (200, 300))
nave2 = Actor("ship2", (300, 300))
nave3 = Actor("ship3", (400, 300))
fondo = Actor("space")
antinaves_lista = []
protoplanetas = []
proyectiles = []
navea = "ninguna"
mode = "menu"
count = 0
invasores = 0
muertes = 0
# Elaboración de la lista de enemigos

    
ap() 
planeta1 = Actor("plan1", (40, 400))
planeta2 = Actor("plan2", (300, 300))
planeta3 = Actor("plan3", (400, 200))
# Elaboración
def draw():
    # Modo de juego
    if mode == "menu":
        nave.draw()
        fondo.draw()
        screen.draw.text("ELIGE TU NAVE", center = (300, 200), color = "white", fontsize = 50)
        nave1.draw()
        nave2.draw()
        nave3.draw()
    if mode == "game":
        fondo.draw()
        planeta1.draw()
        planeta2.draw()
        planeta3.draw()
        nave.draw()
        for i in range(len(proyectiles)):
            proyectiles[i].draw()
        # Atraer a los enemigos
        for i in range(len(antinaves_lista)):
            antinaves_lista[i].draw()
        for i in range(len(protoplanetas)):
            protoplanetas[i].draw()
        screen.draw.text(count, center = (10, 10), color = "white", fontsize = 20)
        screen.draw.text(invasores, center = (580, 10), color = "red", fontsize = 20)
    elif mode == "BOOM!!!":
        fondo.draw()
        screen.draw.text("BOOM!!!", center = (300, 200), color = "orange", fontsize = 100)
        screen.draw.text("Dale al espacio", center = (300, 310), color = "white", fontsize = 10)
    elif mode == "invasion":
        fondo.draw()
        screen.draw.text("INVADIERON TU BASE", center = (300, 200), color = "red", fontsize = 50)
        screen.draw.text("Dale al espacio", center = (300, 310), color = "white", fontsize = 10)
    elif mode == "victoria":
        fondo.draw()
        screen.draw.text("GANASTE", center = (300, 200), color = "yellow", fontsize = 50)
        if invasores == 0:
            screen.draw.text("LOGRO: ASESINO", center = (300, 300), color = "yellow", fontsize = 50)
            screen.draw.text("Acabaste el juego matando a todos", center = (300, 350), color = "yellow", fontsize = 26)
        if muertes == 0:
            screen.draw.text("LOGRO: IMPECABLE", center = (300, 100), color = "yellow", fontsize = 50)
            screen.draw.text("Acabaste el juego sin perder", center = (300, 150), color = "yellow", fontsize = 26)
        
            
# Controles
def on_mouse_move(pos):
    nave.pos = pos
# Añadir nuevos enemigos a la lista
def new_antinave():
    x = random.randint(0, 400)
    y = -50
    antinave = Actor("enemy", (x, y))
    antinave.speed = random.randint(2, 8)
    antinaves_lista.append(antinave)
# Movimiento del enemigo
def antinaves():
    global invasores
    for i in range(len(antinaves_lista)):
        if antinaves_lista[i].y < 650:
            antinaves_lista[i].y = antinaves_lista[i].y + antinaves_lista[i].speed
        else:
            antinaves_lista.pop(i)
            invasores += 1
            new_antinave()
def new_proto():
    x = random.randint(0, 400)
    y = -50
    protoplaneta = Actor("meteor", (x, y))
    protoplaneta.speed = random.randint(2, 8)
    protoplanetas.append(protoplaneta)
def proto():
    for i in range(len(protoplanetas)):
        if protoplanetas[i].y < 650:
            protoplanetas[i].y = protoplanetas[i].y + protoplanetas[i].speed
        else:
            protoplanetas.pop(i)
            new_proto()
def proyectil_movimiento():
    for i in range(len(proyectiles)):
        if proyectiles[i].y > -50:
            proyectiles[i].y = proyectiles[i].y - proyectiles[i].speed
        else:
            proyectiles.pop(i)
            break
def colision():
    global mode
    global count
    global muertes
    for i in range(len(antinaves_lista)):
        if nave.colliderect(antinaves_lista[i]):
            mode = "BOOM!!!"
            muertes += 1
    for j in range(len(antinaves_lista)):
        for i in range(len(proyectiles)):
            if antinaves_lista[j].colliderect(proyectiles[i]):
                antinaves_lista.pop(j)
                proyectiles.pop(i)
                count += 1
                new_antinave()
                break      
def update(dt):
    global mode
    global count
    global invasores
    global muertes
    if mode == "game":
        antinaves()
        colision()
        proto()
        proyectil_movimiento()
        if invasores >= 20:
            mode = "invasion"
            muertes += 1
        if count == 100:
            mode = "victoria"
    if mode == "BOOM!!!" and keyboard.space or mode == "invasion" and keyboard.space:
        count = 0
        invasores = 0
        for i in range(len(antinaves_lista)):
            antinaves_lista[i].y = -50
        for i in range(len(protoplanetas)):
            protoplanetas[i].y = -50
        proyectiles = []
        nave.x = 300
        nave.y = 400
        mode = "game"
        
def on_mouse_down(button, pos):
    global mode
    if mode == "menu" and button == mouse.LEFT:
        if nave1.collidepoint(pos):
            nave.image = "ship1"
            mode = "game"
    if mode == "menu" and button == mouse.LEFT:
        if nave2.collidepoint(pos):
            nave.image = "ship2"
            mode = "game"
    if mode == "menu" and button == mouse.LEFT:
        if nave3.collidepoint(pos):
            nave.image = "ship3"
            mode = "game"
    if mode == "game" and button == mouse.LEFT:
        proyectil = Actor("missiles")
        proyectil.pos = nave.pos
        proyectil.speed = 8
        proyectiles.append(proyectil)
