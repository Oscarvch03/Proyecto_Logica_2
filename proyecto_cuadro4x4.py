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
        elif(c in numeros and len(str) < 2):
            str += c
        elif(c in numeros and len(str) == 2):
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

A = {}
B = {}
C = {}
D = {}
E = {}
F = {}
G = {}
H = {}
I = {}
J = {}
K = {}
L = {}
M = {}
N = {}
P = {}
Q = {}

for j in range(1, 10):
    A[j] = "A0" + str(j)
    B[j] = "B0" + str(j)
    C[j] = "C0" + str(j)
    D[j] = "D0" + str(j)
    E[j] = "E0" + str(j)
    F[j] = "F0" + str(j)
    G[j] = "G0" + str(j)
    H[j] = "H0" + str(j)
    I[j] = "I0" + str(j)
    J[j] = "J0" + str(j)
    K[j] = "K0" + str(j)
    L[j] = "L0" + str(j)
    M[j] = "M0" + str(j)
    N[j] = "N0" + str(j)
    P[j] = "P0" + str(j)
    Q[j] = "Q0" + str(j)

for j in range(10, 17):
    A[j] = "A" + str(j)
    B[j] = "B" + str(j)
    C[j] = "C" + str(j)
    D[j] = "D" + str(j)
    E[j] = "E" + str(j)
    F[j] = "F" + str(j)
    G[j] = "G" + str(j)
    H[j] = "H" + str(j)
    I[j] = "I" + str(j)
    J[j] = "J" + str(j)
    K[j] = "K" + str(j)
    L[j] = "L" + str(j)
    M[j] = "M" + str(j)
    N[j] = "N" + str(j)
    P[j] = "P" + str(j)
    Q[j] = "Q" + str(j)

# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)
# print(G)
# print(H)
# print(I)
# print(J)
# print(K)
# print(L)
# print(M)
# print(N)
# print(P)
# print(Q)

LETRAS = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, P, Q]

###############################################################################
# Reglas escritas en forma polaca inversa #####################################
###############################################################################

# Regla 1

REGLA1 = ""

# for A
regla1A = ""
for i in range(1, 16):
    impl1 = "{2}{1}O{0}>".format(A[i], G[i + 1], J[i + 1])
    regla1A += impl1
regla1A += "O" * 14
# print(regla1A)

# for B
regla1B = ""
for i in range(1, 16):
    impl2 = "{3}{2}{1}OO{0}>".format(B[i], H[i + 1], I[i + 1], K[i + 1])
    regla1B += impl2
regla1B += "O" * 14
# print(regla1B)

# for C
regla1C = ""
for i in range(1, 16):
    impl3 = "{3}{2}{1}OO{0}>".format(C[i], E[i + 1], J[i + 1], L[i + 1])
    regla1C += impl3
regla1C += "O" * 14
# print(regla1C)

# for D
regla1D = ""
for i in range(1, 16):
    impl4 = "{2}{1}O{0}>".format(D[i], F[i + 1], K[i + 1])
    regla1D += impl4
regla1D += "O" * 14
# print(regla1D)

# for E
regla1E = ""
for i in range(1, 16):
    impl5 = "{3}{2}{1}OO{0}>".format(E[i], C[i + 1], K[i + 1], N[i + 1])
    regla1E += impl5
regla1E += "O" * 14
# print(regla1E)

# for F
regla1F = ""
for i in range(1, 16):
    impl6 = "{4}{3}{2}{1}OOO{0}>".format(F[i], D[i + 1], L[i + 1],
                                         M[i + 1], P[i + 1])
    regla1F += impl6
regla1F += "O" * 14
# print(regla1F)

# for G
regla1G = ""
for i in range(1, 16):
    impl7 = "{4}{3}{2}{1}OOO{0}>".format(G[i], A[i + 1], I[i + 1],
                                         N[i + 1], Q[i + 1])
    regla1G += impl7
regla1G += "O" * 14
# print(regla1G)

# for H
regla1H = ""
for i in range(1, 16):
    impl8 = "{3}{2}{1}OO{0}>".format(H[i], B[i + 1], J[i + 1], P[i + 1])
    regla1H += impl8
regla1H += "O" * 14
# print(regla1H)

# for I
regla1I = ""
for i in range(1, 16):
    impl9 = "{3}{2}{1}OO{0}>".format(I[i], B[i + 1], G[i + 1], P[i + 1])
    regla1I += impl9
regla1I += "O" * 14
# print(regla1I)

# for J
regla1J = ""
for i in range(1, 16):
    impl10 = "{4}{3}{2}{1}OOO{0}>".format(J[i], A[i + 1], C[i + 1],
                                          H[i + 1], Q[i + 1])
    regla1J += impl10
regla1J += "O" * 14
# print(regla1J)

# for K
regla1K = ""
for i in range(1, 16):
    impl11 = "{4}{3}{2}{1}OOO{0}>".format(K[i], B[i + 1], D[i + 1],
                                          E[i + 1], M[i + 1])
    regla1K += impl11
regla1K += "O" * 14
# print(regla1K)

