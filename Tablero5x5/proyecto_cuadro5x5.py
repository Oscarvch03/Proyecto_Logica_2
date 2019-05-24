from rep_soluciones_tablero_5x5 import dibujar_tablero
from algoritmos import Tseitin, formaClausal
from DPLL import DPLL
# from DPLLisa import DPLL

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


#####################################################3

#Diccionarios de letras proposicionales

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
R = {}
S = {}
T = {}
U = {}
V = {}
W = {}
X = {}
Ñ = {}
Z = {}

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
    R[j] = "R0" + str(j)
    S[j] = "S0" + str(j)
    T[j] = "T0" + str(j)
    U[j] = "U0" + str(j)
    V[j] = "V0" + str(j)
    W[j] = "W0" + str(j)
    X[j] = "X0" + str(j)
    Ñ[j] = "Ñ0" + str(j)
    Z[j] = "Z0" + str(j)

for j in range(10, 26):
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
    R[j] = "R" + str(j)
    S[j] = "S" + str(j)
    T[j] = "T" + str(j)
    U[j] = "U" + str(j)
    V[j] = "V" + str(j)
    W[j] = "W" + str(j)
    X[j] = "X" + str(j)
    Ñ[j] = "Ñ" + str(j)
    Z[j] = "Z" + str(j)

LETRAS = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, P, Q, R, S, T, U, V, W, X, Ñ, Z]


###############################################################################
# Reglas escritas en forma polaca inversa #####################################
###############################################################################

# Regla 1

REGLA1 = ""

# for A
regla1A = ""
for i in range(1, 25):
    impl1 = "{2}{1}O{0}>".format(A[i], H[i + 1], L[i + 1])
    regla1A += impl1
regla1A += "Y" * 23

# for B
regla1B = ""
for i in range(1, 25):
    impl2 = "{3}{2}{1}OO{0}>".format(B[i], I[i + 1], K[i + 1], M[i + 1])
    regla1B += impl2
regla1B += "Y" * 23

# for C
regla1C = ""
for i in range(1, 25):
    impl3 = "{4}{3}{2}{1}OOO{0}>".format(C[i], F[i + 1], J[i + 1], L[i + 1], N[i + 1])
    regla1C += impl3
regla1C += "Y" * 23

# for D
regla1D = ""
for i in range(1, 25):
    impl4 = "{3}{2}{1}OO{0}>".format(D[i], G[i + 1], M[i + 1], P[i + 1])
    regla1D += impl4
regla1D += "Y" * 23

# for E
regla1E = ""
for i in range(1, 25):
    impl5 = "{2}{1}O{0}>".format(E[i], H[i + 1], N[i + 1])
    regla1E += impl5
regla1E += "Y" * 23

# for F
regla1F = ""
for i in range(1, 25):
    impl6 = "{3}{2}{1}OO{0}>".format(F[i], C[i + 1], M[i + 1], R[i + 1])
    regla1F += impl6
regla1F += "Y" * 23

# for G
regla1G = ""
for i in range(1, 25):
    impl7 = "{4}{3}{2}{1}OOO{0}>".format(G[i], D[i + 1], N[i + 1], Q[i + 1], S[i + 1])
    regla1G += impl7
regla1G += "Y" * 23

# for H
regla1H = ""
for i in range(1, 25):
    impl8 = "{6}{5}{4}{3}{2}{1}OOOOO{0}>".format(H[i], A[i + 1], E[i + 1], K[i + 1], P[i + 1], R[i + 1], T[i + 1])
    regla1H += impl8
regla1H += "Y" * 23

# for I
regla1I = ""
for i in range(1, 25):
    impl9 = "{4}{3}{2}{1}OOO{0}>".format(I[i], B[i + 1], L[i + 1], S[i + 1], U[i + 1])
    regla1I += impl9
regla1I += "Y" * 23

# for J
regla1J = ""
for i in range(1, 25):
    impl10 = "{3}{2}{1}OO{0}>".format(J[i], C[i + 1], M[i + 1], T[i + 1])
    regla1J += impl10
regla1J += "Y" * 23

# for K
regla1K = ""
for i in range(1, 25):
    impl11 = "{4}{3}{2}{1}OOO{0}>".format(K[i], B[i + 1], H[i + 1], S[i + 1], W[i + 1])
    regla1K += impl11
regla1K += "Y" * 23

# for L
regla1L = ""
for i in range(1, 25):
    impl12 = "{6}{5}{4}{3}{2}{1}OOOOO{0}>".format(L[i], A[i + 1], C[i + 1], I[i + 1], T[i + 1], V[i + 1], X[i + 1])
    regla1L += impl12
