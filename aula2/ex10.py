print("SEJA BEM VINDO AO SISTEMA!")

turno = str(input("Qual o seu turno? DIGITE [M/T/N]: ")).lower()

match turno:
    case "m":
        print("Tenha um bom dia e bom trabalho!")
    case "t":
        print("Tenha uma boa tarde e bom trabalho!")
    case "n":
        print("Tenha uma ótima noite e um bom trabalho!")
        
    case _:
        print("valor invalido! Digite M para manhã, T para tarde ou N para noite!")  