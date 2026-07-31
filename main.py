import csv

def cadastrar_livro(livros):
    """Cadastra um novo livro no dicionário de livros."""
    codigo = input("Digite o código do livro (ex: 001): ")
    if codigo in livros:
        print("Erro: Já existe um livro com este código.")
        return

    titulo = input("Digite o título do livro: ")

    livros[codigo] = {
        "titulo": titulo,
        "situacao": "disponivel",
        "aluno": "",
        "matricula": "",
        "devolucao": ""
    }
    print(f"Livro '{titulo}' cadastrado com sucesso!")


def cadastrar_usuario(usuarios):
    """Cadastra um novo usuário no dicionário de usuários."""
    matricula = input("Digite a matrícula do usuário: ")
    if matricula in usuarios:
        print("Erro: Já existe um usuário com esta matrícula.")
        return

    nome = input("Digite o nome do usuário: ")

    usuarios[matricula] = {
        "nome": nome
    }
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def consultar_livros(livros):
    """Função extra para buscar um livro específico pelo código."""
    codigo = input("Digite o código do livro para consultar: ")
    if codigo in livros:
        livro = livros[codigo]
        print(f"\n--- Dados do Livro ({codigo}) ---")
        print(f"Título: {livro['titulo']}")
        print(f"Situação: {livro['situacao']}")
        if livro['situacao'] == 'emprestado':
            print(f"Aluno: {livro['aluno']} (Matrícula: {livro['matricula']})")
            print(f"Previsão de devolução: {livro['devolucao']}")
    else:
        print("Erro: Livro não encontrado.")


def emprestar_livro(livros, usuarios):
    """Realiza o empréstimo de um livro disponível com validações."""
    codigo = input("Digite o código do livro: ")

    # Validação 1: Verificar se o livro existe
    if codigo not in livros:
        print("Erro: Livro não cadastrado.")
        return

    # Validação 3: Verificar se o livro está disponível
    if livros[codigo]['situacao'] == 'emprestado':
        print("Erro: Este livro já está emprestado.")
        return

    matricula = input("Digite a matrícula do usuário: ")

    # Validação 2: Verificar se o usuário existe
    if matricula not in usuarios:
        print("Erro: Usuário não cadastrado. Realize o cadastro primeiro.")
        return

    data_dev = input("Digite a data prevista de devolução (ex: 10/09/2026): ")

    # Atualizando os dados do livro
    livros[codigo]['situacao'] = 'emprestado'
    livros[codigo]['aluno'] = usuarios[matricula]['nome']
    livros[codigo]['matricula'] = matricula
    livros[codigo]['devolucao'] = data_dev

    print("Empréstimo realizado com sucesso!")


def devolver_livro(livros):
    """Registra a devolução de um livro emprestado."""
    codigo = input("Digite o código do livro para devolução: ")

    # Verifica se o livro existe
    if codigo not in livros:
        print("Erro: Livro não cadastrado.")
        return

    # Validação 4: Verificar se o livro realmente está emprestado antes de devolver
    if livros[codigo]['situacao'] == 'disponivel':
        print("Erro: Este livro já consta como disponível.")
        return

    # Limpando os dados do empréstimo
    livros[codigo]['situacao'] = 'disponivel'
    livros[codigo]['aluno'] = ""
    livros[codigo]['matricula'] = ""
    livros[codigo]['devolucao'] = ""

    print("Devolução registrada com sucesso!")


def gerar_relatorio(livros):
    """Mostra a situação atual dos livros em formato de tabela."""
    print("\n" + "="*95)
    print(f"{'Código':<8} | {'Livro':<30} | {'Situação':<12} | {'Aluno':<15} | {'Matrícula':<10} | {'Devolução'}")
    print("-" * 95)

    if not livros:
        print("Nenhum livro cadastrado no sistema.")
    else:
        for cod, dados in livros.items():
            # Tratando espaços vazios para a tabela ficar alinhada
            aluno = dados['aluno'] if dados['aluno'] else "-"
            matricula = dados['matricula'] if dados['matricula'] else "-"
            devolucao = dados['devolucao'] if dados['devolucao'] else "-"

            print(f"{cod:<8} | {dados['titulo']:<30} | {dados['situacao'].capitalize():<12} | {aluno:<15} | {matricula:<10} | {devolucao}")
    print("="*95 + "\n")


def salvar_csv(livros):
    """Salva os dados dos livros em um arquivo CSV."""
    nome_arquivo = 'relatorio_livros.csv'

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escrevendo o cabeçalho
            writer.writerow(['codigo', 'titulo', 'situacao', 'aluno', 'matricula', 'devolucao'])

            # Escrevendo os dados de cada livro
            for cod, dados in livros.items():
                writer.writerow([
                    cod,
                    dados['titulo'],
                    dados['situacao'],
                    dados['aluno'],
                    dados['matricula'],
                    dados['devolucao']
                ])
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")


def main():
    """Função principal que controla o menu do sistema."""
    livros_db = {}
    usuarios_db = {}

    while True:
        print("\n=== SISTEMA DE EMPRÉSTIMO DE LIVROS ===")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Consultar livros")
        print("4. Emprestar livro")
        print("5. Devolver livro")
        print("6. Gerar relatório")
        print("7. Salvar relatório em arquivo .csv")
        print("8. Sair")

        opcao = input("Escolha uma opção (1-8): ")

        if opcao == '1':
            cadastrar_livro(livros_db)
        elif opcao == '2':
            cadastrar_usuario(usuarios_db)
        elif opcao == '3':
            consultar_livros(livros_db)
        elif opcao == '4':
            emprestar_livro(livros_db, usuarios_db)
        elif opcao == '5':
            devolver_livro(livros_db)
        elif opcao == '6':
            gerar_relatorio(livros_db)
        elif opcao == '7':
            salvar_csv(livros_db)
        elif opcao == '8':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
