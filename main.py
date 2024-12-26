# Função para calcular o número de acertos entre dois conjuntos de números
def contar_acertos(jogo, numeros_sorteados):
    return len(set(jogo) & set(numeros_sorteados))

# Leitura dos números sorteados
def ler_numeros_sorteados():
    while True:
        try:
            entrada = input("Digite os 6 números sorteados, separados por espaço: ")
            numeros = list(map(int, entrada.split()))
            if len(numeros) != 6:
                raise ValueError("Você deve digitar exatamente 6 números.")
            return numeros
        except ValueError as e:
            print(f"Entrada inválida: {e}")

# Leitura dos jogos do arquivo
def ler_jogos_do_arquivo(nome_arquivo):
    jogos = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                jogo = list(map(int, linha.strip().split(';')))
                jogos.append(jogo)
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    except ValueError:
        raise ValueError("Erro: Certifique-se de que o arquivo contenha apenas números separados por ponto e vírgula.")
    return jogos

# Conferência dos resultados
def conferir_resultados(numeros_sorteados, jogos):
    resultados = []
    for indice, jogo in enumerate(jogos, start=1):
        acertos = contar_acertos(jogo, numeros_sorteados)
        if acertos >= 4:
            resultados.append((indice, acertos))
    return resultados

# Programa principal
def main():
    print("Bem-vindo ao conferidor de resultados da Mega Sena!")

    nome_arquivo = input("Digite o nome do arquivo .txt com os jogos: ")
    jogos = ler_jogos_do_arquivo(nome_arquivo)

    if not jogos:
        print("Nenhum jogo encontrado ou erro ao ler o arquivo.")
        return

    numeros_sorteados = ler_numeros_sorteados()

    resultados = conferir_resultados(numeros_sorteados, jogos)

    if resultados:
        print("\nJogos com 4 acertos ou mais:")
        for indice, acertos in resultados:
            print(f"Linha {indice}: {acertos} acertos")
    else:
        print("\nNenhum jogo obteve 4 acertos ou mais.")

if __name__ == "__main__":
    main()
