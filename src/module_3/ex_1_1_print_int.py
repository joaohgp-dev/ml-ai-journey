def print_int():
    """
    Ex 1.1 – Print an integer entered by the user / Imprimir um número inteiro fornecido pelo usuário

    Description | Descrição:
    This script asks the user for an integer number and prints it to the screen.
    Este script solicita ao usuário um número inteiro e o imprime na tela.

    Author | Autor: João Henrique
    Date: 15/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0
    """

    n = int(input("Please enter an integer number: ")) # Solicita um número inteiro e guarda o valor na variável 'n'.
    print(f"You entered: {n}") # Imprime o valor da variável 'n' no console.

if __name__ == "__main__":
    print_int()