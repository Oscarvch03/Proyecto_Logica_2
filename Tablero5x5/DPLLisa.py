def unitPropagate(clausulas,valorliterales):
    clausulas,valorliterales,estado=helperOfUnitPropagate(clausulas,[],valorliterales)
    return clausulas, valorliterales, estado

def helperOfUnitPropagate(clausulas,clausulasFinales,valorliterales):
    if(clausulas==[]):
        return clausulas,valorliterales,"Satifacible"
    for i in range(len(clausulas)):
        if(len(clausulas[i])<=1):
            if(len(clausulas[i])==0):
                return clausulas,[],"Insatisfacible"
            if(clausulas[i][0][0]!="-"):
                literal=clausulas[i][0];
                literalnegado="-"+literal
            if(clausulas[i][0][0]=="-"):
                literal=clausulas[i][0]
                literalnegado=literal[1:]
            valorliterales.append(literal)
            tmpclausula=[]
            count=-1
            for p in clausulas:
                if(literal not in p):
                    tmpclausula.append(p)
            for s in tmpclausula:
                if(literalnegado in s):
                    count+=1
                    clausulasFinales.append([])
                    for t in s:
                        if(t!=literalnegado):
                            clausulasFinales[count].append(t)
                else:
                    count+=1
                    clausulasFinales.append(s)
            tmp = clausulasFinales.copy();
            clausulasFinales.clear()
            return helperOfUnitPropagate(tmp,clausulasFinales,valorliterales)
    return clausulas,valorliterales,"Indefinido"

def DPLL(clausulas):
    interpretaciones=[]
    final=helperOfDPLL(interpretaciones, clausulas)
    return final

def helperOfDPLL(interpretaciones,clausulas):
    inter=interpretaciones[:len(interpretaciones)-2]
    clausulas, interpretaciones, estado = unitPropagate(clausulas,interpretaciones)
    if(estado=="Indefinido"):
        for i in clausulas:
            for p in i:
                d=p[0]
                if(p[0]=="-"):
                    d=p[1]
                if(d not in interpretaciones and "-"+d not in interpretaciones):
                    literal=[d];
                    clausulas.append(literal)
                    return helperOfDPLL(interpretaciones,clausulas)
    elif(estado=="Satifacible"):
        return "Satisfacible",interpretaciones
    elif(estado=="Insatisfacible"):
        return "Insatisfacible", clausulas
