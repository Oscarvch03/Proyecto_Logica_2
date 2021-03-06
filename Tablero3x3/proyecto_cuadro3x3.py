# Librerias y Modulos Importados
from rep_soluciones_tablero_3x3 import dibujar_tablero
from algoritmos import Tseitin, formaClausal
from DPLL import DPLL

# Clase Tree
class Tree:
    def __init__(self, label, left = None, right = None):
        self.label = label
        self.left = left
        self.right = right

###############################################################################
# Funciones Importantes

def InOrder(A):
    conectivos = ["Y", "O", ">", "$"]
    if(A.right == None):
        return [A.label]
    elif(A.label == "-"):
        return ["-", A.right.label]
    elif(A.label in conectivos):
        return ["("] + InOrder(A.left) + [A.label] + InOrder(A.right) + [")"]


def string2Tree(A, letrasProposicionales, numeros):
    conectivos = ["O", "Y", ">", "$"]
    pila = []

    str = ""
    for c in A:
        if(c in letrasProposicionales):
            str += c
        elif(c in numeros):
            str += c
            pila.append(Tree(str, None, None))
            str = ""
        elif(c == "-"):
            formulaAux = Tree(c, None, pila[-1])
            del(pila[-1])
            pila.append(formulaAux)
        elif(c in conectivos):
            formulaAux = Tree(c, pila[-1], pila[-2])
            del(pila[-1])
            del(pila[-1])
            pila.append(formulaAux)

    return pila[-1]


###############################################################################
# Diccionarios de letras proposicionales

A = {1:"A1", 2:"A2", 3:"A3", 4:"A4", 5:"A5", 6:"A6", 7:"A7", 8:"A8", 9:"A9"}
B = {1:"B1", 2:"B2", 3:"B3", 4:"B4", 5:"B5", 6:"B6", 7:"B7", 8:"B8", 9:"B9"}
C = {1:"C1", 2:"C2", 3:"C3", 4:"C4", 5:"C5", 6:"C6", 7:"C7", 8:"C8", 9:"C9"}
D = {1:"D1", 2:"D2", 3:"D3", 4:"D4", 5:"D5", 6:"D6", 7:"D7", 8:"D8", 9:"D9"}
E = {1:"E1", 2:"E2", 3:"E3", 4:"E4", 5:"E5", 6:"E6", 7:"E7", 8:"E8", 9:"E9"}
F = {1:"F1", 2:"F2", 3:"F3", 4:"F4", 5:"F5", 6:"F6", 7:"F7", 8:"F8", 9:"F9"}
G = {1:"G1", 2:"G2", 3:"G3", 4:"G4", 5:"G5", 6:"G6", 7:"G7", 8:"G8", 9:"G9"}
H = {1:"H1", 2:"H2", 3:"H3", 4:"H4", 5:"H5", 6:"H6", 7:"H7", 8:"H8", 9:"H9"}
I = {1:"I1", 2:"I2", 3:"I3", 4:"I4", 5:"I5", 6:"I6", 7:"I7", 8:"I8", 9:"I9"}

LETRAS = [A, B, C, D, E, F, G, H, I]

###############################################################################
# Reglas escritas en forma polaca inversa #####################################
###############################################################################

# Regla 1

REGLA1 = ""

# for A
regla1A = ""
for i in range(1, 9):
    impl1 = "{2}{1}O{0}>".format(A[i], F[i + 1], H[i + 1])
    regla1A += impl1
regla1A += ("Y" * 7)
# print(regla1A)

# for B
regla1B = ""
for i in range(1, 9):
    impl2 = "{2}{1}O{0}>".format(B[i], G[i + 1], I[i + 1])
    regla1B += impl2
regla1B += ("Y" * 7)
# print(regla1B)

# for C
regla1C = ""
for i in range(1, 9):
    impl3 = "{2}{1}O{0}>".format(C[i], D[i + 1], H[i + 1])
    regla1C += impl3
regla1C += ("Y" * 7)
# print(regla1C)

