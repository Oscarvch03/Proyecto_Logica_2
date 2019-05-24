def EquFNC(A):
    # out = []
    if(len(A) == 4):
        out = ["(", "-" + A[0], "O", "".join(A[2:]), ")", "Y",
               "(", A[0], "O", A[3], ")"]
    elif(len(A) == 7):
        if (A[4] == "Y"):
            out = ["(", A[3], "O", "-" + A[0], ")", "Y",
                   "(", A[5], "O", "-" + A[0], ")", "Y",
                   "(", "-" + A[3], "O", "-" + A[5], "O", A[0], ")"]
        elif(A[4] == "O"):
            out = ["(", "-" + A[3], "O", A[0], ")", "Y",
                   "(", "-" + A[5], "O", A[0], ")", "Y",
                   "(", A[3], "O", A[5], "O", "-" + A[0], ")"]
        elif(A[4] == ">"):
            out = ["(", A[3], "O", A[0], ")", "Y",
                   "(", "-" + A[5], "O", A[0], ")", "Y",
                   "(", "-" + A[3], "O", A[5], "O", "-" + A[0], ")"]
        elif(A[4] == "$"):
            out = ["(", "-" + A[0], "O", "-" + A[3], "O", A[5], ")", "Y",
                   "(", "-" + A[0], "O", "-" + A[5], "O", A[3], ")", "Y",
                   "(", A[3], "O", A[5], "O", A[0], ")", "Y",
                   "(", A[3], "O", "-" + A[3], "O", A[0], ")", "Y",
                   "(", "-" + A[5], "O", A[5], "O", A[0], ")", "Y",
                   "(", "-" + A[5], "O", "-" + A[3], "O", A[0], ")"]
    return out


def Tseitin(A, letrasProposicionalesA):
    # letrasProposicionalesB = ["X" + str(i) for i in range(1, 501)]
    letrasProposicionalesB = []
    for m in range(1, 10):
        letrasProposicionalesB.append("x0000" + str(m))
    for m in range(10, 100):
        letrasProposicionalesB.append("x000" + str(m))
    for m in range(100, 1000):
        letrasProposicionalesB.append("x00" + str(m))
    for m in range(1000, 10000):
        letrasProposicionalesB.append("x0" + str(m))
    for m in range(10000, 70000):
        letrasProposicionalesB.append("x" + str(m))
    # print(letrasProposicionalesB)
    # print(len(letrasProposicionalesB))
    cont = 0
    atomos = letrasProposicionalesA + letrasProposicionalesB
    # print(atomos)
    L = []
    pila = []
    i = -1
    s = A[0]

    while(len(A) > 0):
        if(s in atomos and len(pila) > 0 and pila[-1] == "-"):
            i += 1
            atomo = letrasProposicionalesB[i]
            # print(atomo)
            pila = pila[:-1]
            pila.append(atomo)
            # print(pila)
            L.append([atomo, "$", "-", s])
            cont += 1
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif(s == ")"):
            w = pila[-1]
            O = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila) - 4]
            i += 1
            atomo = letrasProposicionalesB[i]
            # print(atomo)
            # print(pila)
            L.append([atomo, "$", "(", v, O, w, ")"])
            cont += 1
            # pila = pila[:-1]
            s = atomo
        else:
            pila.append(s)
            # print(pila)
            # pila = pila[:-1]
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    # print()
    # print(L)
    B = []
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]

    # print(L)
    # L.reverse()
    # print(L)

    for X in L:
        # print("X: ", X)
        # print("formula: ", X)
        Y = EquFNC(X)
        # print("formula en fnc: ", Y)
        # print()
        # print(Y)
        # B += "Y" + str(Y)
        B.append("Y")
        # B.append("(")
        for f in Y:
            B.append(f)
        # B.append(")")
    B = [atomo] + B

    return B, cont


# def Clausula(C):
#     # print(C)
#     L = []
#     s = C[0]
#     while(len(C) > 0):
#         if(s == "O" or s == "(" or s == ")"):
#             C = C[1:]
#         # elif(s == "-"):
#         #     literal = s + C[1]
#         #     # print(literal)
#         #     L.append(literal)
#         #     # L += literal
#         #     C = C[2:]
#         else:
#             L.append(s)
#             # L += s
#             C = C[1:]
#         if len(C) > 0:
#             s = C[0]
#     return L
#
#
# def formaClausal(A):
#     L = []
#     i = 0
#     while(len(A) > 0):
#         # print(A[i])
#         if(A[i] == "Y" or i == len(A) - 1):
#             L.append(Clausula(A[:i]))
#             # L += Clausula(A[:i])
#             A = A[i + 1:]
#             i = 0
#         else:
#             i += 1
#     # for k in L:
#     #     for m in k:
#     #         if(m == "(" or m == ")"):
#     #             k.remove(m)
#                 # k.replace(m, '')
#     return L


def formaClausal(A):
    out = []
    aux = []
    for i in A:
        if(i == "Y"):
            out.append(aux)
            aux = []
        elif(i != "(" and i != ")" and i != "O"):
            aux.append(i)
        else:
            continue
    return out
