letra = str(input("Digite uma letra: ")).lower()

if len(letra) == 1:
    if letra in "aeiou":
        print("É vogal")
    elif letra in "bcdfghjklmnpqrstvxywz":
        print("É consoante")
    else:
        print("Meu fi, digite uma LETRA, sabe o que é letra?")
else:
    print("Digite só UMAAAAAA letra")
