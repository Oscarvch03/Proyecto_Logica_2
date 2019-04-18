# Clase Tree
class Tree:
    def __init__(self, label, left = None, right = None):
        self.label = label
        self.left = left
        self.right = right

###############################################################################
# Funciones Importantes

def VI(f, I):
    if(f.right == None):
        return I[f.label]
    elif(f.label == "-"):
        return 1 - VI(f.right, I)
    elif(f.label == "Y"):
        return VI(f.left, I) * VI(f.right, I)
    elif(f.label == "O"):
        return max(VI(f.left, I), VI(f.right, I))
    elif(f.label == ">"):
        return max(1 - VI(f.left, I), VI(f.right, I))
    elif(f.label == "$"):
        return 1 - (VI(f.left, I) - VI(f.right, I)) ** 2


def InOrder(A):
    conectivos = ["Y", "O", ">", "$"]
    if(A.right == None):
        return A.label
    elif(A.label == "-"):
        return "-" + InOrder(A.right)
    elif(A.label in conectivos):
        return "(" + InOrder(A.left) + A.label + InOrder(A.right) + ")"


def casos(letrasProposicionales):
    interps = []
    aux = {}
    cont = 0
    for a in letrasProposicionales:
        aux[a] = 1

    interps.append(aux)
    cont += 1
    # print(interps)
    for a in letrasProposicionales:
        interps_aux = [i for i in interps]

        for i in interps_aux:
            aux1 = {}

            for b in letrasProposicionales:
                if(a == b):
                    aux1[b] = 1 - i[b]
                else:
                    aux1[b] = i[b]

            interps.append(aux1)
            cont += 1
            print(cont)
    return interps


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


def soluciones(interpretaciones, formula):
    out = []
    for i in interpretaciones:
        valor = VI(formula, i)
        if(valor):
            out.append(i)

    return out

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
regla1A += "OOOOOOO"  # Revisar Y o O
# print(regla1A)

# for B
regla1B = ""
for i in range(1, 9):
    impl2 = "{2}{1}O{0}>".format(B[i], G[i + 1], I[i + 1])
    regla1B += impl2
regla1B += "OOOOOOO"  # Revisar Y o O
# print(regla1B)

# for C
regla1C = ""
for i in range(1, 9):
    impl3 = "{2}{1}O{0}>".format(C[i], D[i + 1], H[i + 1])
    regla1C += impl3
regla1C += "OOOOOOO"  # Revisar Y o O
# print(regla1C)

# for D
regla1D = ""
for i in range(1, 9):
    impl4 = "{2}{1}O{0}>".format(D[i], C[i + 1], I[i + 1])
    regla1D += impl4
regla1D += "OOOOOOO"  # Revisar Y o O
# print(regla1D)

# for E
# Si ubicamos el 1 en E no hay forma de ubicar los siguientes numeros

# for F
regla1F = ""
for i in range(1, 9):
    impl6 = "{2}{1}O{0}>".format(F[i], A[i + 1], G[i + 1])
    regla1F += impl6
regla1F += "OOOOOOO"  # Revisar Y o O
# print(regla1F)

# for G
regla1G = ""
for i in range(1, 9):
    impl7 = "{2}{1}O{0}>".format(G[i], B[i + 1], F[i + 1])
    regla1G += impl7
regla1G += "OOOOOOO"  # Revisar Y o O
# print(regla1G)

# for H
regla1H = ""
for i in range(1, 9):
    impl8 = "{2}{1}O{0}>".format(H[i], A[i + 1], C[i + 1])
    regla1H += impl8
regla1H += "OOOOOOO"  # Revisar Y o O
# print(regla1H)

# for I
regla1I = ""
for i in range(1, 9):
    impl9 = "{2}{1}O{0}>".format(I[i], B[i + 1], D[i + 1])
    regla1I += impl9
regla1I += "OOOOOOO"  # Revisar Y o O
# print(regla1I)

REGLA1 += regla1A + regla1B + regla1C + regla1D + regla1F
REGLA1 += regla1G + regla1H + regla1I + "YYYYYYY"
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
        regla2 += "YYYYYYY" + letra + "$"
        cont += 1
        # print(regla2)
        # print(cont)
        REGLA2 += regla2
REGLA2 += "O" * 80  # Revisar Y o O
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
        regla3 += "YYYYYYY" + letra + "$"
        cont += 1
        # print(regla3)
        # print(cont)
        REGLA3 += regla3
REGLA3 += "O" * 80
# print()
# print(REGLA3)
# x = string2Tree(REGLA3, ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
#                         ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

# Regla Final

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
REGLAFINAL = REGLA1 + REGLA2 + REGLA3 + "YY"
# print(REGLAFINAL) # Polaca Inversa
arbol = string2Tree(REGLAFINAL, letras, nums)
formula = InOrder(arbol)
# print(formula) # Forma Comun

###############################################################################

# Casos para las letras proposicionales

letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append("A" + str(i))
    letrasProposicionales.append("B" + str(i))
    letrasProposicionales.append("C" + str(i))
    letrasProposicionales.append("D" + str(i))
    letrasProposicionales.append("E" + str(i))
    letrasProposicionales.append("F" + str(i))
    letrasProposicionales.append("G" + str(i))
    letrasProposicionales.append("H" + str(i))
    letrasProposicionales.append("I" + str(i))
