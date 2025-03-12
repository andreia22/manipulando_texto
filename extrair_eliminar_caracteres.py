def abrir_ler_arquivo(nome_arquivo):
    try:
        # abrir arquivo e ler o arquivo
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: 
          conteudo = arquivo.read()
          return conteudo
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
    except Exception as e:
        print(f"Erro ao abrir arquivo: {e}")
    return None

def extrair_caracteres_ascii(nome_arquivo):
    conteudo = abrir_ler_arquivo(nome_arquivo)
    caracteres_ascii = []
    for caractere in conteudo:
        valor_ascii = ord(caractere)
        caracteres_ascii.append(valor_ascii)
    return caracteres_ascii    

def filtra_eliminar_caracteres_indesejados(conteudo, caracteres_indesejados):
    for caractere in caracteres_indesejados:
        conteudo = conteudo.replace(caractere, '')
    return conteudo


def main():
    # Abrir e ler arquivo txt
    nome_arquivo = 'teste.txt'
    conteudo = abrir_ler_arquivo(nome_arquivo)
    if conteudo is not None:
        print("Está escrito: ", conteudo)

    # Extrair caracteres ascii
    print("Os caracteres ascii correspondentes são: ", extrair_caracteres_ascii(nome_arquivo))    

    # filtra e elimina caracteres indesejados
    caracteres_indesejados = [' ', '\t', '\n', '\r', '\x0b', '\x0c']
    conteudo_filtrado = filtra_eliminar_caracteres_indesejados(conteudo, caracteres_indesejados)
    print("Conteudo original: ", conteudo, "Conteudo sem caracteres indesejados: ", conteudo_filtrado)
     
    

if __name__ == "__main__":
    main()
