#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Naves vs Antinaves 2: La Venganza"
FPS = 30

# Objetos y variables
nave = Actor("ship", (300, 400))
nave1 = Actor("ship1", (100, 300))
nave2 = Actor("ship2", (200, 300))
nave3 = Actor("ship3", (300, 300))
nave4 = Actor("ship4", (450, 300))
fondo = Actor("space")
normal = Actor("boton", (300, 100))
exploracion = Actor("boton", (300, 150))
invasionm = Actor("boton", (300, 200))
creditos = Actor("boton", (300, 400))
gigantinave = Actor("gigaantinave", (300, 20))
barra = Actor("barra1", (40, 10))
cruz = Actor("cross", (580, 10))
antinaves_lista = []
protoplanetas = []
proyectiles = []
gigaantinaves = []
antiproyectiles = []
escudo = 4
navea = "ninguna"
mode = "menu"
count = 0
invasores = 0
muertes = 0
megameteorito = Actor("mega-meteorito",(300, -300))
cuenta = 0
# Elaboración de la lista de enemigos

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
ap() 
planeta1 = Actor("plan1", (40, 400))
planeta2 = Actor("plan2", (300, 300))
planeta3 = Actor("plan3", (400, 200))
# Elaboración
def draw():
    # Modo de juego
    if mode == "menu":
        fondo.draw()
        normal.draw()
        exploracion.draw()
        invasionm.draw()
        creditos.draw()
        screen.draw.text("MODO NORMAL", center = (300, 100), color = "white", fontsize = 20)
        screen.draw.text("MODO EXPLORACIÓN", center = (300, 150), color = "white", fontsize = 15)
        screen.draw.text("MODO INVASIÓN", center = (300, 200), color = "white", fontsize = 15)
        screen.draw.text("CREDITOS", center = (300, 400), color = "white", fontsize = 20)
        screen.draw.text("Naves vs Antinaves 2: La ", center = (200, 300), color = "white", fontsize = 30)
        screen.draw.text("Venganza", center = (435, 300), color = "red", fontsize = 30)
    if mode == "creditos":
        fondo.draw()
        screen.draw.text("Juego hecho por:", center = (300, 100), color = "white", fontsize = 20)
        screen.draw.text("Unai Picornell Pozo/Ñupi", center = (300, 120), color = "white", fontsize = 20)
        screen.draw.text("También podeis jugar a Naves vs Antinaves, clicker del boscaje y", center = (300, 140), color = "white", fontsize = 20)
        screen.draw.text("a THIS IS NOT A ROGUE LITE.", center = (300, 160), color = "white", fontsize = 20)
        screen.draw.text("DISTRIBUIDORA: Empresa Pipozo", center = (300, 320), color = "white", fontsize = 20)
        screen.draw.text("GRACIAS POR JUGAR", center = (300, 400), color = "white", fontsize = 20)
        cruz.draw()
    if mode == "seleccionN":
        nave.draw()
        fondo.draw()
        screen.draw.text("ELIGE TU NAVE:", center = (300, 200), color = "white", fontsize = 50)
        nave1.draw()
        nave2.draw()
        nave3.draw()
        nave4.draw()
    if mode == "seleccionE":
        nave.draw()
        fondo.draw()
        screen.draw.text("ELIGE TU NAVE:", center = (300, 200), color = "white", fontsize = 50)
        nave1.draw()
        nave2.draw()
        nave3.draw()
        nave4.draw()
    if mode == "seleccionI":
        nave.draw()
        fondo.draw()
        screen.draw.text("ELIGE TU NAVE:", center = (300, 200), color = "white", fontsize = 50)
        nave1.draw()
        nave2.draw()
        nave3.draw()
        nave4.draw()
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
    if mode == "exploracion":
        fondo.draw()
        planeta1.draw()
        planeta2.draw()
        planeta3.draw()
        nave.draw()
        for i in range(len(proyectiles)):
            proyectiles[i].draw()
        # Atraer a los enemigos
        for i in range(len(protoplanetas)):
            protoplanetas[i].draw()
        megameteorito.draw()
        screen.draw.text(count, center = (10, 10), color = "white", fontsize = 20)
    if mode == "invasion":
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
        gigantinave.draw()
        barra.draw()
        screen.draw.text(count, center = (10, 10), color = "white", fontsize = 20)
        screen.draw.text(invasores, center = (580, 10), color = "red", fontsize = 20)
    if mode == "BOOM!!!":
        fondo.draw()
        screen.draw.text("BOOM!!!", center = (300, 200), color = "orange", fontsize = 100)
        screen.draw.text("Dale al espacio", center = (300, 310), color = "white", fontsize = 10)
    elif mode == "destruccion":
        fondo.draw()
        screen.draw.text("DESTRUYERON EL PLANETA", center = (300, 200), color = "orange", fontsize = 20)
        screen.draw.text("Dale al espacio", center = (300, 310), color = "white", fontsize = 10)
    elif mode == "invasionp":
        fondo.draw()
        screen.draw.text("INVADIERON TU BASE", center = (300, 200), color = "red", fontsize = 50)
        screen.draw.text("Dale al espacio", center = (300, 310), color = "white", fontsize = 10)
    elif mode == "victoria":
        fondo.draw()
        screen.draw.text("GANASTE", center = (300, 200), color = "yellow", fontsize = 50)
        if mode == "invasion":
            if invasores == 0:
                screen.draw.text("LOGRO: ASESINO", center = (300, 300), color = "yellow", fontsize = 50)
                screen.draw.text("Acabaste el juego matando a todos", center = (300, 350), color = "yellow", fontsize = 26)
        
        
            