letrasProposicionales.sort()
# print(letrasProposicionales)
# print(len(letrasProposicionales))

"""casosPosibles = casos(letrasProposicionales)
print(len(casosPosibles))

soluciones3x3 = soluciones(casosPosibles, arbol)
print(len(soluciones3x3))"""

###############################################################################



###############################################################################
###############################################################################
# Reglas escritas de manera comun #############################################

# # for A
# regla1A = "("
# cont1 = 0
# for i in range(1, 9):
#     impl1 = "({0}>({1}O{2}))".format(A[i], F[i + 1], H[i + 1])
#     regla1A += impl1
#     cont1 += 1
#     if cont1 < 8:
#         regla1A += "O"  # Revisar Y o O
# regla1A += ")"
# # print(regla1A)
#
# # for B
# regla1B = "("
# cont2 = 0
# for i in range(1, 9):
#     impl2 = "({0}>({1}O{2}))".format(B[i], G[i + 1], I[i + 1])
#     regla1B += impl2
#     cont2 += 1
#     if cont2 < 8:
#         regla1B += "O"  # Revisar Y o O
# regla1B += ")"
# # print(regla1B)
#
# # for C
# regla1C = "("
# cont3 = 0
# for i in range(1, 9):
#     impl3 = "({0}>({1}O{2}))".format(C[i], D[i + 1], H[i + 1])
#     regla1C += impl3
#     cont3 += 1
#     if cont3 < 8:
#         regla1C += "O"  # Revisar Y o O
# regla1C += ")"
# # print(regla1C)
#
# # for D
# regla1D = "("
# cont4 = 0
# for i in range(1, 9):
#     impl4 = "({0}>({1}O{2}))".format(D[i], C[i + 1], I[i + 1])
#     regla1D += impl4
#     cont4 += 1
#     if cont4 < 8:
#         regla1D += "O"  # Revisar Y o O
# regla1D += ")"
# # print(regla1D)
#
# # for E
# # Si ubicamos el 1 en E no hay forma de ubicar los siguientes numeros
#
# # for F
# regla1F = "("
# cont6 = 0
# for i in range(1, 9):
#     impl6 = "({0}>({1}O{2}))".format(F[i], A[i + 1], G[i + 1])
#     regla1F += impl6
#     cont6 += 1
#     if cont6 < 8:
#         regla1F += "O"  # Revisar Y o O
# regla1F += ")"
# # print(regla1F)
#
# # for G
# regla1G = "("
# cont7 = 0
# for i in range(1, 9):
#     impl7 = "({0}>({1}O{2}))".format(G[i], B[i + 1], F[i + 1])
#     regla1G += impl7
#     cont7 += 1
#     if cont7 < 8:
#         regla1G += "O"  # Revisar Y o O
# regla1G += ")"
# # print(regla1G)
#
# # for H
# regla1H = "("
# cont8 = 0
# for i in range(1, 9):
#     impl8 = "({0}>({1}O{2}))".format(H[i], A[i + 1], C[i + 1])
#     regla1H += impl8
#     cont8 += 1
#     if cont8 < 8:
#         regla1H += "O"  # Revisar Y o O
# regla1H += ")"
# # print(regla1H)
#
# # for I
# regla1I = "("
# cont9 = 0
# for i in range(1, 9):
#     impl9 = "({0}>({1}O{2}))".format(I[i], B[i + 1], D[i + 1])
#     regla1I += impl9
#     cont9 += 1
#     if cont9 < 8:
#         regla1I += "O"  # Revisar Y o O
# regla1I += ")"
# # print(regla1I)
#
#
# REGLA1 += regla1A + "Y" + regla1B + "Y" + regla1C + "Y" + regla1D + "Y" + regla1F + "Y" + regla1G + "Y" + regla1H + "Y" + regla1I
# # print(REGLA1)
#
###############################################################################
#
# REGLA2 = ""
#
# for dic in LETRAS:
#     letras = dic.values()
#     cont2 = 0
#     for letra in letras:
#         cont = 0;
#         regla2 = "(" + letra + "$("
#         for letra2 in letras:
#             if letra2 != letra:
#                 regla2 += "-" + letra2
#                 cont += 1
#                 if cont < 8:
#                     regla2 += "Y"
#         regla2 += "))"
#         # print(regla2)
#         REGLA2 += regla2
#         cont2 += 1
#         if cont2 < 9:
#             REGLA2 += "O"  # Revisar Y o O
# # print()
# # print(REGLA2)
#
###############################################################################
#
# REGLA3 = ""
#
# for i in range(1, len(dic) + 1):
#     list = []
#     for dic in LETRAS:
#         list.append(dic[i])
#     # print(list)
#     cont2 = 0
#     for letra in list:
#         cont = 0
#         regla3 = "(" + letra + "$("
#         for letra2 in list:
#             if letra2 != letra:
#                 regla3 += "-" + letra2
#                 cont += 1
#                 if cont < 8:
#                     regla3 += "Y"
#         regla3 += "))"
#
#         # print(regla3)
#         REGLA3 += regla3
#         cont2 += 1
#         if cont2 < 9:
#             REGLA3 += "O"  # Revisar Y o O
# # print()
# # print(REGLA3)
#
###############################################################################
#
# REGLAFINAL = REGLA1 + "Y" + REGLA2 + "Y" + REGLA3
# # print(REGLAFINAL)
