

def exibir_cardapio():
    """
    Este código foi gerado com a ajuda do assistente GitHub Copilot.

    Módulo para exibir um cardápio de itens com seus respectivos preços.

    Funções:
    - exibir_cardapio(): Exibe uma lista de itens do cardápio com seus preços formatados.

    Uso:
    Ao executar este script diretamente, a função `exibir_cardapio` será chamada e o cardápio será exibido no console.
    """
    cardapio = {
        "1. Pizza Margherita": 25.00,
        "2. Hambúrguer Clássico": 18.50,
        "3. Salada Caesar": 15.00,
        "4. Suco de Laranja": 7.00,
        "5. Pudim de Leite": 10.00
    }

    print("Cardápio:")
    for item, preco in cardapio.items():
        print(f"{item} - R$ {preco:.2f}")

if __name__ == "__main__":
    exibir_cardapio()
