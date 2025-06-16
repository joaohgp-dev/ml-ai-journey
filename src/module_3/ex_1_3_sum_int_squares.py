def sum_squares_of():
    """
    Ex 1.3 – Sum the squares from three integers provided by the user / Somar os quadrados de três inteiros fornecidos pelo usuário

    Description | Descrição:
    This script requests the user three integers and prints the sum of their squares on the screen.
    Este script solicita ao usuário três números inteiros e imprime a soma dos quadrados deles na tela.

    Author | Autor: João Henrique
    Date | Data: 15/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0
    """

    num_list = [int(input(f"Please enter integer #{i + 1}: "))for i in range(3)] # Solicita um número inteiro e guarda o valor do quadrado na variável 'num_list'.
    print(f"The sum of {' + '.join(f'{n}²' for n in num_list)} is {sum(n ** 2 for n in num_list)}") # Imprime na tela a soma dos quadrados dos inteiros e o resultado

if __name__ == "__main__":
    sum_squares_of()