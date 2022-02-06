from matplotlib import pyplot as plt 

data = []
transacoes_blog = []
transacoes_site = []
usuarios_blog = []
listamedia = []
listamediaBlog = []
listamediaSite = []
listamediaTotais = []
receita = []


f = open("semoutlier.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    transacoes_blog.append(int(lista[2]))
    data.append(lista[0])
    receita.append(int(lista[1]))
    transacoes_site.append(int(lista[3]))
    usuarios_blog.append(int(lista[-2]))

transacoes_totais = []
for i in range(len(usuarios_blog)):
    transacoes_totais.append(transacoes_blog[i] + transacoes_site[i])
semanas = list(range(1, len(usuarios_blog)+1))


plt.plot(semanas, usuarios_blog, label='Usuários blog')
plt.plot(semanas, transacoes_totais, label='Transacoes totais')
plt.plot(semanas, transacoes_site, label='Transacoes site')
plt.plot(semanas, transacoes_blog, label='Transacoes blog')


plt.title("DIAS X TRANSAÇÕES BLOG E SITE")
plt.legend()
plt.xlabel("DIAS")
plt.show()