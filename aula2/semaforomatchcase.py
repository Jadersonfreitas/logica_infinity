print("Bem vindo ao semaforo digital!")

cor = str(input("Escolha uma cor entre verde, amarelo e vermelho: ")).lower().strip()

match cor:
        case "vermelho":
                print("pare! O sinal está fechado!")
        case "amarelo":
                print("o semaforo está livre pode acelerar!")
        case "verde":
                print("o semaforo está livre pode acelerar!")
        case _:
                print("Deixa de ser burro! Esta cor nao existe no semaforo!")
                