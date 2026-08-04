import os; os.system('cls')
import csv

def ler_dicionario(arquivo_csv, chave_id=0):
    """Lê o arquivo CSV e retorna um dicionário com id: nome.
    chave_id padrão é 0. O nome sempre está na coluna 1"""
    INDICE_NOME = 1
    dicionario = {}
    with open(arquivo_csv, "rt", encoding="utf-8") as arquivo_de_estudantes:
        leitor_de_arquivo = csv.reader(arquivo_de_estudantes)
        next(leitor_de_arquivo) # pula o cabeçalho

        for linha in leitor_de_arquivo:
            id_estudante = linha[chave_id]
            dicionario[id_estudante] = linha[INDICE_NOME]

    return dicionario


def main():
    d_estudante = ler_dicionario("estudantes.csv") # só 1 parâmetro agora

    id = input("Por favor, informe qual o ID do estudante que você deseja saber o nome: ")
    id = id.replace("-", "") # remove os traços

    if id in d_estudante:
        print(f"O nome do aluno é {d_estudante[id]}.")
    elif not id.isdigit():
        print("Número de identificação inválido.")
    elif len(id) < 9:
        print("Número de identificação inválido: dígitos insuficientes.")
    elif len(id) > 9:
        print("Número de identificação inválido: ultrapassa o limite de dígitos.")
    else:
        print("Estudante inexistente.")


if __name__ == "__main__":
    main()