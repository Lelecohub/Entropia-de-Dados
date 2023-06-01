import math

def calcular_entropia(probabilidades):
    entropia = 0
    for probabilidade in probabilidades:
        if probabilidade > 0:
            entropia -= probabilidade * math.log2(probabilidade)      
    return entropia

probabilidades = [0.02, 0.614, 0.226, 0.065, 0.042, 0.033]

entropia = calcular_entropia(probabilidades)
print("Entropia dos Dados:", entropia)

n = len(probabilidades)
entropia_maxima = math.log2(n)
print("Entropia Máxima:", entropia_maxima)