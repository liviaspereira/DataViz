from matplotlib import pyplot as plt 
from scipy.stats import pearsonr, spearmanr

data = []
transacoes_blog = []
transacoes_site = []
usuarios_blog = []
listamedia = []
listamediaBlog = []
listamediaSite = []
listamediaTotais = []
usuarios_site = []
receita = []


f = open("blogsemcopy.csv", "r")
lines = f.readlines()

for line in lines:
    lista = line.split(',')
    transacoes_blog.append(int(lista[2]))
    data.append(lista[0])
    receita.append(int(lista[1]))
    transacoes_site.append(int(lista[3]))
    usuarios_blog.append(int(lista[-2]))
    usuarios_site.append(int(lista[-1]))

acumulado_transacoes_blog = [transacoes_blog[0]]
acumulado_transacoes_totais = [transacoes_blog[0] + transacoes_site[0]]
acumulado_usuarios_blog = [usuarios_blog[0]]
acumulado_usuarios_site = [usuarios_site[0]]

for i in range(1, len(transacoes_blog)):
    acumulado_transacoes_blog.append(transacoes_blog[i] + acumulado_transacoes_blog[-1])
    acumulado_transacoes_totais.append(transacoes_blog[i] + transacoes_site[i] + acumulado_transacoes_totais[-1])
    acumulado_usuarios_blog.append(usuarios_blog[i] + acumulado_usuarios_blog[-1])
    acumulado_usuarios_site.append(usuarios_site[i] + acumulado_usuarios_site[-1])

dias = list(range(1, len(transacoes_blog)+1))

print(spearmanr(acumulado_usuarios_blog, acumulado_transacoes_totais))
print(spearmanr(acumulado_usuarios_site, acumulado_usuarios_blog))


plt.plot(dias, acumulado_usuarios_site, label='Diferença Transações Blog e Site')

plt.title("DIAS X acumulado_usuarios_site")
plt.legend()
plt.xlabel("DIAS")
plt.show()


