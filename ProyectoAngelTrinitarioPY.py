import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Memoria")
fuente = pygame.font.Font(None, 74)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

TAMANO_CARTA = 100
MARGEN = 20

# Crear posiciones de las cartas
def crear_posiciones_cartas():
    posiciones = []
    for i in range(4):
        for j in range(4):
            x = MARGEN + j * (TAMANO_CARTA + MARGEN)
            y = MARGEN + i * (TAMANO_CARTA + MARGEN)
            posiciones.append((x, y))
    return posiciones

# Generar pares
def generar_pares():
    simbolos = list(range(8)) * 2
    random.shuffle(simbolos)
    return simbolos

# Clase Carta
class Carta:
    def __init__(self, simbolo, posicion):
        self.simbolo = simbolo
        self.posicion = posicion
        self.rectangulo = pygame.Rect(posicion[0], posicion[1], TAMANO_CARTA, TAMANO_CARTA)
        self.revelada = False
        self.encontrada = False

    def dibujar(self, pantalla):
        if self.revelada or self.encontrada:
            pygame.draw.rect(pantalla, BLANCO, self.rectangulo)
            texto = fuente.render(str(self.simbolo), True, NEGRO)
            pantalla.blit(texto, (self.posicion[0] + 35, self.posicion[1] + 25))
        else:
            pygame.draw.rect(pantalla, VERDE, self.rectangulo)

# Pantalla inicial
def pantalla_inicial():
    pantalla.fill(NEGRO)
    texto = fuente.render("¿Quieres jugar?", True, BLANCO)
    pantalla.blit(texto, (ANCHO // 2 - 200, ALTO // 2 - 100))

    boton_si = pygame.Rect(150, 400, 100, 50)
    boton_no = pygame.Rect(350, 400, 100, 50)
    pygame.draw.rect(pantalla, VERDE, boton_si)
    pygame.draw.rect(pantalla, ROJO, boton_no)

    texto_si = fuente.render("Sí", True, NEGRO)
    texto_no = fuente.render("No", True, NEGRO)
    pantalla.blit(texto_si, (175, 405))
    pantalla.blit(texto_no, (375, 405))

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_si.collidepoint(evento.pos):
                    return True
                elif boton_no.collidepoint(evento.pos):
                    pygame.quit()
                    exit()

# Juego principal
def juego():
    posiciones = crear_posiciones_cartas()
    pares = generar_pares()
    cartas = [Carta(pares[i], posiciones[i]) for i in range(16)]

    primera_carta = None
    segunda_carta = None
    coincidencias = 0
    intentos = 0
    juego_activo = True
    reloj = pygame.time.Clock()

    # Mostrar todas las cartas al inicio
    pantalla.fill(NEGRO)
    for carta in cartas:
        carta.revelada = True
        carta.dibujar(pantalla)
    pantalla.blit(fuente.render("Memoriza los pares", True, BLANCO), (10, 500))
    pygame.display.flip()

    time.sleep(5)  # Espera 5 segundos para memorizar

    for carta in cartas:
        carta.revelada = False

    # Bucle principal del juego
    while juego_activo:
        pantalla.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_activo = False
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if primera_carta is None or (primera_carta and segunda_carta is None):
                    for carta in cartas:
                        if carta.rectangulo.collidepoint(evento.pos) and not carta.revelada and not carta.encontrada:
                            carta.revelada = True
                            if primera_carta is None:
                                primera_carta = carta
                            elif segunda_carta is None:
                                segunda_carta = carta
                                intentos += 1

        if primera_carta and segunda_carta:
            pygame.time.wait(500)
            if primera_carta.simbolo == segunda_carta.simbolo:
                primera_carta.encontrada = True
                segunda_carta.encontrada = True
                coincidencias += 1
            else:
                primera_carta.revelada = False
                segunda_carta.revelada = False
            primera_carta = None
            segunda_carta = None

        for carta in cartas:
            carta.dibujar(pantalla)

        texto = pygame.font.Font(None, 36).render(f"Coincidencias: {coincidencias}  Intentos: {intentos}", True, BLANCO)
        pantalla.blit(texto, (10, 500))

        if coincidencias == 8:
            texto_ganar = fuente.render("¡Ganaste!", True, ROJO)
            pantalla.blit(texto_ganar, (ANCHO // 2 - 100, ALTO // 2 - 50))
            pygame.display.flip()
            time.sleep(3)
            return  # Volver a la pantalla inicial

        pygame.display.flip()
        reloj.tick(30)

# Bucle principal del programa
while True:
    if pantalla_inicial():
        juego()
