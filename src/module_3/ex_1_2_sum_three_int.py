def sum_three_int():
    """
    Ex 1.2 – Sum three integers provided by the user / Somar três inteiros fornecidos pelo usuário

    Description | Descrição:
    This script asks the user for three integer numbers and prints their sum to the screen.
    Este script solicita ao usuário três números inteiros e imprime a soma deles na tela.

    Author | Autor: João Henrique
    Date | Data: 15/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0
    """

    sum_adders = [int(input(f"Please enter integer #{i + 1}: ")) for i in range(3)]
    print(f"The sum of {sum_adders[0]} + {sum_adders[1]} + {sum_adders[2]} is {sum(sum_adders)}")

if __name__ == "__main__":
    sum_three_int()