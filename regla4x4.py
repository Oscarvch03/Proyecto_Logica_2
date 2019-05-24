class Tree:
    def __init__(self, label, left = None, right = None):
        self.label = label
        self.left = left
        self.right = right

    def __str__(self):
        return "Tree({0}, {1}, {2})".format(self.label, self.left, self.right)


def VI(f, I):
    if(f.right == None):
        # print("letra")
        return I[f.label]
    elif(f.label == "-"):
        # print("negado")
        return 1 - VI(f.right, I)
    elif(f.label == "Y"):
        # print("conjuncion")
        return VI(f.left, I) * VI(f.right, I)
    elif(f.label == "O"):
        # print("disyuncion")
        return max(VI(f.left, I), VI(f.right, I))
    elif(f.label == ">"):
        # print("implicacion")
        return max(1 - VI(f.left, I), VI(f.right, I))
    elif(f.label == "$"):
        # print("sii")
        return 1 - ((VI(f.left, I) - VI(f.right, I)) ** 2)


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
regla1A += "Y" * 14
# print(regla1A)

# for B
regla1B = ""
for i in range(1, 16):
    impl2 = "{3}{2}{1}OO{0}>".format(B[i], H[i + 1], I[i + 1], K[i + 1])
    regla1B += impl2
regla1B += "Y" * 14
# print(regla1B)

# for C
regla1C = ""
for i in range(1, 16):
    impl3 = "{3}{2}{1}OO{0}>".format(C[i], E[i + 1], J[i + 1], L[i + 1])
    regla1C += impl3
regla1C += "Y" * 14
# print(regla1C)

# for D
regla1D = ""
for i in range(1, 16):
    impl4 = "{2}{1}O{0}>".format(D[i], F[i + 1], K[i + 1])
    regla1D += impl4
regla1D += "Y" * 14
# print(regla1D)

# for E
regla1E = ""
for i in range(1, 16):
    impl5 = "{3}{2}{1}OO{0}>".format(E[i], C[i + 1], K[i + 1], N[i + 1])
    regla1E += impl5
regla1E += "Y" * 14
# print(regla1E)

# for F
regla1F = ""
for i in range(1, 16):
    impl6 = "{4}{3}{2}{1}OOO{0}>".format(F[i], D[i + 1], L[i + 1],
                                         M[i + 1], P[i + 1])
    regla1F += impl6
regla1F += "Y" * 14
# print(regla1F)

# for G
regla1G = ""
for i in range(1, 16):
    impl7 = "{4}{3}{2}{1}OOO{0}>".format(G[i], A[i + 1], I[i + 1],
                                         N[i + 1], Q[i + 1])
    regla1G += impl7
regla1G += "Y" * 14
# print(regla1G)

# for H
regla1H = ""
for i in range(1, 16):
    impl8 = "{3}{2}{1}OO{0}>".format(H[i], B[i + 1], J[i + 1], P[i + 1])
    regla1H += impl8
regla1H += "Y" * 14
# print(regla1H)

# for I
regla1I = ""
for i in range(1, 16):
    impl9 = "{3}{2}{1}OO{0}>".format(I[i], B[i + 1], G[i + 1], P[i + 1])
    regla1I += impl9
regla1I += "Y" * 14
# print(regla1I)

# for J
regla1J = ""
for i in range(1, 16):
    impl10 = "{4}{3}{2}{1}OOO{0}>".format(J[i], A[i + 1], C[i + 1],
                                          H[i + 1], Q[i + 1])
    regla1J += impl10
regla1J += "Y" * 14
# print(regla1J)

# for K
regla1K = ""
for i in range(1, 16):
    impl11 = "{4}{3}{2}{1}OOO{0}>".format(K[i], B[i + 1], D[i + 1],
                                          E[i + 1], M[i + 1])
    regla1K += impl11
regla1K += "Y" * 14
# print(regla1K)

# for L
regla1L = ""
for i in range(1, 16):
    impl12 = "{3}{2}{1}OO{0}>".format(L[i], C[i + 1], F[i + 1], N[i + 1])
    regla1L += impl12
regla1L += "Y" * 14
# print(regla1L)

