alternativa = str(input("você deseja sir? S/N ")).lower()

if alternativa == "s" or alternativa == "n":
    print("Operação válida")
    if alternativa == "s":
     print("Vai timbora, carniça!")
    else:
     print("Continue usando o programa")
    

else:
    print("Operação inválida")
