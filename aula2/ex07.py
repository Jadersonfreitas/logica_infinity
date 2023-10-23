n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))
n3 = float(input("digite o terceiro numero: "))

if n1 > n2 > n3:
    print(f"O {n1} numero é o maior e o {n3} é o menor")
elif n1 > n3 > n2:
    print(f"O numero {n1} é o maior e o {n2} é o menor")
elif n2 > n1 > n3:
    print(f"O numero {n2} é o maior e o {n3} é o menor")
elif n2 > n3 > n1:
    print(f"O numero {n2} é o maior e o {n1} é o menor")
elif n3 > n1 > n2:
    print(f"O numero {n3} é o maior e o {n2} é o menor")
elif n3 > n2 > n1:
    print(f"O numero {n3} é o maior e o {n1} é o menor")
else:
    print(" os  tres numeros são iguais!")
    