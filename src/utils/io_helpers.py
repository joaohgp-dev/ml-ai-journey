import os


def clear():
    """
    Clear the terminal screen (cross-platform).
    Limpa a tela do terminal (multi-plataforma).

    Author | Autor: João Henrique
    Date: 16/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0
    """

    if os.getenv("TERM") is not None:
        # Verifica o SO e executa o respectivo comando CLI que limpa o
        # terminal.
        os.system("cls" if os.name == "nt" else "clear")
    else:
        # Se não estiver em um ambiente compatível, apenas pula 20 linhas.
        print("\n" * 20)


def get_valid_int(prompt: str) -> int:
    """
    Prompt the user until a valid integer is entered.
    Solicita um número inteiro ao usuário até que um valor válido seja
    informado.

    Author | Autor: João Henrique
    Date: 16/06/2025 (DD/MM/YYYY)
    Versão | Version: 1.0

    Args:
        prompt (str): A mensagem exibida para o usuário.

    Returns:
        int: O valor inteiro fornecido.
    """

    while True:
        clear()  # Limpa o terminal.
        # Imprime uma mensagem personalizada e guarda o valor informado na
        # variável 'user_input'.
        user_input = input(prompt)
        try:
            # Retorna o valor de 'user_input' caso seja um inteiro válido.
            return int(user_input)
        except ValueError:
            # Imprime uma mensagem de erro informando o termo inválido e
            # incentivando o usuário à uma nova tentativa.
            input(f"Error: '{user_input}' is not a valid integer."
                  f"\nPress ENTER to try again.")