# Controles
def on_mouse_move(pos):
    nave.pos = pos
# Añadir nuevos enemigos a la lista
def new_antinave():
    x = random.randint(0, 600)
    y = -50
    antinave = Actor("enemy", (x, y))
    antinave.speed = random.randint(2, 8)
    antinaves_lista.append(antinave)
# Movimiento del enemigo
def antinaves():
    global invasores
    if mode == "game" or mode == "invasion":
        for i in range(len(antinaves_lista)):
            if antinaves_lista[i].y < 650:
                antinaves_lista[i].y = antinaves_lista[i].y + antinaves_lista[i].speed
            else:
                antinaves_lista.pop(i)
                if mode == "invasion":
                    invasores += 1
                new_antinave()
def antiproyectiles_movimiento():
    global invasores
    if mode == "invasion":
        for i in range(len(antiproyectiles)):
            if antiproyectiles[i].y < 650:
                antiproyectiles[i].y += antinaves_lista[i].speed
            else:
                antiproyectiles.pop(i)
                
def new_proto():
    x = random.randint(0, 600)
    y = -50
    protoplaneta = Actor("meteor", (x, y))
    protoplaneta.speed = random.randint(2, 8)
    protoplanetas.append(protoplaneta)
def proto():
    for i in range(len(protoplanetas)):
        if mode == "game" or mode == "exploracion":
            if protoplanetas[i].y < 650:
                protoplanetas[i].y = protoplanetas[i].y + protoplanetas[i].speed
                protoplanetas[i].angle += protoplanetas[i].speed
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
    global cuenta
    global escudo
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
    if mode == "exploracion":
        for i in range(len(protoplanetas)):
            for j in range(len(proyectiles)):
                if protoplanetas[i].colliderect(proyectiles[j]):
                    protoplanetas.pop(i)
                    proyectiles.pop(j)
                    cuenta += 1
                    new_proto()
                    break
        for i in range(len(protoplanetas)):
            if nave.colliderect(protoplanetas[i]):
                mode = "BOOM!!!"
                muertes += 1
        for i in range(len(proyectiles)):
            if proyectiles[i].colliderect(megameteorito):
                mode = "victoria"
    if mode == "invasion":
        for i in range(len(proyectiles)):
            if gigantinave.colliderect(proyectiles[i]):
                escudo -= 1
                proyectiles.pop(i)
                break
                
