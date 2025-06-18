import math


def root_of():
    """
    Solicita um número inteiro ao usuário; se for positivo: imprime a raiz
    quadrada; se for negativo: retorna uma mensagem do erro.
    """

    try:
        num = int(input("Please enter an integer number: "))
        print(f"The square root of {num} is {math.sqrt(num)}")
    except ValueError:
        print("Error: ")


if __name__ == "__main__":
    root_of()
