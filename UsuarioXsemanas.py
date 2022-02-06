from matplotlib import pyplot as plt 


data = []
usuarios_blog = []
f = open("blog.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    data.append(lista[0])
    usuarios_blog.append(int(lista[-2]))


listamedia =[]

for numero in range(int(len(usuarios_blog)/7)+1):
    if len(usuarios_blog[:7]) == 0:
        break
    media = sum(usuarios_blog[:7])/len(usuarios_blog[:7])
    listamedia.append(media)
    for i in range(len(usuarios_blog[:7])):
        del usuarios_blog[0]


semanas = list(range(1, len(listamedia)+1))
semanas = [str(i) for i in semanas]


plt.plot(semanas, listamedia)
plt.title("RELAÇÃO DE USUÁRIOS POR SEMANA")
plt.xlabel("Semanas")
plt.ylabel("Usuarios")
plt.show()

    


