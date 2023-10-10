print("Bem vindo ao semaforo digital!")

cor = str(input("Escolha uma cor entre verde, amarelo e vermelho: ")).lower().strip()
#.lower() transforma tudo que tiver no input em minusculo!
#.strip() remove todos os espsços antes e depois do texto para evitar erro na leitura.
#upper() transforma tudo escrito no input em maiusculo!


          
if cor == "vermelho":
          print("pare! O sinal está fechado!")
elif cor == "amarelo":
          print("tenha atenção! O sinal ja vai fechar!")
elif cor == "verde":
          print("o semaforo está livre pode acelerar!") 
else:
        print("Deixa de ser burro! Esta cor nao existe no semaforo!")