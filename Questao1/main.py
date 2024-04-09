def dobrar_pares (lista : list[int])-> list[int]:
    """
    Descrição:
    Cria uma lista de números pares multiplicados por 2 a partir de uma lista dada pelo usuário.

    Parâmetros:
    lista (list[int]): Uma lista de numeros inteiros.

    Retorna:
    lista_pares (list[int]) : Uma lista contendo apenas os números pares da lista original multiplicados por 2.
    """
    return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, lista)))