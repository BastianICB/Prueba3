import funciones as fn

pedidos = []


while True:
    print("Bievenidos a gaxplosive")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

    opcion = int(input("Escoja la opcion deseada: "))

    if opcion == 1:
        fn.registrarPedido(pedidos)
    elif opcion == 2:
        fn.listarPedidos(pedidos)
        print("")
    elif opcion == 3:
        fn.imprimirHojaDeRuta(pedidos)
        print("Exitoso\n")
    elif opcion == 4:
        break

    else:
        print("Opcion invalida, intente nuevamente")

    