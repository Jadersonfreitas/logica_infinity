n1 = float(input("Quanoto custa o primeiro item: "))
n2 = float(input("Quanto custa o segundo item: "))
n3 = float(input("Quanto custa o terceiro item: "))

if n1 < n2 and n1 < n3:
    print("O primeiro item é o mais barato!")
elif n2 < n1 and n2 < n3:
    print("O segundo item é o mais barato!")
elif n3 < n1 and n3 < n2:
    print("O terceiro item é o mais barato!")
else:
    print(" os  tres itens possuem o mesmo preço!")
    
