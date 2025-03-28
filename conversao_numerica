# Definições globais
DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
MEMORIA = []

def validar_base(base):
    """Verifica se a base é válida (2 a 64)"""
    return 2 <= base <= 64

def converter_para_decimal(numero_str, base_origem):
    """Converte um número de qualquer base (2-64) para decimal"""
    if not validar_base(base_origem):
        print(f"Erro: Base {base_origem} inválida. Deve ser entre 2 e 64.")
        return None
    
    numero_str = numero_str.strip()
    if not numero_str:
        print("Erro: Número vazio.")
        return None
    
    # Tratamento de sinal
    negativo = numero_str[0] == '-'
    if negativo:
        numero_str = numero_str[1:]
    
    # Conversão
    decimal = 0
    for pos, char in enumerate(numero_str[::-1]):
        try:
            valor = DIGITOS.index(char)
        except ValueError:
            print(f"Erro: Caractere '{char}' inválido para base {base_origem}.")
            return None
        
        if valor >= base_origem:
            print(f"Erro: Dígito '{char}' inválido para base {base_origem}.")
            return None
        
        decimal += valor * (base_origem ** pos)
    
    return -decimal if negativo else decimal

def converter_decimal_para_base(decimal, base_destino, digitos=0, sinal_esquerda=True):
    """Converte um número decimal para qualquer base (2-64) com formatação"""
    if not validar_base(base_destino):
        print(f"Erro: Base {base_destino} inválida. Deve ser entre 2 e 64.")
        return None
    
    # Caso especial para zero
    if decimal == 0:
        return "0".zfill(max(1, digitos))
    
    # Tratamento de sinal
    negativo = decimal < 0
    decimal = abs(decimal)
    
    # Conversão
    resultado = ""
    while decimal > 0:
        resultado = DIGITOS[decimal % base_destino] + resultado
        decimal = decimal // base_destino
    
    # Formatação
    if digitos > 0:
        resultado = resultado.zfill(digitos)
    
    if negativo:
        resultado = "-" + resultado if sinal_esquerda else resultado + "-"
    
    return resultado

def mostrar_memoria():
    """Exibe os valores armazenados na memória"""
    if not MEMORIA:
        print("Memória vazia.")
        return
    
    print("\n--- Valores na Memória (Decimal) ---")
    for i, valor in enumerate(MEMORIA):
        print(f"[{i}] = {valor}")

def menu_principal():
    """Exibe o menu principal"""
    print("\n=== CONVERSOR NUMÉRICO UNIVERSAL ===")
    print("1. Converter para decimal (armazenar)")
    print("2. Converter da memória para outra base")
    print("3. Conversão direta entre bases")
    print("4. Visualizar memória")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    """Função principal do programa"""
    global MEMORIA
    
    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            # Conversão para decimal
            numero = input("\nDigite o número: ").strip()
            base = int(input("Base de origem (2-64): "))
            
            decimal = converter_para_decimal(numero, base)
            if decimal is not None:
                MEMORIA.append(decimal)
                print(f"Valor armazenado: {decimal} (posição {len(MEMORIA)-1})")
        
        elif opcao == "2":
            # Conversão da memória
            if not MEMORIA:
                print("\nMemória vazia!")
                continue
                
            mostrar_memoria()
            try:
                pos = int(input("\nPosição na memória: "))
                if pos < 0 or pos >= len(MEMORIA):
                    print("Posição inválida!")
                    continue
                    
                base = int(input("Base de destino (2-64): "))
                digitos = int(input("Dígitos mínimos (0 para automático): "))
                sinal = input("Sinal à esquerda? (s/n): ").lower() == 's'
                
                resultado = converter_decimal_para_base(
                    MEMORIA[pos],
                    base,
                    digitos,
                    sinal
                )
                
                print(f"\nResultado: {resultado}")
            except ValueError:
                print("Entrada inválida!")
        
        elif opcao == "3":
            # Conversão direta
            numero = input("\nDigite o número: ").strip()
            base_origem = int(input("Base de origem (2-64): "))
            base_destino = int(input("Base de destino (2-64): "))
            
            decimal = converter_para_decimal(numero, base_origem)
            if decimal is not None:
                resultado = converter_decimal_para_base(decimal, base_destino)
                print(f"\nResultado: {resultado}")
        
        elif opcao == "4":
            # Visualizar memória
            mostrar_memoria()
        
        elif opcao == "5":
            # Sair
            print("\nPrograma encerrado.")
            break
        
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    main()