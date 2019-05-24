def EquFNC(A):
    # out = []
    if(len(A) == 4):
        out = ["(", "-" + A[0], "O", "".join(A[2:]), ")", "Y",
               "(", A[0], "O", A[3], ")"]
    elif(len(A) == 7):
        if (A[4] == "Y"):
            out = ["(", A[3], "O", "-" + A[0], ")", "Y",
                   "(", A[5], "O", "-"+ A[0], ")", "Y",
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
    letrasProposicionalesB = []
    for m in range(1, 10):
        letrasProposicionalesB.append("x000" + str(m))
    for m in range(10, 100):
        letrasProposicionalesB.append("x00" + str(m))
    for m in range(100, 1000):
        letrasProposicionalesB.append("x0" + str(m))
    for m in range(1000, 3000):
        letrasProposicionalesB.append("x" + str(m))

    cont = 0
    atomos = letrasProposicionalesA + letrasProposicionalesB

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
            L.append([atomo, "$", "(", v, O, w, ")"])
            cont += 1
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    B = []
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]

    # L.reverse()

    for X in L:
        Y = EquFNC(X)
        B.append("Y")
        for f in Y:
            B.append(f)

    B = [atomo] + B

    return B, cont


def Clausula(C):
    L = []
    s = C[0]
    while(len(C) > 0):
        if(s == "O" or s == "(" or s == ")"):
            C = C[1:]
        else:
            L.append(s)
            C = C[1:]
        if len(C) > 0:
            s = C[0]
    return L


def formaClausal(A):
    L = []
    i = 0
    while(len(A) > 0):
        if(A[i] == "Y" or i == len(A) - 1):
            L.append(Clausula(A[:i]))
            A = A[i + 1:]
            i = 0
        else:
            i += 1

    return L
