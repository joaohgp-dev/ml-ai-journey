from src import clear


def sum_three_int():
    """
    Ex 1.2
    Sum three integers provided by the user.
    Somar três inteiros fornecidos pelo usuário.

    Description | Descrição:
    This script asks the user for three integer numbers and prints their sum to
    the screen.
    Este script solicita ao usuário três números inteiros e imprime a soma
    deles na tela.

    Author | Autor: João Henrique
    Date | Data: 15/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.1
    """

    while True:
        clear()  # Limpa o terminal.
        # Solicita um número inteiro três vezes e guarda os valores na variável
        # 'user_input'.
        user_input = [input(f"Please enter integer #{i + 1}: ")for i in
                      range(3)]
        try:
            # Salva os elementos de 'user_input' como inteiros na variável
            # 'sum_adders'.
            sum_adders = [int(element)for element in user_input]
        except ValueError:
            clear()  # Limpa o terminal.
            # Mensagem de erro clara
            input(f"Error: '{user_input}' is not a valid integer."
                  f"\nPress ENTER Try again.")
        else:
            # Imprime na tela a expressão da soma dos inteiros e o resultado.
            print(f"The sum of {sum_adders[0]} + {sum_adders[1]} + "
                  f"{sum_adders[2]} is {sum(sum_adders)}")
            break

if __name__ == "__main__":
    sum_three_int()
