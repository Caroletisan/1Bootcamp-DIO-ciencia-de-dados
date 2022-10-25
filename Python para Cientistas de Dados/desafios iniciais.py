#Duas torres
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

ICM = (distancia / (diametro1 + diametro2))

print(f"{ICM:.2f}")


#Cachorro quente
cachorro_quentes_consumidos = 10
participantes = 90

media = cachorro_quentes_consumidos / participantes

print(f"{media:.2f}")



#Viagem
def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

valores = input().split()

# declare constants
RENDIMENTO = 12 #RENDIMENTO EM km/L

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

tempo_de_viagem = int(valores[0])
velocidade_media = int(valores[1])

distancia_percorrida = tempo_de_viagem * velocidade_media
combustivel_gasto = truncate( (distancia_percorrida / RENDIMENTO),3)
print(f"{combustivel_gasto:.3f}")