comunas = ['vina','valpo','quilpue']


def registrarPedido(pedidos):
    cantidad5 = 0
    cantidad15 = 0
    cantidad45 = 0

    nombre = input("Ingrese nombre y apellido del cliente: ")
    while True:
        comuna = input("Ingrese comuna del pedido(vina,valpo o quilpue): ").lower()
        if comuna in comunas:
            break
        else:
            print("Esta comuna no se encuentra en el radio de entrega, intente nuevamente")
    direccion = input("Ingrese direccion del cliente: ")
    while True:
        try:
            tipoCilindro = int(input("Ingrese el tipo de cilindro solicitado (presione 5,15 o 45 y 0 para salir): "))
            if tipoCilindro == 5:
                try:
                    cilindro5 = int(input("Ingrese la cantidad solicitada: "))
                    cantidad5 = cantidad5 + cilindro5
                except:
                    print("Ingrese un dato válido")
            elif tipoCilindro == 15:
                try:
                    cilindro15 = int(input("Ingrese la cantidad solicitada: "))
                    cantidad15 = cantidad15 + cilindro15
                except:
                    print("Ingrese un dato válido")
            elif tipoCilindro == 45:
                try:
                    cilindro45 = int(input("Ingrese la cantidad solicitada: "))
                    cantidad45 = cantidad45 + cilindro45
                except:
                    print("Ingrese un dato válido")
            elif tipoCilindro == 0:
                break
            else:
                print("Escoja una opcion valida, intente nuevamente")
        except:
            print("Ingrese un dato válido")    
            

        pedidos.append({'Cliente' : nombre,
                        'Direccion' : direccion,
                        'Comuna' : comuna,
                        'Cil. 5kg' : cantidad5,
                        'Cil. 15kg' : cantidad15,
                        'Cil. 45kg' : cantidad45}) 

def listarPedidos(pedidos):
    print("Listado de pedidos")
    for pedido in pedidos:
        print(pedido)

def imprimirHojaDeRuta(pedidos):
    while True:
        elegirComuna = input("Ingrese la comuna deseada para imprimir la hoja de ruta: ")

        if elegirComuna in comunas:
            imprimir = []
            for comuna in pedidos:
                if comuna['Comuna'] == elegirComuna:
                    imprimir.append(comuna)
        
            hojaDeRuta = f'HojaDeRuta-{elegirComuna}.txt'

            with open(hojaDeRuta,'w') as archivo:
                archivo.write(f"Lista de pedidos\n") 
                for pedido in imprimir: 
                    archivo.write(f'{pedido}\n') 
            break
        elif elegirComuna == 0:
            break    
        else:
            print("Comuna fuera de rango, intente nuevamente o presione 0 para salir")

