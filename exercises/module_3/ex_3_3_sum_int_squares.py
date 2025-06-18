from src import get_valid_int
from src import clear

"""
Ex 3.3
[EN] Sum the squares from three integers provided by the user.
[PT] Somar os quadrados de três inteiros fornecidos pelo usuário.

Function | Função: sum_squares_of()
Author   | Autor: João Henrique
Date     | Data: 18/06/2025 (DD/MM/YYYY)
Version  | Versão: 1.3
"""


def sum_squares_of():
    """
    EN | This script requests the user three integers and prints the sum of
    their squares on the screen.

    PT | Este script solicita ao usuário três números inteiros e imprime a
    soma dos quadrados deles na tela.
    """

    while True:
        # Solicita três números inteiros e guarda na variável 'num_list'.
        numbers = [get_valid_int(f"Please enter integer #{i + 1}: ") for i
                      in range(3)]
        clear()  # Limpa o conteúdo do terminal
        # Imprime na tela a expressão da soma dos inteiros ao quadrado e o
        # resultado.
        print(f"The sum of {' + '.join(f'{n}²' for n in numbers)} is"
              f" {sum(n ** 2 for n in numbers)}")
        return


if __name__ == "__main__":
    sum_squares_of()
