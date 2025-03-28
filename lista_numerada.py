import re

def abrir_ler( nome_arquivo):
    try:
        # abrir arquivo e ler o arquivo
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: 
          linhas = arquivo.readlines()
        return linhas 
            
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
    except Exception as e:
        print(f"Erro ao abrir arquivo: {e}")
    return None

def numerar_linhas(linhas):   
    linhas_numeradas = []
    for numero, linha in enumerate(linhas, start=1):
        linhas_numeradas.append ((f"{numero} - {linha}"))
    return linhas_numeradas 

def extrair_palavras(linhas):
    tabela_palavras = {}
    for numero, linha in enumerate(linhas, start=1):
        palavras = re.findall(r'\b\w+\b', linha.lower())
        for palavra in palavras:
            if palavra not in tabela_palavras:
                tabela_palavras[palavra] = set()
            tabela_palavras[palavra].add(numero)
    return tabela_palavras

def imprimir_tabela_referencias(tabela_palavras):
    palavras_ordenadas = sorted(tabela_palavras.keys())
    largura_palavra = max(len(palavra) for palavra in palavras_ordenadas) + 2
    largura_linhas = 1
    # Imprimir o cabeçalho da tabela
    print(f"{'Palavra'.ljust(largura_palavra)} | Linhas")
    print('-' * (largura_palavra + largura_linhas + 9))
    # Imprimir cada palavra e as linhas em que ocorreu
    for palavra in palavras_ordenadas:
        linhas = sorted(tabela_palavras[palavra])  
        linhas_formatadas = ', '.join(map(str, linhas)) 
        print(f"{palavra.ljust(largura_palavra)} | {linhas_formatadas}")
        print('-' * (largura_palavra + largura_linhas + 6))


def main():
 # abrir e ler arquivo txt
    nome_arquivo_numerado = 'teste.txt' 
    linhas = abrir_ler(nome_arquivo_numerado) 
    if linhas is not None:
        linhas_numeradas = numerar_linhas(linhas)
        for linha in linhas_numeradas:
            print( linha, end='')
    print('\n')    
               
 # Tabela de referências cruzadas
    tabela_palavras = extrair_palavras(linhas)
    imprimir_tabela_referencias(tabela_palavras)
    

if __name__ == "__main__":
    main()
