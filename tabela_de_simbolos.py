import json

# Tabela inicial com elementos da linguagem Python
TABELA_INICIAL = {
    "palavras_chave": [
        {"simbolo": "if", "tipo": "controle", "descricao": "Condicional se"},
        {"simbolo": "for", "tipo": "loop", "descricao": "Loop iterativo"},
        {"simbolo": "def", "tipo": "definicao", "descricao": "Definir função"},
        {"simbolo": "class", "tipo": "definicao", "descricao": "Definir classe"},
        {"simbolo": "import", "tipo": "modulo", "descricao": "Importar módulo"}
    ],
    "funcoes": [
        {"simbolo": "print()", "tipo": "saida", "descricao": "Imprime na tela"},
        {"simbolo": "len()", "tipo": "analise", "descricao": "Retorna tamanho"},
        {"simbolo": "range()", "tipo": "sequencia", "descricao": "Gera sequência"}
    ],
    "atributos": [
        {"simbolo": "__name__", "tipo": "especial", "descricao": "Nome do módulo"},
        {"simbolo": "__doc__", "tipo": "documentacao", "descricao": "String de documentação"}
    ]
}

# Converter para lista única de símbolos
tabela_simbolos = []
for categoria in TABELA_INICIAL.values():
    tabela_simbolos.extend(categoria)
    
tabela_ordenada = False

def salvar_tabela():
    """Salva a tabela em um arquivo JSON"""
    with open('tabela_simbolos.json', 'w') as f:
        json.dump(tabela_simbolos, f, indent=4)

def carregar_tabela():
    """Carrega a tabela de um arquivo JSON"""
    global tabela_simbolos
    try:
        with open('tabela_simbolos.json', 'r') as f:
            tabela_simbolos = json.load(f)
        print("Tabela carregada com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado, usando tabela padrão.")

def adicionar_simbolo(simbolo, tipo=None, descricao=None):
    """Adiciona novo símbolo à tabela"""
    global tabela_simbolos, tabela_ordenada
    novo_simbolo = {"simbolo": simbolo}
    if tipo:
        novo_simbolo["tipo"] = tipo
    if descricao:
        novo_simbolo["descricao"] = descricao
    
    tabela_simbolos.append(novo_simbolo)
    tabela_ordenada = False
    salvar_tabela()
    print(f"Símbolo '{simbolo}' adicionado com sucesso.")

def buscar_simbolo(simbolo):
    """Busca um símbolo na tabela"""
    for item in tabela_simbolos:
        if item['simbolo'] == simbolo:
            return item
    return None

def ordenar_alfabeticamente():
    """Ordena a tabela alfabeticamente"""
    global tabela_simbolos, tabela_ordenada
    tabela_simbolos.sort(key=lambda x: x['simbolo'])
    tabela_ordenada = True
    salvar_tabela()
    print("Tabela ordenada alfabeticamente.")

def adicionar_atributo(simbolo, chave, valor):
    """Adiciona/atualiza um atributo de um símbolo"""
    item = buscar_simbolo(simbolo)
    if item:
        item[chave] = valor
        salvar_tabela()
        print(f"Atributo '{chave}' adicionado a '{simbolo}'.")
    else:
        print(f"Erro: Símbolo '{simbolo}' não encontrado.")

def remover_simbolo(simbolo):
    """Remove um símbolo da tabela"""
    global tabela_simbolos
    item = buscar_simbolo(simbolo)
    if item:
        tabela_simbolos.remove(item)
        salvar_tabela()
        print(f"Símbolo '{simbolo}' removido.")
    else:
        print(f"Erro: Símbolo '{simbolo}' não encontrado.")

def mostrar_tabela(filtro=None):
    """Mostra a tabela completa ou filtrada"""
    if not tabela_simbolos:
        print("Tabela vazia.")
        return

    print("\nTABELA DE SÍMBOLOS")
    print("="*60)
    print(f"{'Símbolo':<15} | {'Tipo':<15} | {'Descrição/Atributos'}")
    print("="*60)
    
    for item in tabela_simbolos:
        if filtro and not any(filtro in str(v).lower() for v in item.values()):
            continue
            
        simbolo = item.get('simbolo', '')
        tipo = item.get('tipo', '')
        desc = item.get('descricao', '')
        outros = {k:v for k,v in item.items() if k not in ['simbolo', 'tipo', 'descricao']}
        
        print(f"{simbolo:<15} | {tipo:<15} | {desc}")
        if outros:
            print(" "*19 + "| " + ", ".join(f"{k}={v}" for k,v in outros.items()))
    print("="*60)
    if tabela_ordenada:
        print("(Tabela ordenada alfabeticamente)")

def menu():
    print("\n=== TABELA DE SÍMBOLOS PYTHON ===")
    print("1. Mostrar tabela completa")
    print("2. Buscar símbolo")
    print("3. Filtrar tabela")
    print("4. Adicionar símbolo")
    print("5. Adicionar/editar atributo")
    print("6. Remover símbolo")
    print("7. Ordenar alfabeticamente")
    print("8. Sair")
    return input("Escolha uma opção: ")

def main():
    carregar_tabela()
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            mostrar_tabela()
        
        elif opcao == '2':
            simbolo = input("Digite o símbolo: ")
            item = buscar_simbolo(simbolo)
            if item:
                print("\nDETALHES DO SÍMBOLO:")
                for chave, valor in item.items():
                    print(f"{chave}: {valor}")
            else:
                print("Símbolo não encontrado.")
        
        elif opcao == '3':
            termo = input("Digite termo para filtrar: ").lower()
            mostrar_tabela(termo)
        
        elif opcao == '4':
            simbolo = input("Símbolo: ")
            tipo = input("Tipo (opcional): ")
            desc = input("Descrição (opcional): ")
            adicionar_simbolo(simbolo, tipo or None, desc or None)
        
        elif opcao == '5':
            simbolo = input("Símbolo: ")
            chave = input("Atributo: ")
            valor = input("Valor: ")
            adicionar_atributo(simbolo, chave, valor)
        
        elif opcao == '6':
            simbolo = input("Símbolo a remover: ")
            remover_simbolo(simbolo)
        
        elif opcao == '7':
            ordenar_alfabeticamente()
        
        elif opcao == '8':
            print("Salvando e saindo...")
            salvar_tabela()
            break
        
        else:
            print("Opção inválida!")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()