# for D
regla1D = ""
for i in range(1, 9):
    impl4 = "{2}{1}O{0}>".format(D[i], C[i + 1], I[i + 1])
    regla1D += impl4
regla1D += ("Y" * 7)
# print(regla1D)

# for E
# Si ubicamos el 1 en E no hay forma de ubicar los siguientes numeros

# for F
regla1F = ""
for i in range(1, 9):
    impl6 = "{2}{1}O{0}>".format(F[i], A[i + 1], G[i + 1])
    regla1F += impl6
regla1F += ("Y" * 7)
# print(regla1F)

# for G
regla1G = ""
for i in range(1, 9):
    impl7 = "{2}{1}O{0}>".format(G[i], B[i + 1], F[i + 1])
    regla1G += impl7
regla1G += ("Y" * 7)
# print(regla1G)

# for H
regla1H = ""
for i in range(1, 9):
    impl8 = "{2}{1}O{0}>".format(H[i], A[i + 1], C[i + 1])
    regla1H += impl8
regla1H += ("Y" * 7)
# print(regla1H)

# for I
regla1I = ""
for i in range(1, 9):
    impl9 = "{2}{1}O{0}>".format(I[i], B[i + 1], D[i + 1])
    regla1I += impl9
regla1I += ("Y" * 7)
# print(regla1I)

REGLA1 += regla1A + regla1B + regla1C + regla1D + regla1F
REGLA1 += regla1G + regla1H + regla1I + ("Y" * 7)

# x = string2Tree(REGLA1, ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
#                         ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

# Regla 2

REGLA2 = ""
cont = 0
for dic in LETRAS:
    letras = dic.values()
    for letra in letras:
        regla2 = ""
        for letra2 in letras:
            if letra2 != letra:
                regla2 += letra2 + "-"
        regla2 += ("Y" * 7) + letra + "$"
        cont += 1
        # print(regla2)
        # print(cont)
        REGLA2 += regla2
REGLA2 += "Y" * 80

# print()
# print(REGLA2)
# x = string2Tree(REGLA2, ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
#                         ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

# Regla 3

REGLA3 = ""

cont = 0
for i in range(1, len(dic) + 1):
    list = []
    for dic in LETRAS:
        list.append(dic[i])
    # print(list)
    for letra in list:
        regla3 = ""
        for letra2 in list:
            if letra2 != letra:
                regla3 += letra2 + "-"
        regla3 += ("Y" * 7) + letra + "$"
        cont += 1
        # print(regla3)
        # print(cont)
        REGLA3 += regla3
REGLA3 += "Y" * 80

# print()
# print(REGLA3)
# x = string2Tree(REGLA3, ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
#                         ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

# Regla Final

letrasTs = []
for i in range(1, 10):
    letrasTs.append("A" + str(i))
    letrasTs.append("B" + str(i))
    letrasTs.append("C" + str(i))
    letrasTs.append("D" + str(i))
    letrasTs.append("E" + str(i))
    letrasTs.append("F" + str(i))
    letrasTs.append("G" + str(i))
    letrasTs.append("H" + str(i))
    letrasTs.append("I" + str(i))

# print(letrasTs)

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
REGLAFINAL = REGLA1 + REGLA2 + REGLA3 + "YY"
# print(REGLAFINAL) # Polaca Inversa
arbol = string2Tree(REGLAFINAL, letras, nums)
formula = InOrder(arbol)
# print(formula) # Forma Comun
# print("".join(formula))

###############################################################################

# Solucion al problema

FNC, cont = Tseitin(formula, letrasTs)
# print(FNC)
print()
print("Letras de Tseitin: ", cont)
# FNCSN = withoutDN(FNC)
# print(FNCSN)
FC = formaClausal(FNC)
# print(FC)

inter = {}

respuesta, interpretacion = DPLL(FC, inter)
print()
print("Tablero 3x3: ")
print()
print("La formula es: ", respuesta)
print("Su interpretación es: ", interpretacion)
print("Por lo tanto este problema no tiene solución. ")

###############################################################################
