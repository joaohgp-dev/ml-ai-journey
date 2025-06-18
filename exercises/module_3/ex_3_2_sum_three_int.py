from src import get_valid_int
from src import clear

"""
Ex 3.2
[EN] Sum three integers provided by the user.
[PT] Somar três inteiros fornecidos pelo usuário.

Function | Função: sum_three_int()
Author   | Autor: João Henrique
Date     | Data: 18/06/2025 (DD/MM/YYYY)
Version  | Versão: 1.3
"""


def sum_three_int():
    """
    EN | This script asks the user for three integer numbers and prints their
    sum to the screen.

    PT | Este script solicita ao usuário três números inteiros e imprime a soma
    deles na tela.
    """

    while True:
        # Solicita um número inteiro três vezes e guarda os valores na variável
        # 'user_input'.
        numbers = [get_valid_int(f"Please enter integer #{i + 1}: ") for i
                   in range(3)]
        clear()  # Limpa o conteúdo do terminal
        # Imprime na tela a expressão da soma dos inteiros e o resultado.
        print(f"The sum of {numbers[0]} + {numbers[1]} + "
              f"{numbers[2]} is {sum(numbers)}")
        return


if __name__ == "__main__":
    sum_three_int()