# for L
regla1L = ""
for i in range(1, 16):
    impl12 = "{3}{2}{1}OO{0}>".format(L[i], C[i + 1], F[i + 1], N[i + 1])
    regla1L += impl12
regla1L += "O" * 14
# print(regla1L)

# for M
regla1M = ""
for i in range(1, 16):
    impl13 = "{2}{1}O{0}>".format(M[i], F[i + 1], K[i + 1])
    regla1M += impl13
regla1M += "O" * 14
# print(regla1M)

# for N
regla1N = ""
for i in range(1, 16):
    impl14 = "{3}{2}{1}OO{0}>".format(N[i], E[i + 1], G[i + 1], L[i + 1])
    regla1N += impl14
regla1N += "O" * 14
# print(regla1N)

# for P
regla1P = ""
for i in range(1, 16):
    impl15 = "{3}{2}{1}OO{0}>".format(P[i], F[i + 1], H[i + 1], I[i + 1])
    regla1P += impl15
regla1P += "O" * 14
# print(regla1P)

# for Q
regla1Q = ""
for i in range(1, 16):
    impl16 = "{2}{1}O{0}>".format(Q[i], G[i + 1], J[i + 1])
    regla1Q += impl16
regla1Q += "O" * 14
# print(regla1Q)

REGLA1 += regla1A + regla1B + regla1C + regla1D + regla1E + regla1F
REGLA1 += regla1G + regla1H + regla1I + regla1J + regla1K + regla1L
REGLA1 += regla1M + regla1N + regla1P + regla1Q + ("Y" * 15)
# x = string2Tree(REGLA1, ["A", "B", "C", "D", "E", "F", "G", "H",
#                          "I", "J", "K", "L", "M", "N", "P", "Q"],
#                         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
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
        regla2 += ("Y" * 14) + letra + "$"
        cont += 1
        # print(regla2)
        # print(cont)
        REGLA2 += regla2
REGLA2 += "O" * 255  # Revisar Y o O
# print()
# print(REGLA2)
# x = string2Tree(REGLA2, ["A", "B", "C", "D", "E", "F", "G", "H",
#                          "I", "J", "K", "L", "M", "N", "P", "Q"],
#                         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

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
        regla3 += ("Y" * 14) + letra + "$"
        cont += 1
        # print(regla3)
        # print(cont)
        REGLA3 += regla3
REGLA3 += "O" * 255
# print()
# print(REGLA3)
# x = string2Tree(REGLA3, ["A", "B", "C", "D", "E", "F", "G", "H",
#                          "I", "J", "K", "L", "M", "N", "P", "Q"],
#                         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y = InOrder(x)
# print(y)

###############################################################################

# Regla Final

letras = ["A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "P", "Q"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
REGLAFINAL = REGLA1 + REGLA2 + REGLA3 + "YY"
# print(REGLAFINAL) # Polaca Inversa
arbol = string2Tree(REGLAFINAL, letras, nums)
formula = InOrder(arbol)
# print(formula) # Forma Comun

###############################################################################

# Casos para las letras proposicionales

letrasProposicionales = []
for i in range(1, 10):
    letrasProposicionales.append("A0" + str(i))
    letrasProposicionales.append("B0" + str(i))
    letrasProposicionales.append("C0" + str(i))
    letrasProposicionales.append("D0" + str(i))
    letrasProposicionales.append("E0" + str(i))
    letrasProposicionales.append("F0" + str(i))
    letrasProposicionales.append("G0" + str(i))
    letrasProposicionales.append("H0" + str(i))
    letrasProposicionales.append("I0" + str(i))
    letrasProposicionales.append("J0" + str(i))
    letrasProposicionales.append("K0" + str(i))
    letrasProposicionales.append("L0" + str(i))
    letrasProposicionales.append("M0" + str(i))
    letrasProposicionales.append("N0" + str(i))
    letrasProposicionales.append("P0" + str(i))
    letrasProposicionales.append("Q0" + str(i))

for i in range(10, 17):
    letrasProposicionales.append("A" + str(i))
    letrasProposicionales.append("B" + str(i))
    letrasProposicionales.append("C" + str(i))
    letrasProposicionales.append("D" + str(i))
    letrasProposicionales.append("E" + str(i))
    letrasProposicionales.append("F" + str(i))
    letrasProposicionales.append("G" + str(i))
    letrasProposicionales.append("H" + str(i))
    letrasProposicionales.append("I" + str(i))
    letrasProposicionales.append("J" + str(i))
    letrasProposicionales.append("K" + str(i))
    letrasProposicionales.append("L" + str(i))
    letrasProposicionales.append("M" + str(i))
    letrasProposicionales.append("N" + str(i))
    letrasProposicionales.append("P" + str(i))
    letrasProposicionales.append("Q" + str(i))

letrasProposicionales.sort()
# print(letrasProposicionales)
# print(len(letrasProposicionales))

"""casosPosibles = casos(letrasProposicionales)
print(len(casosPosibles))

soluciones4x4 = soluciones(casosPosibles, arbol)
print(len(soluciones4x4))"""

###############################################################################
