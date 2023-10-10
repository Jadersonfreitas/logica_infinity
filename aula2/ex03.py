letra = str(input("digite seu sexo [M/F]: ")).lower()

match letra:
    case "f":
       print("F - Seu sexo é feminino")
    case "m":
        print("M - Seu sexo é masculino")
    case _:
        print("alternativa invalida! Digite F ou M!")

 # ou temos que colocar .lower() para diminuir tudo e funcionar maiusculo ou minusculo
 # ou colocamos as duas possibilidades dentro de um conjunto e ficaria:
 #  if letra in "Ff" ou if letra in "mM".       
