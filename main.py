"""
Programa:       Número perfecto
Descripción:    Indica si un número es perfecto
                Un número entero positivo es perfecto si
                es igual a la suma de sus divisores

                Línea añadida para probar git reset
                Línea añadida para probar git reset
                Línea añadida para probar git reset --mixed HEAD - 
                Línea añadida para probar git reset --soft
"""
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
