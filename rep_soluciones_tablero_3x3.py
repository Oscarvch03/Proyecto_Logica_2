import random

print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

###############################################################################

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
# print(len(inter))

del inter1["A1"]
del inter1["B2"]
del inter1["C3"]
del inter1["D4"]
del inter1["E5"]
del inter1["F6"]
del inter1["G7"]
del inter1["H8"]
del inter1["I9"]

# print(len(inter1))

inter1["A1"] = 1
inter1["B2"] = 1
inter1["C3"] = 1
inter1["D4"] = 1
inter1["E5"] = 1
inter1["F6"] = 1
inter1["G7"] = 1
inter1["H8"] = 1
inter1["I9"] = 1

# for j in inter1:
#     print(j, inter1[j])

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

del inter2["A1"]
del inter2["F2"]
del inter2["G3"]
del inter2["B4"]
del inter2["I5"]
del inter2["D6"]
del inter2["C7"]
del inter2["H8"]
del inter2["E9"]

# print(len(inter2))

inter2["A1"] = 1
inter2["B4"] = 1
inter2["C7"] = 1
inter2["D6"] = 1
inter2["E9"] = -1
inter2["F2"] = 1
inter2["G3"] = 1
inter2["H8"] = 1
inter2["I5"] = 1

# print()
# for j in inter2:
#     print(j, inter2[j])

###############################################################################

# Asignamos los numeros del tablero

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

# print()
# for l in asig:
#     print(l, asig[l])

###############################################################################

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
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]

    cont = 1
    for l in f:
        if f[l] == 1:
            plt.text(direcciones[cont][0], direcciones[cont][1], letras[l],
                     fontsize = 15, horizontalalignment = 'center',
                     verticalalignment = 'center')
            cont += 1
        elif f[l] == -1:
            plt.text(direcciones[cont][0], direcciones[cont][1], "N",
                     fontsize = 15, horizontalalignment = 'center',
                     verticalalignment = 'center')
            cont += 1

    # plt.show()
    fig.savefig("tablero_" + str(n) + ".png")

###############################################################################

dibujar_tablero(inter1, asig, 1)
dibujar_tablero(inter2, asig, 2)
