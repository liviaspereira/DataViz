from matplotlib import pyplot as plt 

transacoes_blog = []
transacoes_site = []
transacoes_totais = []
usuarios_blog = []


f = open("blog.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    transacoes_blog.append(int(lista[2]))
    transacoes_site.append(int(lista[3]))
    usuarios_blog.append(int(lista[-2]))
    transacoes_totais.append(int(lista[2]) + int(lista[3]))

transacoes_totais = []
for i in range(len(usuarios_blog)):
    transacoes_totais.append(transacoes_blog[i] + transacoes_site[i])

diferençaTB = []
for i in range(len(transacoes_blog)):
    diferençaTB.append(abs(transacoes_totais[i] - transacoes_site[i]))

dias = list(range(1, len(transacoes_blog)+1))


plt.plot(dias, diferençaTB, label='Diferença Transações Blog e Site')

plt.title("DIAS X Diferença Transações Totais")
plt.legend()
plt.xlabel("DIAS")
plt.show()

print(sum(diferençaTB)/len(diferençaTB))
print(sum(transacoes_totais)/sum(diferençaTB))


