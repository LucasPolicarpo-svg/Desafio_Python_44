def main():
    try:
        num = int(input("Digite um número inteiro que deseja obter os ímpares: "))
        print("Números ímpares de 1 até", num, ":")
        for x in range(1, num + 1):
            if x % 2 != 0:
                print(x, end=" ")
        print()  # Pular uma linha no final
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro.")

if __name__ == "__main__":
    main()