regla1L += "Y" * 23

# for M
regla1M = ""
for i in range(1, 25):
    impl13 = "{8}{7}{6}{5}{4}{3}{2}{1}OOOOOOO{0}>".format(M[i], B[i + 1], D[i + 1], F[i + 1], J[i + 1], Q[i + 1], U[i + 1], W[i + 1], Ñ[i + 1])
    regla1M += impl13
regla1M += "Y" * 23

# for N
regla1N = ""
for i in range(1, 25):
    impl14 = "{6}{5}{4}{3}{2}{1}OOOOO{0}>".format(N[i], C[i + 1], E[i + 1], G[i + 1], R[i + 1], X[i + 1], Z[i + 1])
    regla1N += impl14
regla1N += "Y" * 23

# for P
regla1P = ""
for i in range(1, 25):
    impl15 = "{4}{3}{2}{1}OOO{0}>".format(P[i], D[i + 1], H[i + 1], S[i + 1], Ñ[i + 1])
    regla1P += impl15
regla1P += "Y" * 23

# for Q
regla1Q = ""
for i in range(1, 25):
    impl16 = "{3}{2}{1}OO{0}>".format(Q[i], G[i + 1], M[i + 1], X[i + 1])
    regla1Q += impl16
regla1Q += "Y" * 23

# for R
regla1R = ""
for i in range(1, 25):
    impl17 = "{4}{3}{2}{1}OOO{0}>".format(R[i], H[i + 1], N[i + 1], Ñ[i + 1], F[i + 1])
    regla1R += impl17
regla1R += "Y" * 23

# for S
regla1S = ""
for i in range(1, 25):
    impl18 = "{6}{5}{4}{3}{2}{1}OOOOO{0}>".format(S[i], G[i + 1], I[i + 1], K[i + 1], P[i + 1], V[i + 1], Z[i + 1])
    regla1S += impl18
regla1S += "Y" * 23


# for T
regla1T = ""
for i in range(1, 25):
    impl19 = "{4}{3}{2}{1}OOO{0}>".format(T[i], H[i + 1], J[i + 1], L[i + 1], W[i + 1])
    regla1T += impl19
regla1T += "Y" * 23

# for U
regla1U = ""
for i in range(1, 25):
    impl20 = "{3}{2}{1}OO{0}>".format(U[i], I[i + 1], M[i + 1], X[i + 1])
    regla1U += impl20
regla1U += "Y" * 23

# for V
regla1V = ""
for i in range(1, 25):
    impl21 = "{2}{1}O{0}>".format(V[i], S[i + 1], L[i + 1])
    regla1V += impl21
regla1V += "Y" * 23

# for W
regla1W = ""
for i in range(1, 25):
    impl22 = "{3}{2}{1}OO{0}>".format(W[i], K[i + 1], M[i + 1], T[i + 1])
    regla1W += impl22
regla1W += "Y" * 23

# for X
regla1X = ""
for i in range(1, 25):
    impl23 = "{4}{3}{2}{1}OOO{0}>".format(X[i], L[i + 1], N[i + 1], Q[i + 1], U[i + 1])
    regla1X += impl23
regla1X += "Y" * 23

# for Ñ
regla1Ñ = ""
for i in range(1, 25):
    impl24 = "{3}{2}{1}OO{0}>".format(Ñ[i], M[i + 1], P[i + 1], R[i + 1])
    regla1Ñ += impl24
regla1Ñ += "Y" * 23

# for Z
regla1Z = ""
for i in range(1, 25):
    impl25 = "{2}{1}O{0}>".format(Z[i], N[i + 1], S[i + 1])
    regla1Z += impl25
regla1Z += "Y" * 23


REGLA1 += regla1A + regla1B + regla1C + regla1D + regla1E + regla1F + regla1G
REGLA1 += regla1H + regla1I + regla1J + regla1K + regla1L + regla1M + regla1N
REGLA1 += regla1P + regla1Q + regla1R + regla1S + regla1T + regla1U + regla1V
REGLA1 += regla1W + regla1X + regla1Ñ + regla1Z + ("Y" * 24)

# print(REGLA1)
# arbol1 = string2Tree(REGLA1, ["A", "B", "C", "D", "E", "F", "G", "H",
#                               "I", "J", "K", "L", "M", "N", "P", "Q",
#                               "R", "S", "T", "U", "V", "W", "X", "Ñ", "Z"],
#                              ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# print(arbol1)
# y1 = InOrder(arbol1)
# print(y1)
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
        regla2 += ("Y" * 23) + letra + "$"
        cont += 1
        # print(regla2)
        # print(cont)
        REGLA2 += regla2
