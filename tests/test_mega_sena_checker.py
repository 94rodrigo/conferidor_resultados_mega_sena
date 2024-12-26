import unittest
from unittest.mock import patch, mock_open
from io import StringIO

# Importação das funções do programa principal
from main import contar_acertos, ler_numeros_sorteados, ler_jogos_do_arquivo, conferir_resultados

class TestMegaSenaChecker(unittest.TestCase):

    def test_contar_acertos(self):
        jogo = [1, 2, 3, 4, 5, 6]
        numeros_sorteados = [1, 2, 3, 7, 8, 9]
        self.assertEqual(contar_acertos(jogo, numeros_sorteados), 3)

    @patch('builtins.input', side_effect=["1 2 3 4 5 6"])
    def test_ler_numeros_sorteados(self, mock_input):
        numeros = ler_numeros_sorteados()
        self.assertEqual(numeros, [1, 2, 3, 4, 5, 6])

    def test_ler_jogos_do_arquivo(self):
        conteudo_mock = "1;2;3;4;5;6\n7;8;9;10;11;12\n"
        with patch("builtins.open", mock_open(read_data=conteudo_mock)):
            jogos = ler_jogos_do_arquivo("jogos.txt")
        self.assertEqual(jogos, [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

    def test_ler_jogos_do_arquivo_arquivo_nao_encontrado(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                ler_jogos_do_arquivo("jogos_inexistente.txt")

    def test_ler_jogos_do_arquivo_formato_invalido(self):
        conteudo_mock = "1;2;3;4;5\n7;8;9;10;11;abc\n"
        with patch("builtins.open", mock_open(read_data=conteudo_mock)):
            with self.assertRaises(ValueError):
                ler_jogos_do_arquivo("jogos.txt")

    def test_conferir_resultados(self):
        numeros_sorteados = [1, 2, 3, 4, 5, 6]
        jogos = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [1, 2, 3, 6, 8, 9]]
        resultados = conferir_resultados(numeros_sorteados, jogos)
        self.assertEqual(resultados, [(1, 6), (3, 4)])

    def test_conferir_resultados_jogos_com_15_numeros(self):
        numeros_sorteados = [2, 4, 6, 8, 10, 12]
        jogos = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 4, 6, 8, 10, 13, 14, 15, 16, 17, 18, 20]]
        resultados = conferir_resultados(numeros_sorteados, jogos)
        self.assertEqual(resultados, [(1, 6), (2, 4)])

if __name__ == "__main__":
    unittest.main()
