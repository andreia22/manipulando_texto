import json

# Tabela de palavras reservadas do Python
TABELA_PYTHON = {
    "palavras_chave": [
        {"simbolo": "False", "tipo": "valor", "descricao": "Valor booleano falso"},
        {"simbolo": "True", "tipo": "valor", "descricao": "Valor booleano verdadeiro"},
        {"simbolo": "None", "tipo": "valor", "descricao": "Representa ausência de valor"},
        {"simbolo": "and", "tipo": "operador", "descricao": "Operador lógico AND"},
        {"simbolo": "or", "tipo": "operador", "descricao": "Operador lógico OR"},
        {"simbolo": "not", "tipo": "operador", "descricao": "Operador lógico NOT"},
        {"simbolo": "if", "tipo": "controle", "descricao": "Estrutura condicional"},
        {"simbolo": "elif", "tipo": "controle", "descricao": "Condicional 'else if'"},
        {"simbolo": "else", "tipo": "controle", "descricao": "Bloco condicional alternativo"},
        {"simbolo": "for", "tipo": "loop", "descricao": "Loop iterativo"},
        {"simbolo": "while", "tipo": "loop", "descricao": "Loop condicional"},
        {"simbolo": "break", "tipo": "controle", "descricao": "Interrompe loop"},
        {"simbolo": "continue", "tipo": "controle", "descricao": "Pula para próxima iteração"},
        {"simbolo": "def", "tipo": "definicao", "descricao": "Define uma função"},
        {"simbolo": "return", "tipo": "controle", "descricao": "Retorna valor de função"},
        {"simbolo": "class", "tipo": "definicao", "descricao": "Define uma classe"},
        {"simbolo": "import", "tipo": "modulo", "descricao": "Importa módulo"},
        {"simbolo": "from", "tipo": "modulo", "descricao": "Importa parte de módulo"},
        {"simbolo": "as", "tipo": "modulo", "descricao": "Alias para importação"},
        {"simbolo": "try", "tipo": "excecao", "descricao": "Bloco de tratamento de exceção"},
        {"simbolo": "except", "tipo": "excecao", "descricao": "Captura exceção"},
        {"simbolo": "finally", "tipo": "excecao", "descricao": "Executa sempre ao final"}
    ],
    "operadores": [
        {"simbolo": "+", "tipo": "aritmetico", "descricao": "Adição"},
        {"simbolo": "-", "tipo": "aritmetico", "descricao": "Subtração"},
        {"simbolo": "*", "tipo": "aritmetico", "descricao": "Multiplicação"},
        {"simbolo": "/", "tipo": "aritmetico", "descricao": "Divisão"},
        {"simbolo": "**", "tipo": "aritmetico", "descricao": "Exponenciação"},
        {"simbolo": "//", "tipo": "aritmetico", "descricao": "Divisão inteira"},
        {"simbolo": "%", "tipo": "aritmetico", "descricao": "Módulo"},
        {"simbolo": "==", "tipo": "comparacao", "descricao": "Igualdade"},
        {"simbolo": "!=", "tipo": "comparacao", "descricao": "Diferença"},
        {"simbolo": ">", "tipo": "comparacao", "descricao": "Maior que"},
        {"simbolo": "<", "tipo": "comparacao", "descricao": "Menor que"},
        {"simbolo": ">=", "tipo": "comparacao", "descricao": "Maior ou igual"},
        {"simbolo": "<=", "tipo": "comparacao", "descricao": "Menor ou igual"}
    ]
}

def pesquisar_simbolo(tabela, termo, case_sensitive=False, por_atributo=None):
    """
    Pesquisa um símbolo na tabela fixa
    
    Args:
        tabela: Dicionário contendo as categorias de símbolos
        termo: Termo a ser pesquisado
        case_sensitive: Se a busca deve diferenciar maiúsculas/minúsculas
        por_atributo: Atributo específico para pesquisar (None para pesquisar pelo símbolo)
    
    Returns:
        Dicionário com os resultados encontrados ou None se não encontrar
    """
    termo = termo if case_sensitive else termo.lower()
    resultados = []
    
    for categoria in tabela.values():
        for item in categoria:
            # Campo principal (símbolo)
            campo_principal = item['simbolo'] if case_sensitive else item['simbolo'].lower()
            
            # Pesquisa pelo símbolo principal
            if por_atributo is None and campo_principal == termo:
                resultados.append(item)
            
            # Pesquisa por atributo específico
            elif por_atributo and por_atributo in item:
                valor_atributo = str(item[por_atributo])
                if not case_sensitive:
                    valor_atributo = valor_atributo.lower()
                if valor_atributo == termo:
                    resultados.append(item)
    
    return resultados[0] if len(resultados) == 1 else resultados or None

def mostrar_resultados(resultados):
    """Exibe os resultados da pesquisa formatados"""
    if resultados is None:
        print("Nenhum resultado encontrado.")
        return
    
    if not isinstance(resultados, list):
        resultados = [resultados]
    
    print("\nRESULTADOS DA PESQUISA:")
    print("=" * 60)
    for item in resultados:
        print(f"Símbolo: {item['simbolo']}")
        print(f"Tipo: {item.get('tipo', 'desconhecido')}")
        print(f"Descrição: {item.get('descricao', 'sem descrição')}")
        print("-" * 60)

def menu_principal():
    """Exibe o menu principal"""
    print("\n=== TABELA DE SÍMBOLOS DO PYTHON ===")
    print("1. Pesquisar por símbolo")
    print("2. Pesquisar por tipo")
    print("3. Pesquisar por descrição")
    print("4. Mostrar todas as palavras-chave")
    print("5. Mostrar todos os operadores")
    print("6. Sair")
    return input("Escolha uma opção: ")

def main():
    """Função principal do programa"""
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            simbolo = input("Digite o símbolo a pesquisar: ")
            resultados = pesquisar_simbolo(TABELA_PYTHON, simbolo)
            mostrar_resultados(resultados)
        
        elif opcao == '2':
            tipo = input("Digite o tipo a pesquisar (ex: 'controle', 'operador'): ")
            resultados = pesquisar_simbolo(TABELA_PYTHON, tipo, por_atributo='tipo')
            mostrar_resultados(resultados)
        
        elif opcao == '3':
            descricao = input("Digite termo para pesquisar na descrição: ")
            resultados = pesquisar_simbolo(TABELA_PYTHON, descricao, por_atributo='descricao')
            mostrar_resultados(resultados)
        
        elif opcao == '4':
            mostrar_resultados(TABELA_PYTHON['palavras_chave'])
        
        elif opcao == '5':
            mostrar_resultados(TABELA_PYTHON['operadores'])
        
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()