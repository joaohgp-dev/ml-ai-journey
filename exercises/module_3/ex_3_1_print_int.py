from src import get_valid_int
from src import clear

"""
Ex 3.1
[EN] Print an integer entered by the user.
[PT] Imprimir um número inteiro fornecido pelo usuário.

Function | Função: print_int()
Author   | Autor: João Henrique
Date     | Data: 18/06/2025 (DD/MM/YYYY)
Version  | Versão: 1.3
"""


def print_int():
    """
    EN | This script asks the user for an integer number and prints it to the
    screen.

    PT | Este script solicita ao usuário um número inteiro e o imprime na tela.
    """

    while True:
        # Solicita um número inteiro e guarda o valor na variável 'user_input'.
        user_input = get_valid_int("Please enter an integer number: ")
        clear()  # Limpa o conteúdo do terminal
        # Imprime uma mensagem com o número inteiro informado.
        print(f"You entered: {user_input}")
        return


if __name__ == "__main__":
    print_int()
