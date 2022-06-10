import os.path, glob

print('''
___ _  _    ___ _ ____ _  _ ___  ____ 
 |  |  |     |  | |___ |\ | |  \ |__| 
 |  |__|     |  | |___ | \| |__/ |  |  
                                    0.3
Bienvenido al lugar perfecto para comprar o vender articulos
''')


#=====================================MENU PRINCIPAL=====================================
#menu pricipal
menuPrincipal = {
    1: 'Quieres vender?',
    2: 'Quieres comprar?',
    3: 'Ya tengo una tienda: Ingresar'

}

#menu principal
def print_menuPrincipal():
    for key in menuPrincipal.keys():
         print(key, '--', menuPrincipal[key])

#=====================================////MENU PRINCIPAL===================================


#=====================================LLAMAR EL PRIMER MENU INPUT FROM USER=====================================

#llamar el menu principal
print_menuPrincipal()
#bienvenida
opcionPrincipal = input("Que quieres hacer, Ingresa tu opcion: ")

#=====================================////LLAMAR EL PRIMER MENU INPUT FROM USER==================================


#=====================================MENUS DE COMPRA Y VENTA=====================================


#menu vendedor
menuVendedor = {
    1: 'Agregar producto -(Solo puedes agregar 2 productos)',
    2: 'Opciones de Productos',
    3: 'Ver Estadisticas de mi Tienda',
    4: 'Salir'
}

#menu vendedor
def print_menuVendedor():
    for key in menuVendedor.keys():
        print(key, '--', menuVendedor[key])


#menu vendedor estadisticas
menuVendedor_Estadisticas = {
    1: 'Inventario',
    2: 'Ventas',


}

#menu vendedor estadisticas menu de vendedor primera vez
def print_menuVendedorestadistivas():
    for key in menuVendedor_Estadisticas.keys():
        print(key, '--', menuVendedor_Estadisticas[key])


#menu comprador
menuComprador = {
    1: 'Ver Tiendas',
    2: 'Salir'
}

#menu comprador
def print_menuComprador():
    for key in menuComprador.keys():
        print(key, '--', menuComprador[key])



#menu comprador en tienda
menuComprador_enTienda = {
    1: 'Comprar',
    2: 'Salir'
}


#menu comprador
def print_menuComprador_tienda():
    for key in menuComprador_enTienda.keys():
        print(key, '--', menuComprador_enTienda[key])






#=====================================////MENUS DE COMPRA Y VENTA=================================


#=====================================OPCION  DEL MENU PRICIPAL =====================================

