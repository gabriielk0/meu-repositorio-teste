palavra = input("Insira uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra é um Palíndromo")
else:
    print("A palavra não é um Palíndromo")