print("Faça seu cadastro!")
while True:

    nome = str(input("Digite o seu nome: ")).lower()

    if len(nome) < 3:
        print("Nome deve ter no minimo 3 letras.")
    else:
        print("nome valido.")
        break
while True:

    idade = int(input("Qual a sua idade: "))
    if idade == 0:
        print("zero anos? está na barriga da sua mãe?")
    elif idade > 150:
        print("mais de 150 anos? Voce é algum dinossauro?")
    else:
        print("idade cadastrada.")
        break
while True:
    renda = float(input("Qual a sua renda mensal: "))
    if renda == 0:
        print("Voce não tem renda? vá dar calote em outro!")
    else:
        print("renda cadastrada.")
        break
while True:
    sexo = str(input("Qual seu sexo? [M/F]: ")).lower()
    if sexo == "m" or sexo == "f":
        print("Sexo cadastrado")
        break
    else:
        print("M ou F")
while True:
    civil = str(input("Estado civial: [S] p/ Solteiro, [C] p/ Casado, [D] p/ Divorciado, [V] p/ viuvo: ")).lower()
    if civil == "s" or civil == "c" or civil == "d" or civil == "v":
        print("Estado civil cadastrado.")
        break
    else:
        print("Deixa de ser burro, digite S/C/D OU V")