#SELECION
#imprimir menu de vendedor y comprador
if opcionPrincipal == "1":
    print('\nBienvenido Vendedor')
    nombreTienda = input('Ingresa el Nombre de tu tienda: ')
    if os.path.exists(nombreTienda):
        # si el nombre de archivo esta creado, entonces pedir que el usuariuo guarde con otro nombre
        nombreTienda = input("El nombre del archivo ya existe. Ingresa otro nombre: ")
    descripcionTienda = input('Ingresa la descripcion de tu tienda(que vendes): ')
    # comprobar si el nombre del archivo existe o no
    #crear archivo
    with open(nombreTienda+'.txt', 'w') as f:
        f.write("Bienvenido a la tienda de : " + nombreTienda)
        f.write('\n' "Descripcion: " +descripcionTienda + '\n')
    print("\n" + "Nombre de la Tienda : " + nombreTienda + '\n' + "Descripcion: " + descripcionTienda )
    print("Que deseas hacer en la tienda: " + nombreTienda)
    while(True):
        print_menuVendedor()
        opcionVender = input("Escoge tu opcion:")
        if opcionVender == "1":
            with open(nombreTienda+'.txt', 'a') as f:
                f.write("PRODUCTO, PRECIO, CANTIDAD" )



                class Product:
                    def __init__(self, name, value, quantity):
                        self.name = name
                        self.value = value
                        self.quantity = quantity


                # valores para guardar producto
                n = input("\nIngresa el nombre de tu producto:")
                p = input("Ingresa el valor:")
                c = input("Ingresa el cantidad:")

                # producto1 guardado en clase
                producto1 = Product(n, p, c)

                # guardamos los datos de la clase en una lista

                listaproducto1 = []
                listaproducto1.append(producto1.name)
                listaproducto1.append(producto1.value)
                listaproducto1.append(producto1.quantity)

                # nested list, nuestros productos estan dentro de otra lista de todos los productos

                ProductosExistentes = []





                # agregar nuestro producto1 a la lista de productos
                ProductosExistentes.append(listaproducto1)



                f.write("\n"+str(listaproducto1))

                agregarOtroProducto = input("\n Si no agregar un 2do producto ahora, luego al agregar, los productos se seborescribiran \nDeseas agreagar otro producto: S/N?" )
                if agregarOtroProducto.upper() == 'S':
                    # valores para guardar producto
                    n2 = input("\nIngresa el nombre de tu producto:")
                    p2 = input("Ingresa el valor:")
                    c2 = input("Ingresa el cantidad:")

                    # producto2 guardado en clase
                    producto2 = Product(n2, p2, c2)

                    # guardamos los datos de la clase en una lista
                    listaproducto2 = []
                    listaproducto2.append(producto2.name)
                    listaproducto2.append(producto2.value)
                    listaproducto2.append(producto2.quantity)

                    # agregar nuestro producto2 a la lista de productos
                    ProductosExistentes.append(listaproducto2)




                    f.write("\n" + str(listaproducto2))


                elif agregarOtroProducto.upper() == 'N':
                    listaproducto2 = []

        if opcionVender == "2":
            print('Mostrar tienda:')
            # Ver que archivos estan creados
            o1 = int(input("Oprime 1 para ver tu tienda disponible en linea \n Oprime 2 para actualizar tus productos"))
            if o1 == 1:
                os.chdir(r'C:/Users/NW USER/PycharmProjects/tienda0.2/')
                myFiles = glob.glob('*.txt')
                print("Tu tienda: " + str(myFiles))
                # leer el archivo
                read_File = input("Que Tienda tuya quieres ver, ingrea el nombre de la lista sin (''):\n  ")
                f = open(read_File + '.txt', "r")
                file1 = f.readlines()
                count = 0
                # Strips the newline character
                for line in file1:
                    count += 1
                    print("{}: {}".format(count, line.strip()))
                print("\n")
                # open notepad
                #file = 'notepad.exe ' + nombreTienda
                #os.system(file)
                #print("\n")
######################################################################actualizar producto#####################
            if o1 == 2:
                print("\nActualizar")
                # actualizar datos de productos
                cambiar = input('9--actualizar prodcuto')

                if cambiar == '9':
                    print("Cambiar datos de productos:")
                    print('Productos disponibles: ')
                    print("PRODUCTO, PRECIO, CANTIDAD" )
                    for i in ProductosExistentes:
                        print(i)

                    print("\nQue producto deseas cambiar")
                    print("PRODUCTO, PRECIO, CANTIDAD")
                    if listaproducto2 == []:
                        print("1--" + str(listaproducto1))
                    elif not listaproducto2 == []:
                        print("1--" + str(listaproducto1))
                        print("2--" + str(listaproducto2))
                    opcionEditar = input("Ingresa tu opcion: ")

                if (opcionEditar == '1'):
                    print(listaproducto1)
                    print("Que dato deseas cambiar:")
                    edicionSingular = input("1-Nombre, 2-Valor, 3-Cantidad")
                    if edicionSingular == '1':
                        nn = input('Ingresa el nuevo nombre del producto')
                        listaproducto1[0] = nn
                    if edicionSingular == '2':
                        nv = input("Ingresa el nuevo precio")
                        listaproducto1[1] = nv
                    elif edicionSingular == '3':
                        nc = input("ingresa la nueva cantidad")
                        listaproducto1[2] = nc

                if (opcionEditar == '2'):
                    print(listaproducto1)
                    print("Que dato deseas cambiar:")
                    edicionSingular = input("1-Nombre, 2-Valor, 3-Cantidad")
                    if edicionSingular == '1':
                        nn2 = input('Ingresa el nuevo nombre del producto')
                        listaproducto2[0] = nn2
                    if edicionSingular == '2':
                        nv2 = input("Ingresa el nuevo precio")
                        listaproducto2[1] = nv2
                    elif edicionSingular == '3':
                        nc2 = input("ingresa la nueva cantidad")
                        listaproducto2[2] = nc2


                with open(nombreTienda + '.txt', 'w') as f:
                    f.write("Bienvenido a la tienda de : " + nombreTienda)
                    f.write('\n' "Descripcion: " + descripcionTienda)
                    f.write("\n" + str(listaproducto1))
                    f.write("\n" + str(listaproducto2))


                # mostrar producto actualizado
                print('Productos actualizados satisfactoriamente')
                print(listaproducto1)
                if listaproducto2 ==[]:
                    print("\n")
                else:
                    print('Mostrar producto actualizado')
                    print(listaproducto2)

