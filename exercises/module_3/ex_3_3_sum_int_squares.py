from src import clear


def sum_squares_of():
    """
    Ex 1.3
    Sum the squares from three integers provided by the user.
    Somar os quadrados de três inteiros fornecidos pelo usuário.

    Description | Descrição:
    This script requests the user three integers and prints the sum of their
    squares on the screen.
    Este script solicita ao usuário três números inteiros e imprime a soma dos
    quadrados deles na tela.

    Author | Autor: João Henrique
    Date | Data: 15/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.1
    """

    while True:
        try:
            num_list = [
                int(input(
                    f"Please enter integer #{i + 1}: ")) for i in range(3)]
            # Solicita três números inteiros e guarda na variável 'num_list'.
            print(
                f"The sum of {' + '.join(f'{n}²' for n in num_list)} is "
                f"{sum(n ** 2 for n in num_list)}")
            # Imprime na tela a expressão da soma dos inteiros ao quadrado e
            # o resultado.
            break
        except ValueError:
            print(
                "Error: Please enter only integer numbers. Try again."
            )  # Mensagem de erro clara.


if __name__ == "__main__":
    sum_squares_of()
