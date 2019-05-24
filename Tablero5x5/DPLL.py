def claUnitaria(U):
    flag = False
    posicion = -1
    for i in range(len(U)):
        if(len(U[i]) == 0):
            return (True, False, posicion)
        elif(len(U[i]) == 1):
            flag = True
            posicion = i
            break
    return(False, flag, posicion)

def claUnit(S):
    for i in S:
        if(len(i) == 1):
            return True
    return False

def Compl(l):
    if(l[0] == '-'):
        return l.replace('-', '')
    else:
        return '-' + l

def removeCl(S, l):
    S.remove(l)
    if(len(l) >= 1):
        if(l[0] == '-'):
            L = l.replace('-', '')
        else:
            L = l[0]
        for i in S:
            if L in i:
                S.remove(i)
    return S

def removeCompl(S, l):
    if(len(l) >= 1):
        L = l[0]
        L = Compl(L)
        for i in S:
            if L in i:
                i.remove(L)
    return S

def unitPropagate(S, I):
    vacia, unitaria, posicion = claUnitaria(S)
    while(vacia == False and claUnit(S)):
        for i in S:
            S = removeCl(S, i)
            S = removeCompl(S, i)
            if(len(i) == 0):
                return 'Insatisfacible', I
            if(i[0] == '-'):
                I[Compl(i[0])] = 0
            else:
                I[i[0]] = 1
    # print(S, I)
    return S, I

def lDicc(D):
    I = D.copy()
    for i in I:
        if(i[0] == '-'):
            I.pop(i)
            i = Compl(i)
            if(I.get(i) == 0):
                I[i[0]] = 1
            else:
                I[i[0]] = 0
    return I

def DPLL(S, I):
    S, I = unitPropagate(S, I)
    # print(S,I)
    if(S == "Insatisfacible"):
        return 'Insatisfacible', "{}"
    if(len(S) == 0):
        return 'Satisfacible', lDicc(I)
    for i in S:
        if(len(i) == 0):
            return 'Insatisfacible', "{}"
    L = S[0]
    L = Compl(Compl(L[0]))
    Ip = I.copy()
    if(L[0] == '-'):
        Ip[Compl(L[0])] = 0
    else:
        Ip[L[0]] = 1

    Sp = S.copy()
    Sp.append(L[0])

    aux1, aux2 = DPLL(Sp, Ip)
    if(aux1 == 'Satisfacible'):
        return 'Satisfacible', lDicc(Ip)
    else:
        Spp = S.copy()
        Spp.append(Compl(L[0]))
        Ipp = I.copy()
        if(L[0] == '-'):
            Ipp[Compl(L[0])] = 1
        else:
            Ipp[L[0]] = 0
    return DPLL(Spp, Ipp)

# prueba = [["p", "-q", "r"], ["-p", "q", "-r"], ["-p", "-q", "r"], ["-p", "-q", "-r"]]
# prueba2 = [["p"], ["-p", "q", "-r"], ["q"]]
# prueba3 = [["p"], ["-p", "q"], ["-q", "r", "s"]]
# interpretaciones = {}
# r, int = DPLL(prueba, interpretaciones)
# print(r, int)
