# Conferidor de Resultados da Mega Sena

Este é um programa em Python que confere os resultados de jogos da Mega Sena a partir de números sorteados fornecidos pelo usuário e jogos armazenados em um arquivo `.txt`. O programa exibe as linhas que possuem 4 ou mais acertos e a quantidade de acertos em cada uma dessas linhas.

## Funcionalidades
- **Leitura dos números sorteados**: Permite que o usuário insira os 6 números sorteados.
- **Leitura dos jogos**: Lê jogos de um arquivo `.txt`, onde cada linha contém 6 números separados por ponto e vírgula (`;`).
- **Conferência dos resultados**: Verifica os acertos de cada jogo em relação aos números sorteados.
- **Exibição dos resultados**: Mostra as linhas com 4 ou mais acertos e o número de acertos em cada uma.

## Pré-requisitos
- Python 3.6 ou superior.
- Um arquivo `.txt` com os jogos, no formato especificado abaixo.

## Formato do Arquivo de Jogos
Cada linha do arquivo deve conter 6 números ou mais, separados por ponto e vírgula (`;`). Por exemplo:
```
1;2;3;4;5;6
7;8;9;10;11;12
2;4;6;8;10;12
1;3;5;7;9;11
```

## Como Usar
1. Clone este repositório ou copie o código do programa.
2. Crie um arquivo `.txt` contendo os jogos no formato especificado.
3. Execute o programa.

### Executando o Programa
No terminal, execute o seguinte comando:
```bash
python main.py
```

Siga as instruções:
1. Insira o nome do arquivo `.txt` contendo os jogos.
2. Insira os 6 números sorteados, separados por espaço.
3. O programa exibirá os resultados.

### Exemplo de Execução
Entrada:
```
Digite o nome do arquivo .txt com os jogos: jogos.txt
Digite os 6 números sorteados, separados por espaço: 1 2 3 4 5 7
```

Saída:
```
Jogos com 4 acertos ou mais:
Linha 1: 5 acertos
```

## Tratamento de Erros
- **Arquivo não encontrado**: Verifica se o arquivo `.txt` existe e exibe uma mensagem de erro caso não seja encontrado.
- **Formato inválido**: Garante que cada linha do arquivo contenha apenas números separados por `;`.
- **Entrada de números sorteados**: Valida que o usuário insira exatamente 6 números.

## Licença
Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.
