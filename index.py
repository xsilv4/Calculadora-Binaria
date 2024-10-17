def o_binario(num):
    for digit in num:
        if digit not in '01':
            return False
    return True

def numero_d(numero_decimal):
    binario = bin(numero_decimal)[2:]
    hexadecimal = hex(numero_decimal)[2:]
    octal = oct(numero_decimal)[2:]
    return binario,hexadecimal,octal
    

def decimal(numero_binario,numero_octal,numero_hexadecimal):
    
    numero_decimal = int(numero_binario, 2)
    numero_decimal2 = int(numero_octal, 8)
    numero_decimal3 = int(numero_hexadecimal, 16)
    return numero_decimal,numero_decimal2,numero_decimal3

def main():
    print("Escolha uma opção:")
    print("1. Decimal para Binário, Hexadecimal e Octal")
    print("2. Binário, Octal e Hexadecimal para Decimal")
    escolha = input("Opção: ")

    if escolha == '1':
        numero_decimal = int(input("Digite um número decimal: "))
        binario, hexadecimal, octal = numero_d(numero_decimal)

        print("-----------------------------------------------")
        print("RESULTADO DETALHADO:")
        print("Número binário:", binario)
        print("Número hexadecimal:", hexadecimal)
        print("Número octal:", octal)

    elif escolha == '2':
        numero_binario = input("Digite um número binario: ")
        while not o_binario(numero_binario):
            print("Entrada inválida. Por favor, digite apenas 0 e 1.")
            numero_binario = input("Digite um número binario: ")

        numero_octal = input("Digite um número octal: ")
        numero_hexadecimal = input("Digite um número hexadecimal: ")

        numero_decimal, numero_decimal2, numero_decimal3 = decimal(numero_binario, numero_octal, numero_hexadecimal)

        print("-----------------------------------------------")
        print("RESULTADO DETALHADO:")
        print("Número binário para decimal:", numero_decimal)
        print("Número octal para decimal:", numero_decimal2)
        print("Número hexadecimal para decimal:", numero_decimal3)

    else:
        print("Opção inválida.")

main()