letra = str(input("Digite uma letra: ")).lower()

if len(letra) == 1:
    if letra in "aeiou":
        print("É vogal")
    elif letra in "qwrtypsdfghjklçzxcvbnm":
        print("É consoante")
    else:
        print("Meu fi, digite uma LETRA, sabe o que é letra?")
else:
    print("Voce num sabe o que é UMA não seu animal? É só UMAAAAAA letra!")