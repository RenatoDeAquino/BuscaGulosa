a = [2,"B",36,"C",61]
b = [2,"A",36,"D",31]
c = [4,"A",61,"D",32,"F",31,"L",80]
d = [3,"B",31,"C",32,"E",52]
e = [2,"D",52,"G",43]
f = [3,"C",31,"K",112,"J",122]
g = [2,"E",43,"H",40]
h = [2,"G",40,"I",40]
i = [2,"H",40,"J",45]
j = [3,"I",45,"F",122,"K",36]
k = [3,"J",36,"F",112,"M",32]
l = [2,"C",80,"M",102]

distancia = ["A",223,"B",222,"C",166,"D",192,"E",165,"F",136,"G",122,"H",111,"I",100,"J",60,"K",32,"L",102]


node_atual = None
node_path = []
custo = 0
topzera_1 = 0
topzera_2 = 0
topzera_3 = 0
topzera_4 = 0
node_atual = input("Digite o node do qual deseja comecar: ")
node_path.append(node_atual)

while node_atual.upper() != "M":
    if node_atual.upper() == "A":
        for x in range(0,len(a)):
            if a[x] == "B":
                topzera_1 = distancia[3]
            if a[x] == "C":
                topzera_2 = distancia[5]
        if topzera_1 > topzera_2:
            node_path.append("C")
            node_atual = "c"
        else:
            node_path.append("B")
            node_atual = "b"
#____________________________________________________________
    if node_atual.upper() == "B":
        for x in range(0,len(b)):
            if b[x] == "A":
                topzera_1 = distancia[3]
                print(topzera_1)
            if b[x] == "D":
                topzera_2 = distancia[7]
                print(topzera_2)
        if topzera_1 > topzera_2:
            node_path.append("D")
            node_atual = "d"
        else:
            node_path.append("A")
            node_atual = "a"
#______________________________________________________________________________
    if node_atual.upper() == "C":
        for x in range(0,len(c)):
            if c[x] == "A":
                topzera_1 = distancia[1]
            if c[x] == "D":
                topzera_2 = distancia[7]
            if c[x] == "F":
                topzera_3 = distancia[11]
            if c[x] == "L":
                topzera_4 = distancia[23]
        if topzera_1 < topzera_2 and topzera_1 < topzera_3 and topzera_1 < topzera_4:
            node_path.append("A")
            node_atual = "a"
        if topzera_2 < topzera_1 and topzera_2 < topzera_3 and topzera_2 < topzera_4:
            node_path.append("D")
            node_atual = "d"
        if topzera_3 < topzera_1 and topzera_3 < topzera_2 and topzera_3 < topzera_4:
            node_path.append("F")
            node_atual = "f"
        if topzera_4 < topzera_1 and topzera_4 < topzera_2 and topzera_4 < topzera_3:
            node_path.append("L")
            node_atual = "l"
#______________________________________________________________________________
    if node_atual.upper() == "D":
        for x in range(0,len(d)):
            if d[x] == "B":
                topzera_1 = distancia[3]
            if d[x] == "C":
                topzera_2 = distancia[5]
            if d[x] == "E":
                topzera_3 = distancia[9]
        if topzera_1 < topzera_2 and topzera_1 < topzera_3:
            node_path.append("B")
            node_atual = "b"
        if topzera_2 < topzera_1 and topzera_2 < topzera_3:
            node_path.append("C")
            node_atual = "c"
        if topzera_3 < topzera_1 and topzera_3 < topzera_2:
            node_path.append("E")
            node_atual = "e"
#______________________________________________________________________________
    if node_atual.upper() == "E":
        for x in range(0,len(e)):
            if e[x] == "D":
                topzera_1 = distancia[7]
            if e[x] == "G":
                topzera_2 = distancia[13]
        if topzera_1 > topzera_2:
            node_path.append("G")
            node_atual = "g"
        else:
            node_path.append("D")
            node_atual = "d"
#______________________________________________________________________________
    if node_atual.upper() == "F":
        for x in range(0,len(f)):
            if f[x] == "C":
                topzera_1 = distancia[5]
            if f[x] == "K":
                topzera_2 = distancia[21]
            if f[x] == "J":
                topzera_3 = distancia[19]
        if topzera_1 < topzera_2 and topzera_1 < topzera_3:
            node_path.append("C")
            node_atual = "c"
        if topzera_2 < topzera_1 and topzera_2 < topzera_3:
            node_path.append("K")
            node_atual = "k"
        if topzera_3 < topzera_1 and topzera_3 < topzera_2:
            node_path.append("J")
            node_atual = "j"
#______________________________________________________________________________
    if node_atual.upper() == "G":
        for x in range(0,len(g)):
            if g[x] == "E":
                topzera_1 = distancia[9]
            if b[x] == "H":
                topzera_2 = distancia[15]
        if topzera_1 > topzera_2:
            node_path.append("H")
            node_atual = "h"
        else:
            node_path.append("E")
            node_atual = "e"
#______________________________________________________________________________
    if node_atual.upper() == "H":
        for x in range(0,len(h)):
            if h[x] == "G":
                topzera_1 = distancia[13]
            if h[x] == "I":
                topzera_2 = distancia[17]
        if topzera_1 > topzera_2:
            node_path.append("I")
            node_atual = "i"
        else:
            node_path.append("G")
            node_atual = "g"
#______________________________________________________________________________
    if node_atual.upper() == "I":
        for x in range(0,len(i)):
            if i[x] == "H":
                topzera_1 = distancia[15]
            if i[x] == "J":
                topzera_2 = distancia[19]
        if topzera_1 > topzera_2:
            node_path.append("J")
            node_atual = "j"
        else:
            node_path.append("H")
            node_atual = "h"
#______________________________________________________________________________
    if node_atual.upper() == "J":
        for x in range(0,len(j)):
            if j[x] == "I":
                topzera_1 = distancia[17]
            if j[x] == "F":
                topzera_2 = distancia[11]
            if j[x] == "K":
                topzera_3 = j[x + 1]
        if topzera_1 < topzera_2 and topzera_1 < topzera_3:
            node_path.append("I")
            node_atual = "i"
        if topzera_2 < topzera_1 and topzera_2 < topzera_3:
            node_path.append("F")
            node_atual = "f"
        if topzera_3 < topzera_1 and topzera_3 < topzera_2:
            node_path.append("K")
            node_atual = "k"
#______________________________________________________________________________
    if node_atual.upper() == "K":
        for x in range(0,len(k)):
            if k[x] == "J":
                topzera_1 = distancia[19]
            if k[x] == "F":
                topzera_2 = distancia[11]
            if k[x] == "M":
                topzera_3 = 0
        if topzera_1 < topzera_2 and topzera_1 < topzera_3:
            node_path.append("J")
        if topzera_2 < topzera_1 and topzera_2 < topzera_3:
            node_path.append("F")
            node_atual = "f"
        if topzera_3 < topzera_1 and topzera_3 < topzera_2:
            node_path.append("M")
            node_atual = "m"
#______________________________________________________________________________
    if node_atual.upper() == "L":
        for x in range(0,len(l)):
            if l[x] == "C":
                topzera_1 = distancia[5]
            if l[x] == "M":
                topzera_2 = 0
        if topzera_1 > topzera_2:
            node_path.append("M")
            node_atual = "m"
        else:
            node_path.append("C")
            node_atual = "c"
#______________________________________________________________________________
print(node_path)