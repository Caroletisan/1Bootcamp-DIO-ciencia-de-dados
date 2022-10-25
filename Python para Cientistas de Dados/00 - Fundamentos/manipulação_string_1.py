#Maiúscula, Minúscula e Título
nome = "pYtHon"

print(nome.upper()) #PYTHON
print(nome.lower()) #python
print(nome.title()) #Python

# Elimina os espaços em branco 
texto = "  Olá mundo!    "

print(texto + ".") #  Olá mundo!    .
print(texto.strip() + ".") #Olá mundo!.
print(texto.rstrip() + ".") #  Olá mundo!.
print(texto.lstrip() + ".") #Olá mundo!    .

menu = "Python"

print("####" + menu + "####") #####Python####
print(menu.center(14)) #    Python    
print(menu.center(14, "#")) ####Python####
print("-".join(menu)) #P-y-t-h-o-n