######################################################################////actualizar producto#####################



# ===========================================ESTADISTICAS====================================
        if opcionVender == "3":
            print('Ver estadisticas')
            print_menuVendedorestadistivas()
            oestadisticas = input("Que deseas hacer:")

            if oestadisticas == '1':
               print("Ver inventario")
               print('Total productos:')
               if not listaproducto2:
                   int(producto1.quantity)
                   print("Productos Totales: "+ producto1.quantity)

               else:
                   print("Productos Totales: " +int(producto1.quantity) + int(producto2.quantity))


            elif oestadisticas == '2':
                print("\nVer ventas")


# ===========================================//ESTADISTICAS====================================

# ===========================================VUELVE PRONTO====================================

        elif opcionVender == "4":
           print('Gracias, vuelve pronto')
           exit()

# ===========================================//VUELVE PRONTO====================================


#===========================================COMPRADOR====================================


elif opcionPrincipal == "2":
    print('\nBienvenido Comprador')
    print("Que deseas hacer: Escoge tu opcion")
    print_menuComprador()
    print('Mostrar tienda:')
    # Ver que archivos estan creados
    o1 = int(input("Oprime 1 para ver tus tiendas disponibles"))
    if o1 == 1:
        os.chdir(r'C:/Users/NW USER/PycharmProjects/tienda0.2/')
        myFiles = glob.glob('*.txt')
        print("Tiendas Disponibles: " + str(myFiles))
        # leer el archivo
        read_File = input("Que tIENDA quieres ver? ingrea el nombre de la lista sin (''):\n  ")
        f = open(read_File + '.txt', "r")
        file1 = f.readlines()
        count = 0
        # Strips the newline character
        for line in file1:
            count += 1
            print("{}: {}".format(count, line.strip()))
        print("\n")
        # open notepad
        #file = 'notepad.exe ' + nombreTienda
        #os.system(file)
        #print("\n")

        print_menuComprador_tienda()
        opcionCompra = input("Que deseas hacer?")
        if opcionCompra == '1':
            print("Que producto deseas comprar?")
            f = open(read_File + '.txt', "r")
            file1 = f.readlines()
            last2lines = file1[-2:]
            for line in last2lines:
                count += 1
                print("{}: {}".format(count, line.strip()))
            selecionarCompra = input("Ingreas el nombre del producto que desea comprar:")

# sobre escribir el archivo y luego leer desde el vendedor y acrualizar


        elif opcionCompra == '2':
            print("Hasta luego, Gracias por tu visita!")
            exit()

#===========================================//COMPRADOR====================================

elif opcionPrincipal == "3":
    print("Bueno verte de nuevo")
    os.chdir(r'C:/Users/NW USER/PycharmProjects/tienda0.2/')
    myFiles = glob.glob('*.txt')
    print("Tu tienda: " + str(myFiles))
    # leer el archivo
    read_File = input("Ingrea a tu tienda, ingrea el nombre de la lista sin (''):\n  ")
    f = open(read_File + '.txt', "r")
    file1 = f.readlines()
    count = 0
    # Strips the newline character
    for line in file1:
        count += 1
        print("{}: {}".format(count, line.strip()))
    print("\n")

    optienda = input("Que deseas hacer en tu tienda")



#=====================================////OPCION DEL MENU PRICIPAL =================================





