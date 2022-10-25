texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# #Range é uma função built-in do Python, ela é usada para produzir sequência de números inteiros apartir de um ínicio (inclusivo) para um fim (exclusivo) passo a passo. Se usarmos range(i, j) será produzido: i, i+1, i+2, i+3 ... j-1.
#Se informarmos o ínicio sem o fim para a função, por padrão ela irá iniciar de zero.
# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
