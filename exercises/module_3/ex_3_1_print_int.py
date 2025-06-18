from src import get_valid_int


# Exercise 1.1:
# Print an integer entered by the user.
# Imprimir um número inteiro fornecido pelo usuário.

def print_int():
    """
    This script asks the user for an integer number and prints it to the
    screen.
    Este script solicita ao usuário um número inteiro e o imprime na tela.

    Author | Autor: João Henrique
    Date: 16/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.2
    """

    while True:
        # Solicita um número inteiro e guarda o valor na variável 'user_input'.
        user_input = get_valid_int("Please enter an integer number: ")
        print(f"You entered: {user_input}")
        return user_input


if __name__ == "__main__":
    print_int()
