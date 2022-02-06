from matplotlib import pyplot as plt 

data = []
transacoes_blog = []
transacoes_site = []
usuarios_blog = []
listamedia = []
listamediaBlog = []
listamediaSite = []
listamediaTotais = []


f = open("dadosCOM.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    transacoes_blog.append(int(lista[2]))
    data.append(lista[0])
    transacoes_site.append(int(lista[3]))
    usuarios_blog.append(int(lista[-2]))

for numero in range(int(len(transacoes_blog)/7)+1):
    if len(transacoes_blog[:7]) == 0:
        break
    media = sum(transacoes_blog[:7])/len(transacoes_blog[:7])  #lista de MEDIAS DO BLOG
    listamediaBlog.append(media)
    for i in range(len(transacoes_blog[:7])):
        del transacoes_blog[0]


for numero in range(int(len(transacoes_site)/7)+1):
    if len(transacoes_site[:7]) == 0:
        break
    media = sum(transacoes_site[:7])/len(transacoes_site[:7])  #lista de MEDIAS DO SITE
    listamediaSite.append(media)
    for i in range(len(transacoes_site[:7])):
        del transacoes_site[0]

for i in range(len(listamediaBlog)):
    listamediaTotais.append(listamediaBlog[i]+listamediaSite[i])

for numero in range(int(len(usuarios_blog)/7)+1):
    if len(usuarios_blog[:7]) == 0:
        break
    media = sum(usuarios_blog[:7])/len(usuarios_blog[:7])   #lista de MEDIAS DE USUARIOS BLOG
    listamedia.append(media)
    for i in range(len(usuarios_blog[:7])):
        del usuarios_blog[0]

semanas = list(range(1, len(listamediaTotais)+1))

plt.plot(semanas, listamediaTotais, color='red', label='TRANSAÇÕES BLOG E SITE')
plt.plot(semanas, listamedia, color='blue', label='USUARIOS BLOG')
plt.title("USUÁRIOS X TRANSAÇÕES BLOG E SITE EM RELAÇÃO A SEMANAS")
plt.legend()
plt.xlabel("DIAS")
plt.show()

