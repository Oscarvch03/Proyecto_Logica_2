print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
print("Listo!")

def dibujar_tablero(f, letras, n):
    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./4
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

    ###############################################################################
    tangulos.append(patches.Rectangle(*[(0, 3 * step), step, step], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3 * step, step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step, 0), step, step], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 3 * step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step, 3 * step), step, step], facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(3 * step, 2 * step), step, step], facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, 3 * step), step, step], facecolor='cornsilk'))
    ################################################################################
    tangulos.append(patches.Rectangle(*[(4 * step, 4 * step), step, step], facecolor='green'))
    tangulos.append(patches.Rectangle(*[(3 * step, 4 * step), step, step], facecolor='pink'))
    tangulos.append(patches.Rectangle(*[(4 * step, 3 * step), step, step], facecolor='pink'))
    tangulos.append(patches.Rectangle(*[(2 * step, 4 * step), step, step], facecolor='red'))
    tangulos.append(patches.Rectangle(*[(4 * step, 2 * step), step, step], facecolor='red'))
    tangulos.append(patches.Rectangle(*[(1 * step, 4 * step), step, step], facecolor='blue'))
    tangulos.append(patches.Rectangle(*[(4 * step, 1 * step), step, step], facecolor='blue'))
    tangulos.append(patches.Rectangle(*[(0 * step, 4 * step), step, step], facecolor='purple'))
    tangulos.append(patches.Rectangle(*[(4 * step, 0 * step), step, step], facecolor='purple'))

    #################################################################################

    # Creo las líneas del tablero
    for j in range(4):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005], facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1], facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)


    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.125, 0.875]  # A
    direcciones[2] = [0.375, 0.875]  # B
    direcciones[3] = [0.625, 0.875]  # C
    direcciones[4] = [0.875, 0.875]  # D
    direcciones[5] = [0.125, 0.625]  # E
    direcciones[6] = [0.375, 0.625]  # F
    direcciones[7] = [0.625, 0.625]  # G
    direcciones[8] = [0.875, 0.625]  # H
    direcciones[9] = [0.125, 0.375]  # I
    direcciones[10] = [0.375, 0.375] # J
    direcciones[11] = [0.625, 0.375] # K
    direcciones[12] = [0.875, 0.375] # L
    direcciones[13] = [0.125, 0.125] # M
    direcciones[14] = [0.375, 0.125] # N
    direcciones[15] = [0.625, 0.125] # P
    direcciones[16] = [0.875, 0.125] # Q


    # Asignar direccion a cada casilla del tablero
    aux = {}
    for i in range(1, 10):
        aux["A0" + str(i)] = 1
        aux["B0" + str(i)] = 2
        aux["C0" + str(i)] = 3
        aux["D0" + str(i)] = 4
        aux["E0" + str(i)] = 5
        aux["F0" + str(i)] = 6
        aux["G0" + str(i)] = 7
        aux["H0" + str(i)] = 8
        aux["I0" + str(i)] = 9
        aux["J0" + str(i)] = 10
        aux["K0" + str(i)] = 11
        aux["L0" + str(i)] = 12
        aux["M0" + str(i)] = 13
        aux["N0" + str(i)] = 14
        aux["P0" + str(i)] = 15
        aux["Q0" + str(i)] = 16

    for i in range(10, 17):
        aux["A" + str(i)] = 1
        aux["B" + str(i)] = 2
        aux["C" + str(i)] = 3
        aux["D" + str(i)] = 4
        aux["E" + str(i)] = 5
        aux["F" + str(i)] = 6
        aux["G" + str(i)] = 7
        aux["H" + str(i)] = 8
        aux["I" + str(i)] = 9
        aux["J" + str(i)] = 10
        aux["K" + str(i)] = 11
        aux["L" + str(i)] = 12
        aux["M" + str(i)] = 13
        aux["N" + str(i)] = 14
        aux["P" + str(i)] = 15
        aux["Q" + str(i)] = 16


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
    fig.savefig("tablero_4x4_" + str(n) + ".png")

###############################################################################
# Bloque principal de instrucciones ###########################################

# Creamos las interpretaciones

inter1 = {}
for i in range(1, 10):
    inter1["A0" + str(i)] = 0
    inter1["B0" + str(i)] = 0
    inter1["C0" + str(i)] = 0
    inter1["D0" + str(i)] = 0
    inter1["E0" + str(i)] = 0
    inter1["F0" + str(i)] = 0
    inter1["G0" + str(i)] = 0
    inter1["H0" + str(i)] = 0
    inter1["I0" + str(i)] = 0
    inter1["J0" + str(i)] = 0
    inter1["K0" + str(i)] = 0
    inter1["M0" + str(i)] = 0
    inter1["L0" + str(i)] = 0
    inter1["N0" + str(i)] = 0
    inter1["P0" + str(i)] = 0
    inter1["Q0" + str(i)] = 0

