from Modelos.classes import *


def main():
    base_de_dados = "C:\\Users\\Manha\\OneDrive\\Ambiente de Trabalho\\Curso Python\\Ricardo Mourao\\Aulas Python\\Aulas Python Avancado\\Aulas\\#2 - Pandas - Biblioteca\\imoveis.csv"

    analise = Dados(base_de_dados)
    print('|------------- LER TABELA COMPLETA -------------|')
    print(analise.dados)
    print()

    print('|------------- LER INICIO DA TABELA -------------|')
    print(analise.ler_inicio(15))
    print()

    print('|------------- LER FIM DA TABELA -------------|')
    print(analise.ler_inicio(15))
    print()

    print('|------------- LER TIPO DA TABELA -------------|')
    print(analise.ler_tipo())
    print()

    print('|------------- LER COLUNAS DA TABELA -------------|')
    print(analise.ler_colunas())
    print()

    print('|------------- LER TIPO DADO CABEÇALHO -------------|')
    print(analise.tipo_dado_cabecalho('Cidade'))
    print()

    print('|------------- VER MÉDIA DE RENDAS POR TIPO DE IMÓVEL -------------|')
    print(analise.media_rendas('Tipo', 'Valor'))
    print()

    print('|------------- VER PERCENTAGEM POR TIPO DE IMÓVEL -------------|')
    print(analise.percentagem_por_tipo())
    print()

    print('|------------- MOSTRAR VALORES NULOS -------------|')
    analise.mostrar_valores_nulos()
    print()

    print('|------------- REMOVER VALORES NULOS -------------|')
    print(analise.remover_valores_nulos(0))
    print()

    print('|------------- ECONTRAR VALORES A ZERO -------------|')
    print(analise.encontrar_valores_zero())
    print()

    print('|------------- REMOVER VALORES A ZERO -------------|')
    print(analise.remover_valores_zero())
    print()

    print('|------------- FILTRAR QUARTOS IGUAL A -------------|')
    print(analise.filtro_quarto(1))
    print()

    print('|------------- FILTRAR ALUGUER IGUAL A -------------|')
    print(analise.filtro_aluguer(500))
    print()

    print('|------------- FILTRAR QUARTOS IGUAL A -------------|')
    print(analise.filtro_quarto_aluguer())
    print()

    print('|------------- FILTRAR QUARTOS EXERCICIO -------------|')
    print(analise.filtro_quarto_aluguer2())
    print()

    # analise.guardar('Test123', separador=";")

    print('|------------- CRIAR COLUNA DESPESAS MENSAIS -------------|')
    print(analise.despesas_mensais())
    print()

    print('|------------- CRIAR COLUNA DESPESAS ANUAIS -------------|')
    print(analise.despesas_anuais())
    print()


if __name__ == '__main__':
    main()
