from matplotlib import pyplot as plt 
import numpy as np
import math

data = []
receitas = []
usuarios_blog = []


f = open("sozero.csv", "r")
lines = f.readlines()

receita_real = []
f2 = open("dadosreais.csv", "r")
lines2 = f2.readlines()
for line in lines2:
    lista = line.split(',')
    receita_real.append(int(lista[1]))

for line in lines:
    lista = line.split(',')
    receitas.append(int(lista[1]))
    data.append(lista[0])
    usuarios_blog.append(int(lista[-1]))

acumulado_receitas = [receitas[0]]
acumulado_usuarios_blog = [usuarios_blog[0]]

for i in range(1, len(receitas)):
    acumulado_receitas.append(receitas[i] + acumulado_receitas[-1])
    acumulado_usuarios_blog.append(usuarios_blog[i] + acumulado_usuarios_blog[-1])

acumulado_receita_real = [receita_real[0]]
for i in range(len(receita_real)):
    acumulado_receita_real.append(receita_real[i] + acumulado_receita_real[-1])

dias = list(range(1, len(usuarios_blog)+1))

x = np.array(dias) 
y = np.array(acumulado_receitas) 
plt.plot(x, y, 'bo', label='Receita Acumulada Real Antes do Blog')
plt.xlabel("Dias", fontsize = 15)
plt.ylabel("Receita", fontsize = 15)
plt.legend()
plt.show()  

def estimate_coef(x, y): 
    # número de observações/pontos
    n = np.size(x) 
  
    # médias de x e y
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calcula os coeficientes de regressão
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 

# função para mostrar os dados e o ajuste linear
def plot_regression_line(x, y, b): 
    # mostra os dados
    plt.scatter(x, y, color = "b", marker = "o", s = 50) 
  
    # prediz os valores
    y_pred = b[0] + b[1]*x 
  
    # mostra a reta de regressão
    plt.plot(x, y_pred, color = "r", label='Regressão Linear')
    plt.plot(x, y, 'bo', label='Receita Acumulada Real Antes do Blog')
    
  
    plt.xlabel('Dias') 
    plt.ylabel('Receita Acumulada') 
    plt.title("Regressão Linear da Receita Acumulada")
    plt.legend()
    plt.show() 


# estima os coeficientes
b = estimate_coef(x, y) 
print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1])) 
  
# mostra o ajuste linear
plot_regression_line(x, y, b) 

#funcao que calcula o RSE
def RSE(x,y,b):
    n = len(y)
    RSE = 0
    for i in range(0,n):
        y_pred = b[0]+ x[i]*b[1] # valor predito
        RSE = RSE + (y[i]-y_pred)**2
    RSE = math.sqrt(RSE/(n-2))
    return RSE
print('RSE:', RSE(x,y,b))

def R2(x,y,b):
    n = len(y)
    c1 = 0
    c2 = 0
    ym = np.mean(y)
    for i in range(0,n):
        y_pred = b[0]+ x[i]*b[1] # valor predito
        c1 = c1 + (y[i]-y_pred)**2
        c2 = c2 + (y[i]-ym)**2
    R2 = 1 - c1/c2
    return R2

print('R2:', R2(x,y,b))

def predicao(x,b):
    y_pred = b[0]+ x*b[1]
    return y_pred

print(f"predição: {predicao(639,b)}")
total_real = acumulado_receita_real[-1]
print(f"total real: {total_real}")

diferenca = abs(total_real - predicao(639,b))
porcentagem = (diferenca/total_real)*100
print(f"diferença: {diferenca}, porcentagem: {porcentagem}")