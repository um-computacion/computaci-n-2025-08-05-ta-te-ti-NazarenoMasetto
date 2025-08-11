from tateti import Tateti

def main():
    print("Bienvenidos al  Ta Te Ti!")
    juego = Tateti()

    while not juego.juego_terminado:
        
        print("Tablero:")
        print(juego.tablero)
        print("Turno de:", juego.turno)

        try:
            fila = int(input("Ponga la fila (0-2): "))
            columna = int(input("Ponga la columna (0-2): "))
            juego.ocupar_una_de_las_casillas(fila, columna)

        except ValueError:
            print("Error: ingrese un numero valido.")
            continue
        except Exception as error:
            print("Error:", error)
            continue

    print("\n" + "="*20)
    print("Tablero final:")
    print(juego.tablero)
    if juego.ganador == None:
        print("IGUALES")
    else:
        print("GANO", juego.ganador)

if __name__ == "__main__":
    main()
