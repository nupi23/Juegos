#pgzero
import random
# Ventana de juego hecha de celdas
cells = Actor("border")
cells1 = Actor("floor")
cells2 = Actor("crack")
cells3 = Actor("bones")
caido_en_cuerpo_vivo = Actor("stand",topleft = (cells.height, cells.width))
esqueletos = []
supervivencia = []
brutalidad = []
tacticas = []
mode = "game"
er = 0
d = 0
verdadero_final_verdadero_de_verdad = 0
size_w = 9 # Anchura del campo en celdas
size_h = 10 # Altura del campo en celdas
caido_en_cuerpo_vivo.health = 100
caido_en_cuerpo_vivo.attack = 5
WIDTH = cells.width * size_w
HEIGHT = cells.height * size_h
for i in range(5):
    x = random.randint(1, 7)
    x *= cells.width
    y = random.randint(1, 7)
    y *= cells.height
    esqueleto = Actor("enemy (1)", topleft = (x, y))
    esqueleto.attack = random.randint(5, 10)
    esqueleto.health = random.randint(10, 20)
    esqueleto.stats = random.randint(0, 3)
    esqueletos.append(esqueleto)
    er += 1
TITLE = "THIS IS NOT A ROGUE-LITE" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 2, 1, 3, 1, 1, 0], [0, 1, 1, 1, 1, 2, 1, 1, 0], [0, 1, 3, 2, 1, 1, 3, 1, 0], [0, 1 ,1, 1, 1, 3, 1, 1, 0], [0, 1, 1, 3, 1, 1, 2, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
def drawma():
    for i in range (len(my_map)) : 
        for j in range (len(my_map[0])):
            if my_map[i][j] == 0:
                cells.left = cells.width * j
                cells.top = cells.height * i
                cells.draw ()
            if my_map[i][j] == 1:
                cells1.left = cells1.width * j
                cells1.top = cells1.height * i
                cells1.draw ()
            if my_map[i][j] == 2:
                cells2.left = cells2.width * j
                cells2.top = cells2.height * i
                cells2.draw ()
            if my_map[i][j] == 3:
                cells3.left = cells3.width * j
                cells3.top = cells3.height * i
                cells3.draw ()
def draw():
    screen.fill("white")
    if mode == "game":
        drawma()
        caido_en_cuerpo_vivo.draw()
        screen.draw.text("HP:", center=(20, 475), color = 'black', fontsize = 16)
        screen.draw.text(caido_en_cuerpo_vivo.health, center=(45, 475), color = 'black', fontsize = 16)
        screen.draw.text("AT:", center=(405, 475), color = 'black', fontsize = 16)
        screen.draw.text(caido_en_cuerpo_vivo.attack, center=(425, 475), color = 'black', fontsize = 16)
        screen.draw.text("BSC:", center=(405, 10), color = 'black', fontsize = 16)
        screen.draw.text(d, center=(435, 10), color = 'black', fontsize = 16)
        for i in range(len(esqueletos)):
            esqueletos[i].draw()
        for i in range(len(supervivencia)):
            supervivencia[i].draw()
        for i in range(len(brutalidad)):
            brutalidad[i].draw()
        for i in range(len(tacticas)):
            tacticas[i].draw()
    if mode == "fin":
        screen.fill("white")
        if verdadero_final_verdadero_de_verdad == 1:
            screen.draw.text("GANASTE!", center=(250, 200), color = 'black', fontsize = 50)
        if verdadero_final_verdadero_de_verdad == -1:
            screen.draw.text("PERDISTE!", center=(250, 200), color = 'black', fontsize = 50)
def on_key_down(key):
    global verdadero_final_verdadero_de_verdad
    global er
    global d
    if mode == "game":
        old_x = caido_en_cuerpo_vivo.x
        old_y = caido_en_cuerpo_vivo.y
        if keyboard.left and caido_en_cuerpo_vivo.x - cells.width > cells.width or keyboard.a and caido_en_cuerpo_vivo.x - cells.width > cells.width:
            caido_en_cuerpo_vivo.x -= cells.width
            caido_en_cuerpo_vivo.image = "left"
        if keyboard.right and caido_en_cuerpo_vivo.x + cells.width < WIDTH - cells.width or keyboard.d and caido_en_cuerpo_vivo.x + cells.width < WIDTH - cells.width:
            caido_en_cuerpo_vivo.x += cells.width
            caido_en_cuerpo_vivo.image = "stand"
        if keyboard.up and caido_en_cuerpo_vivo.y - cells.height > cells.height or keyboard.w and caido_en_cuerpo_vivo.y - cells.height > cells.height:
            caido_en_cuerpo_vivo.y -= cells.height
        if keyboard.down and caido_en_cuerpo_vivo.y + cells.height < HEIGHT - 2 * cells.height or keyboard.s and caido_en_cuerpo_vivo.y + cells.height < HEIGHT - 2 * cells.height:
            caido_en_cuerpo_vivo.y += cells.height
        esqueletos_index = caido_en_cuerpo_vivo.collidelist(esqueletos)
        if esqueletos_index != -1:
            caido_en_cuerpo_vivo.x = old_x
            caido_en_cuerpo_vivo.y = old_y
            esqueleto = esqueletos[esqueletos_index]
            caido_en_cuerpo_vivo.health -= esqueleto.attack
            esqueleto.health -= caido_en_cuerpo_vivo.attack
            if esqueleto.health <= 0:
                if esqueleto.stats == 1:
                    vida = Actor("heart")
                    vida.pos = esqueleto.pos
                    supervivencia.append(vida)
                if esqueleto.stats == 2:
                    puno = Actor("sword")
                    puno.pos = esqueleto.pos
                    brutalidad.append(puno)
                if esqueleto.stats == 3:
                    enemy = Actor("mal")
                    enemy.pos = esqueleto.pos
                    tacticas.append(enemy)
                esqueletos.pop(esqueletos_index)
                er -= 1
        for i in range(len(supervivencia)):
            if caido_en_cuerpo_vivo.colliderect(supervivencia[i]):
                caido_en_cuerpo_vivo.health += 5
                supervivencia.pop(i)
                break
        for i in range(len(brutalidad)):
            if caido_en_cuerpo_vivo.colliderect(brutalidad[i]):
                caido_en_cuerpo_vivo.attack += 5
                brutalidad.pop(i)
                break
        for i in range(len(tacticas)):
            if caido_en_cuerpo_vivo.colliderect(tacticas[i]):
                for j in range(len(esqueletos)):
                    esqueletos[j].attack += 5
                    esqueletos[j].health += 5
                    d += 1
                    tacticas.pop(i)
                    break
def update(dt):
    global mode
    global verdadero_final_verdadero_de_verdad
    if er == 0 and caido_en_cuerpo_vivo.health > 0:
        verdadero_final_verdadero_de_verdad = 1
        mode = "fin"
    if caido_en_cuerpo_vivo.health <= 0:
        verdadero_final_verdadero_de_verdad = -1
        mode = "fin"