REGLA2 += "Y" * 624
# cont = 0
# for i in range(1, 625):
#     if i % 25 == 0:
#         REGLA2 += "Y"
#     else:
#         REGLA2 += "O"

# print(REGLA2)
# arbol2 = string2Tree(REGLA2, ["A", "B", "C", "D", "E", "F", "G", "H",
#                               "I", "J", "K", "L", "M", "N", "P", "Q",
#                               "R", "S", "T", "U", "V", "W", "X", "Ñ", "Z"],
#                               ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# print(arbol2)
# y2 = InOrder(arbol2)
# print(y2)
# print("".join(y2))

##############################################################

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
        regla3 += ("Y" * 23) + letra + "$"
        cont += 1
        # print(regla3)
        # print(cont)
        REGLA3 += regla3
REGLA3 += "Y" * 624
# for i in range(1, 625):
#     if i % 25 == 0:
#         REGLA3 += "Y"
#     else:
#         REGLA3 += "O"


# print()
# print(REGLA3)
# arbol3 = string2Tree(REGLA3, ["A", "B", "C", "D", "E", "F", "G", "H",
#                               "I", "J", "K", "L", "M", "N", "P", "Q",
#                               "R", "S", "T", "U", "V", "W", "X", "Ñ", "Z"],
#                              ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# y3 = InOrder(arbol3)
# print(y3)
# print("".join(y3))

################################################################################

# Regla Final

letrasTs = []
for i in range(1, 10):
    letrasTs.append("A0" + str(i))
    letrasTs.append("B0" + str(i))
    letrasTs.append("C0" + str(i))
    letrasTs.append("D0" + str(i))
    letrasTs.append("E0" + str(i))
    letrasTs.append("F0" + str(i))
    letrasTs.append("G0" + str(i))
    letrasTs.append("H0" + str(i))
    letrasTs.append("I0" + str(i))
    letrasTs.append("J0" + str(i))
    letrasTs.append("K0" + str(i))
    letrasTs.append("L0" + str(i))
    letrasTs.append("M0" + str(i))
    letrasTs.append("N0" + str(i))
    letrasTs.append("P0" + str(i))
    letrasTs.append("Q0" + str(i))
    letrasTs.append("R0" + str(i))
    letrasTs.append("S0" + str(i))
    letrasTs.append("T0" + str(i))
    letrasTs.append("U0" + str(i))
    letrasTs.append("V0" + str(i))
    letrasTs.append("W0" + str(i))
    letrasTs.append("X0" + str(i))
    letrasTs.append("Ñ0" + str(i))
    letrasTs.append("Z0" + str(i))

for i in range(10, 26):
    letrasTs.append("A" + str(i))
    letrasTs.append("B" + str(i))
    letrasTs.append("C" + str(i))
    letrasTs.append("D" + str(i))
    letrasTs.append("E" + str(i))
    letrasTs.append("F" + str(i))
    letrasTs.append("G" + str(i))
    letrasTs.append("H" + str(i))
    letrasTs.append("I" + str(i))
    letrasTs.append("J" + str(i))
    letrasTs.append("K" + str(i))
    letrasTs.append("L" + str(i))
    letrasTs.append("M" + str(i))
    letrasTs.append("N" + str(i))
    letrasTs.append("P" + str(i))
    letrasTs.append("Q" + str(i))
    letrasTs.append("R" + str(i))
    letrasTs.append("S" + str(i))
    letrasTs.append("T" + str(i))
    letrasTs.append("U" + str(i))
    letrasTs.append("V" + str(i))
    letrasTs.append("W" + str(i))
    letrasTs.append("X" + str(i))
    letrasTs.append("Ñ" + str(i))
    letrasTs.append("Z" + str(i))


letras = ["A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "P", "Q",
          "R", "S", "T", "U", "V", "W", "X", "Ñ", "Z"]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
print("cont: ", cont)
# print("".join(FNC))

FC = formaClausal(FNC)
# print(FC)
#
inter = {}
#
respuesta, interpretacion = DPLL(FC, inter)
print("Tablero 5x5: ")
print("La formula es: ", respuesta)
print("Su interpretación es: ", interpretacion)
# print("Por lo tanto este problema no tiene solución. ")

# solucion = DPLL(FC)
# print(solucion)


###############################################################################
