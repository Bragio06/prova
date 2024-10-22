def desenhar_losango(tamanho):
    # Parte superior
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        simbolos = '%' * (2 * i + 1)
        print(espacos + simbolos)

    # Parte inferior
    for i in range(tamanho - 2, -1, -1):
        espacos = ' ' * (tamanho - i - 1)
        simbolos = '%' * (2 * i + 1)
        print(espacos + simbolos)


def desenhar_triangulo(tamanho):
    for i in range(tamanho):
        espacos = ' ' * (tamanho - i - 1)
        simbolos = '%' * (2 * i + 1)
        print(espacos + simbolos)

 


def main():
    figura = input("Escolha a figura, L para losango e T para triângulo: ")
    
    tamanho = int(input("Informe o tamanho (número de linhas): "))
    
    if figura == "L":
        desenhar_losango(tamanho)
    elif figura == "T":
        desenhar_triangulo(tamanho)
    else:
        print("Figura inválida! Por favor, escolha 'L' ou 'T'.")

main()
