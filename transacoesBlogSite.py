import numpy as np 
from matplotlib import pyplot as plt 

transacoes_blog = []
transacoes_site = []
data = []

f = open("dadosCOM.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    data.append(lista[0])
    transacoes_blog.append(int(lista[2]))
    transacoes_site.append(int(lista[3]))

listamediaBlog =[]
listamediaSite =[]



for numero in range(int(len(transacoes_blog)/7)+1):
    if len(transacoes_blog[:7]) == 0:
        break
    media = sum(transacoes_blog[:7])/len(transacoes_blog[:7])
    listamediaBlog.append(media)
    for i in range(len(transacoes_blog[:7])):
        del transacoes_blog[0]


for numero in range(int(len(transacoes_site)/7)+1):
    if len(transacoes_site[:7]) == 0:
        break
    media = sum(transacoes_site[:7])/len(transacoes_site[:7])
    listamediaSite.append(media)
    for i in range(len(transacoes_site[:7])):
        del transacoes_site[0]

semanas = list(range(1, len(listamediaBlog)+1))



plt.plot(semanas, listamediaBlog, color='red', label='TRANSAÇÕES BLOG')
plt.plot(semanas, listamediaSite, color='blue', label='TRANSAÇÕES SITE')
plt.title("SEMANAS X TRANSAÇÕES BLOG E SITE")
plt.legend()
plt.xlabel("SEMANAS")
plt.show()

