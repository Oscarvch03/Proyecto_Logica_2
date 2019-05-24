print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
print("Listo!")

###############################################################################
# Definicion de las funciones #################################################

def dibujar_tablero(f, letras, n):
    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./3
    tangulos = []

    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle((0, step), step, step, facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 0), step, step], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step], facecolor='cornsilk'))

    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step], facecolor='lightslategrey'))

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005], facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1], facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)


    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]  # A
    direcciones[2] = [0.5, 0.835]    # B
    direcciones[3] = [0.835, 0.835]  # C
    direcciones[4] = [0.165, 0.5]    # D
    direcciones[5] = [0.5, 0.5]      # E
    direcciones[6] = [0.835, 0.5]    # F
    direcciones[7] = [0.165, 0.165]  # G
    direcciones[8] = [0.5, 0.165]    # H
    direcciones[9] = [0.835, 0.165]  # I


    # Asignar direccion a cada casilla del tablero
    aux = {}
    for i in range(1, 10):
        aux["A" + str(i)] = 1
        aux["B" + str(i)] = 2
        aux["C" + str(i)] = 3
        aux["D" + str(i)] = 4
        aux["E" + str(i)] = 5
        aux["F" + str(i)] = 6
        aux["G" + str(i)] = 7
        aux["H" + str(i)] = 8
        aux["I" + str(i)] = 9


    # Asignamos los numeros de la interpretacion al tablero
    for l in f:
        if f[l] == 1:
            # print(l, letras[l])
            # print(direcciones[aux[l]][0], direcciones[aux[l]][1])
            plt.text(direcciones[aux[l]][0], direcciones[aux[l]][1], letras[l],
                     fontsize = 15, horizontalalignment = 'center',
                     verticalalignment = 'center')

    # plt.show()

    # Salvamos la imagen del tablero con la respectiva interpretación
    fig.savefig("tablero_3x3_" + str(n) + ".png")


###############################################################################
# Bloque principal de instrucciones ###########################################

# Creamos las interpretaciones

inter1 = {}
for i in range(1, 10):
    inter1["A" + str(i)] = 0
    inter1["B" + str(i)] = 0
    inter1["C" + str(i)] = 0
    inter1["D" + str(i)] = 0
    inter1["E" + str(i)] = 0
    inter1["F" + str(i)] = 0
    inter1["G" + str(i)] = 0
    inter1["H" + str(i)] = 0
    inter1["I" + str(i)] = 0
# print(len(inter1))

# Letras proposicionales con valor de verdad en 1

inter1["A1"] = 1
inter1["B2"] = 1
inter1["C3"] = 1
inter1["D4"] = 1
inter1["E5"] = 1
inter1["F6"] = 1
inter1["G7"] = 1
inter1["H8"] = 1
inter1["I9"] = 1


###############################################################################

inter2 = {}
for i in range(1, 10):
    inter2["A" + str(i)] = 0
    inter2["B" + str(i)] = 0
    inter2["C" + str(i)] = 0
    inter2["D" + str(i)] = 0
    inter2["E" + str(i)] = 0
    inter2["F" + str(i)] = 0
    inter2["G" + str(i)] = 0
    inter2["H" + str(i)] = 0
    inter2["I" + str(i)] = 0
# print(len(inter2))

# Letras proposicionales con valor de verdad en 1

inter2["A1"] = 1
inter2["B4"] = 1
inter2["C7"] = 1
inter2["D6"] = 1
inter2["E9"] = 1
inter2["F2"] = 1
inter2["G3"] = 1
inter2["H8"] = 1
inter2["I5"] = 1

###########################################################

# Asignamos los posibles numeros del tablero a las letras proposicionales

asig = {}
for k in range(1, 10):
    asig["A" + str(k)] = k
    asig["B" + str(k)] = k
    asig["C" + str(k)] = k
    asig["D" + str(k)] = k
    asig["E" + str(k)] = k
    asig["F" + str(k)] = k
    asig["G" + str(k)] = k
    asig["H" + str(k)] = k
    asig["I" + str(k)] = k


###############################################################################

# Invocamos las funciones con las interpretaciones

dibujar_tablero(inter1, asig, 1)
dibujar_tablero(inter2, asig, 2)
