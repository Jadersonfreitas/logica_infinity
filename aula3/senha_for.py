
print("Sua senha deve ter oito digitos, pelo menos 1 letra maiuscula, 1 minuscula, um numero e 1 caractere especial.")
senha = str(input("Defina a sua senha: "))


alfa_g = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
alfa_p = 'abcdefghijklmnopqrstuvxwyz'
num = '0123456789'
esp = '!@#$%&*-_'
vac = " "

val1 = 0
val2 = 0
val3 = 0
val4 = 0
vazio = False
       

for letra in senha:
    if letra in alfa_p:
        val1 += 1
    elif letra in alfa_g:
        val2 += 1
    elif letra in num:
        val3 =+ 1
    elif letra in esp:
        val4 += 1
    elif letra in vac:
        vazio = True
print(f" Sua senha possui {val1} minusculos, {val2} maiusculo, {val3} numeros e {val4} especiais")

if val1 == 0:
    print("Precisa de 1 caractere minusculo, tente novamente.")
elif val2 == 0:
    print("Precisa de 1 maiusculo, tente novamente.")
elif val3 == 0:
    print("Precisa de 1 numero, tente novamente.")
elif val4 == 0:
    print("Precisa de 1 caractere especial, tente novamente.")
elif len(senha) < 8:
    print("Sua senha precisa de pelo menos 8 caracteres")
elif vazio == True:
    print("Senha não aceita espaços, tente novamente.")


else:
    print("senha cadastrada com sucesso!")

   
