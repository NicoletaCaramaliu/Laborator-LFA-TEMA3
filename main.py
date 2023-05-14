f=open("gramatica.txt","r")
n=int(f.readline())
#retinem gramatica sub forma de dictionar- cheile sunt literele mari
gramatica={}
linie=f.readline().split()
while linie!=[]:
    gramatica[linie[0]]=[]
    for i in range(1,len(linie)):
        gramatica[linie[0]].append(linie[i])
    linie=f.readline().split()
print(gramatica)


#cautam literele(cheile din dictionare) ce au simboluri terminale
terminale=[]
for litera in gramatica:
    for stare in gramatica[litera]:
        if stare=='l' or (len(stare)==1 and stare.islower):
            terminale.append(litera)

print(terminale)

#cream o lista in care vom retine toate cuvintele de lungime n, iar apoi verificam daca sunt acceptate
#initial vom avea in lista cuvinte ['aA','dE'] deoarece doar de aici pot proni cuvintele gramaticii, iar apoi
#adaugam pe rand continuarile posibile(la 'aA' punem in locul literei A elementele din lista corespunzatoare cheii A)
cuvinte=[]
for litera in gramatica['S']:
    cuvinte.append(litera)
print(*cuvinte)
l=1
while l<n:
    continuare = []
    for cuvant in cuvinte:
        if(cuvant[-1]!='l' and cuvant[-1].isupper()):
            for litera in gramatica[cuvant[-1]]:
                continuare.append(cuvant[:len(cuvant)-1]+litera)
    cuvinte=continuare
    l=l+1

print(cuvinte)


cuvinteLungimeN=[]
for cuvant in cuvinte:
    if cuvant[-1] in terminale:
        cuvinteLungimeN.append(cuvant[:len(cuvant)-1])
    if cuvant[-1].islower() and cuvant[-1]!='l':
        cuvinteLungimeN.append(cuvant)
print(cuvinteLungimeN)