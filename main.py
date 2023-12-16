"""
Programa:       Número perfecto
Descripción:    Indica si un número es perfecto
                Un número entero positivo es perfecto si
                es igual a la suma de sus divisores

"""


def es_perfecto(numero): 
    suma_divisores = 1
    divisor = 2
    while divisor < numero / 2:
        if numero % divisor == 0:
            suma_divisores += divisor
        divisor = divisor + 1

    # Fin del bucle while
    
    numero_perfecto = suma_divisores == numero
    return numero_perfecto

# Fin de la función es_perfecto

def main():

    while True:
        print("Cálculo de un número perfecto")
        print("-----------------------------")

        numero = int(input("Introduce un número (0 para terminar): "))

        if numero == 0:
            break

        if es_perfecto(numero):
            print(f"El número {numero} ES perfecto")
        else:
            print(f"El número {numero} NO ES perfecto")


    # Fin del bucle while


if __name__ == '__main__':
    main()