def update(dt):
    global mode
    global count
    global invasores
    global muertes
    global cuenta
    global escudo
    if mode == "game":
        antinaves()
        colision()
        proto()
        proyectil_movimiento()
        if invasores >= 20:
            mode = "invasionp"
            muertes += 1
        if count == 100:
            mode = "victoria"
    if mode == "exploracion":
        antinaves()
        colision()
        proto()
        proyectil_movimiento()
    if mode == "invasion":
        antinaves()
        colision()
        proto()
        proyectil_movimiento()
        antiproyectiles_movimiento()
        disparo = 0
        if disparo == 5:
            x = random.randint(0, 600)
            antiproyectil = Actor("antimisil", (x, 0))
            antiproyectiles.append(antiproyectil)
            disparo = 0
        else:
            disparo += 1
        if escudo == 4:
            barra.image = ("barra1")
        if escudo == 3:
            barra.image = ("barra2")
        if escudo == 2:
            barra.image = ("barra3")
        if escudo == 1:
            barra.image = ("barra4")
        if escudo <= 0:
            mode = "victoria"
    if mode == "BOOM!!!" and keyboard.space or mode == "invasionp" and keyboard.space or mode == "destruccion" and keyboard.space or mode == "victoria" and keyboard.space:
        count = 0
        invasores = 0
        escudo = 4
        for i in range(len(antinaves_lista)):
            antinaves_lista[i].y = -50
        for i in range(len(protoplanetas)):
            protoplanetas[i].y = -50
        proyectiles = []
        nave.x = 300
        nave.y = 400
        cuenta = 0
        mode = "menu"
    if mode == "exploracion" and cuenta >=20:
        megameteorito.y += 1
        if megameteorito.y >= 650:
            mode = "destruccion"
def on_mouse_down(button, pos):
    global mode
    if mode == "menu" and button == mouse.LEFT:
        if normal.collidepoint(pos):
            mode = "seleccionN"
        if exploracion.collidepoint(pos):
            mode = "seleccionE"
        if invasionm.collidepoint(pos):
            mode = "seleccionI"
        if creditos.collidepoint(pos):
            mode = "creditos"
    if mode == "creditos" and button == mouse.LEFT:
        if cruz.collidepoint(pos):
            mode = "menu"
    if mode == "seleccionN" and button == mouse.LEFT:
        if nave1.collidepoint(pos):
            nave.image = "ship1"
            mode = "game"
        if nave2.collidepoint(pos):
            nave.image = "ship2"
            mode = "game"
        if nave3.collidepoint(pos):
            nave.image = "ship3"
            mode = "game"
        if nave4.collidepoint(pos):
            nave.image = "ship4"
            mode = "game"
    if mode == "seleccionE" and button == mouse.LEFT:
        if nave1.collidepoint(pos):
            nave.image = "ship1"
            mode = "exploracion"
        if nave2.collidepoint(pos):
            nave.image = "ship2"
            mode = "exploracion"
        if nave3.collidepoint(pos):
            nave.image = "ship3"
            mode = "exploracion"
        if nave4.collidepoint(pos):
            nave.image = "ship4"
            mode = "exploracion"
    if mode == "seleccionI" and button == mouse.LEFT:
        if nave1.collidepoint(pos):
            nave.image = "ship1"
            mode = "invasion"
        if nave2.collidepoint(pos):
            nave.image = "ship2"
            mode = "invasion"
        if nave3.collidepoint(pos):
            nave.image = "ship3"
            mode = "invasion"
        if nave4.collidepoint(pos):
            nave.image = "ship4"
            mode = "invasion"
    if mode == "game" and button == mouse.LEFT or mode == "exploracion" and button == mouse.LEFT or mode == "invasion" and button == mouse.LEFT:
        proyectil = Actor("missiles")
        proyectil.pos = nave.pos
        proyectil.speed = 8
        proyectiles.append(proyectil)