for i in range(10, 17):
    inter1["A" + str(i)] = 0
    inter1["B" + str(i)] = 0
    inter1["C" + str(i)] = 0
    inter1["D" + str(i)] = 0
    inter1["E" + str(i)] = 0
    inter1["F" + str(i)] = 0
    inter1["G" + str(i)] = 0
    inter1["H" + str(i)] = 0
    inter1["I" + str(i)] = 0
    inter1["J" + str(i)] = 0
    inter1["K" + str(i)] = 0
    inter1["M" + str(i)] = 0
    inter1["L" + str(i)] = 0
    inter1["N" + str(i)] = 0
    inter1["P" + str(i)] = 0
    inter1["Q" + str(i)] = 0

# print(len(inter1))

# Letras proposicionales con valor de verdad en 1

inter1["A01"] = 1
inter1["B02"] = 1
inter1["C03"] = 1
inter1["D04"] = 1
inter1["E05"] = 1
inter1["F06"] = 1
inter1["G07"] = 1
inter1["H08"] = 1
inter1["I09"] = 1
inter1["J10"] = 1
inter1["K11"] = 1
inter1["L12"] = 1
inter1["M13"] = 1
inter1["N14"] = 1
inter1["P15"] = 1
inter1["Q16"] = 1


###############################################################################

inter2 = {}
for i in range(1, 10):
    inter2["A0" + str(i)] = 0
    inter2["B0" + str(i)] = 0
    inter2["C0" + str(i)] = 0
    inter2["D0" + str(i)] = 0
    inter2["E0" + str(i)] = 0
    inter2["F0" + str(i)] = 0
    inter2["G0" + str(i)] = 0
    inter2["H0" + str(i)] = 0
    inter2["I0" + str(i)] = 0
    inter2["J0" + str(i)] = 0
    inter2["K0" + str(i)] = 0
    inter2["M0" + str(i)] = 0
    inter2["L0" + str(i)] = 0
    inter2["N0" + str(i)] = 0
    inter2["P0" + str(i)] = 0
    inter2["Q0" + str(i)] = 0

for i in range(10, 17):
    inter2["A" + str(i)] = 0
    inter2["B" + str(i)] = 0
    inter2["C" + str(i)] = 0
    inter2["D" + str(i)] = 0
    inter2["E" + str(i)] = 0
    inter2["F" + str(i)] = 0
    inter2["G" + str(i)] = 0
    inter2["H" + str(i)] = 0
    inter2["I" + str(i)] = 0
    inter2["J" + str(i)] = 0
    inter2["K" + str(i)] = 0
    inter2["M" + str(i)] = 0
    inter2["L" + str(i)] = 0
    inter2["N" + str(i)] = 0
    inter2["P" + str(i)] = 0
    inter2["Q" + str(i)] = 0

# print(len(inter2))

# Letras proposicionales con valor de verdad en 1

inter2["A01"] = 1
inter2["B08"] = 1
inter2["C13"] = 1
inter2["D10"] = 1
inter2["E14"] = 1
inter2["F11"] = 1
inter2["G04"] = 1
inter2["H07"] = 1
inter2["I05"] = 1
inter2["J02"] = 1
inter2["K09"] = 1
inter2["L12"] = 1
inter2["M16"] = 1
inter2["N15"] = 1
inter2["P06"] = 1
inter2["Q03"] = 1


###############################################################################

# Asignamos los posibles numeros del tablero a las letras proposicionales

asig = {}
for i in range(1, 10):
    asig["A0" + str(i)] = i
    asig["B0" + str(i)] = i
    asig["C0" + str(i)] = i
    asig["D0" + str(i)] = i
    asig["E0" + str(i)] = i
    asig["F0" + str(i)] = i
    asig["G0" + str(i)] = i
    asig["H0" + str(i)] = i
    asig["I0" + str(i)] = i
    asig["J0" + str(i)] = i
    asig["K0" + str(i)] = i
    asig["M0" + str(i)] = i
    asig["L0" + str(i)] = i
    asig["N0" + str(i)] = i
    asig["P0" + str(i)] = i
    asig["Q0" + str(i)] = i

for i in range(10, 17):
    asig["A" + str(i)] = i
    asig["B" + str(i)] = i
    asig["C" + str(i)] = i
    asig["D" + str(i)] = i
    asig["E" + str(i)] = i
    asig["F" + str(i)] = i
    asig["G" + str(i)] = i
    asig["H" + str(i)] = i
    asig["I" + str(i)] = i
    asig["J" + str(i)] = i
    asig["K" + str(i)] = i
    asig["M" + str(i)] = i
    asig["L" + str(i)] = i
    asig["N" + str(i)] = i
    asig["P" + str(i)] = i
    asig["Q" + str(i)] = i


###############################################################################

# Invocamos las funciones con las interpretaciones

dibujar_tablero(inter1, asig, 1)
dibujar_tablero(inter2, asig, 2)