# for M
regla1M = ""
for i in range(1, 16):
    impl13 = "{2}{1}O{0}>".format(M[i], F[i + 1], K[i + 1])
    regla1M += impl13
regla1M += "Y" * 14
# print(regla1M)

# for N
regla1N = ""
for i in range(1, 16):
    impl14 = "{3}{2}{1}OO{0}>".format(N[i], E[i + 1], G[i + 1], L[i + 1])
    regla1N += impl14
regla1N += "Y" * 14
# print(regla1N)

# for P
regla1P = ""
for i in range(1, 16):
    impl15 = "{3}{2}{1}OO{0}>".format(P[i], F[i + 1], H[i + 1], I[i + 1])
    regla1P += impl15
regla1P += "Y" * 14
# print(regla1P)

# for Q
regla1Q = ""
for i in range(1, 16):
    impl16 = "{2}{1}O{0}>".format(Q[i], G[i + 1], J[i + 1])
    regla1Q += impl16
regla1Q += "Y" * 14
# print(regla1Q)

REGLA1 += regla1A + regla1B + regla1C + regla1D + regla1E + regla1F
REGLA1 += regla1G + regla1H + regla1I + regla1J + regla1K + regla1L
REGLA1 += regla1M + regla1N + regla1P + regla1Q + ("Y" * 15)

# print(REGLA1)
arbol1 = string2Tree(REGLA1, ["A", "B", "C", "D", "E", "F", "G", "H",
                              "I", "J", "K", "L", "M", "N", "P", "Q"],
                              ["0", "1", "2", "3", "4", "5", "6", "7",
                              "8", "9"])
# # print(arbol1)
# y1 = InOrder(arbol1)
# # print(y1)
# print("".join(y1))

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
REGLA2 += "Y" * 255

# print(REGLA2)
arbol2 = string2Tree(REGLA2, ["A", "B", "C", "D", "E", "F", "G", "H",
                              "I", "J", "K", "L", "M", "N", "P", "Q"],
                             ["0", "1", "2", "3", "4", "5", "6", "7",
                              "8", "9"])
# # print(arbol2)
# y2 = InOrder(arbol2)
# # print(y2)
# print("".join(y2))

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
REGLA3 += "Y" * 255

# print(REGLA3)
arbol3 = string2Tree(REGLA3, ["A", "B", "C", "D", "E", "F", "G", "H",
                              "I", "J", "K", "L", "M", "N", "P", "Q"],
                             ["0", "1", "2", "3", "4", "5", "6", "7",
                              "8", "9"])
# y3 = InOrder(arbol3)
# # print(y3)
# print("".join(y3))

############################ BLOQUE PRINCIPAL DE INSTRUCCIONES

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

inter1["A01"] = 0
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

# inter1["A01"] = 1
# inter1["B08"] = 1
# inter1["C13"] = 1
# inter1["D10"] = 1
# inter1["E14"] = 1
# inter1["F11"] = 1
# inter1["G04"] = 1
# inter1["H07"] = 1
# inter1["I05"] = 1
# inter1["J02"] = 1
# inter1["K09"] = 1
# inter1["L12"] = 1
# inter1["M16"] = 1
# inter1["N15"] = 1
# inter1["P06"] = 1
# inter1["Q03"] = 1

###############################################################################
print()
print("Regla 1: ", VI(arbol1, inter1))
print("Regla 2: ", VI(arbol2, inter1))
print("Regla 3: ", VI(arbol3, inter1))

###############################################################################

letras = ["A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "P", "Q"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
REGLAFINAL = REGLA1 + REGLA2 + REGLA3 + "YY"
# print(REGLAFINAL) # Polaca Inversa
arbol = string2Tree(REGLAFINAL, letras, nums)
formula = InOrder(arbol)
# print(formula) # Forma Comun
# print("".join(formula))
# print(arbol)

###############################################################################

ValorVd = VI(arbol, inter1)
print()
print("Tablero 4x4.")
print()
print("La interpretacion es: ")
for i in inter1:
    if(inter1[i] == 1):
        print(i, inter1[i])
print()
print("El valor de verdad es: ", ValorVd)
