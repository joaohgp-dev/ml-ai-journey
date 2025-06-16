def high_value():
    """
    Ex 2.1 - Requests two integers and prints the highest. / Solicita dois números inteiros e imprime o maior.

    Description | Descrição:
    This script requests the user two integers and prints the largest.
    Este script solicita ao usuário dois números inteiros e imprime o maior.

    Author | Autor: João Henrique
    Date | Data: 16/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0
    """

    num_list = [int(input(f"Please enter integer #{i + 1}: "))for i in range(2)]
    num_list.sort()
    print(f"The higher value between {num_list[0]} and {num_list[-1]} is: {num_list[-1]}")

if __name__ == "__main__":
    high_value()