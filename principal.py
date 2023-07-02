from cliente import Cliente
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def exportar_boleta(venta: Venta):
    c = canvas.Canvas("boleta.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, 720, "EMPRESA COMERCIAL SOLSITO ")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 650, "Cliente:")
    c.setFont("Helvetica", 12)
    c.drawString(150, 650, venta.cliente.razon_social)
    c.drawString(150, 630, venta.cliente.direccion)
    c.drawString(150, 610, venta.cliente.telefono)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 570, "Lista de Compras:")
    c.setFont("Helvetica", 12)
    y = 550
    for detalle in venta.detalle:
        c.drawString(150, y, f"{detalle.descripcion}: {detalle.cantidad} x {detalle.precio_unitario}")
        y -= 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(450, 570, f"Total: {venta.total},")
    c.drawString(450, 650, f"Fecha: {fecha_actual}")
    
    c.save()
    print("La boleta ha sido exportada exitosamente.")


def obtener_fecha_actual():
    global fecha_actual
    fecha_actual = date.today()
    print(fecha_actual)

# CRUD CLIENTE
data_clientes:list=[{"numero_documento":"1",
                     "razon_social":"Anthony Kelman Mamani Vargas",
                     "direccion":"Jr. Ayaviri 290",
                     "telefono":"913777376"},
                     {"numero_documento":"00000000002",
                     "razon_social":"Denis Wilber",
                     "direccion":"Jr. Tupac yupanqui 590",
                     "telefono":"997120432"},
                     {"numero_documento":"00000000003",
                     "razon_social":"Juan Carlos ",
                     "direccion":"Jr. Tupac yupanqui 790",
                     "telefono":"997120440"}]

clientes:Cliente = []
def cargar_datos_clientes():
    for data in data_clientes:
        clientes.append(Cliente(data["numero_documento"],
                                data["razon_social"],
                                data["direccion"],
                                data["telefono"]))
    return clientes

def insertar_cliente():
    numero_documento:str=input("Ingrese el numero de docuemto del cliente: ")
    razon_social:str=input("Ingrese la razon social del cliente: ")
    direccion:str=input("Ingrese la direccion del cliente: ")
    telefono:str=input("Ingrese telefono del cliente: ")
    clientes.append(Cliente(numero_documento,razon_social,direccion,telefono))
    return clientes

def listar_clientes():
    print("-----------------------*")
    print("------LISTA DE CLIENTES -------*-")
    print("-----------------------*")
    print("|NUMERO DE DOC. | RAZON SOCIAL | DIRECCION | TELEFONO |")

    for cliente in clientes:
        print("----------------------------------------------------------------------")
        print(cliente.convertir_a_texto())
    return clientes

def buscar_cliente():
    numero_documento:str=input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            return cliente

def editar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento para editar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento==numero_documento:
            print(cliente.convertir_a_texto())
            cliente.razon_social=input("Ingrese nueva razon social del cliente: ")
            cliente.direccion=input("Ingrese nueva direcion del cliente: ")
            cliente.telefono=input("Ingrese nuevo telefono del cliente: ")
    listar_clientes()
    return clientes

def eliminar_cliente():
    listar_clientes()
    numero_documento:str=input("Ingrese el numero de documento del cliente para eliminar: ")
    for indice, cliente in enumerate(clientes):
        if cliente.numero_documento==numero_documento:
            clientes.pop(indice)
    listar_clientes()
    return clientes

# CRUD PRODUCTO

data_productos:list=[{"codigo":"8804", "nombre":"Cámara de seguridad", "precio":150.00},
{"codigo":"8805", "nombre":"Auriculares inalámbricos", "precio":50.00},
{"codigo":"8806", "nombre":"Cargador portátil", "precio":20.00},
{"codigo":"8807", "nombre":"Altavoz Bluetooth", "precio":40.00},
{"codigo":"8808", "nombre":"Reloj inteligente", "precio":100.00},
{"codigo":"8809", "nombre":"Router Wi-Fi", "precio":60.00},
{"codigo":"8810", "nombre":"Impresora multifuncional", "precio":120.00},
{"codigo":"8811", "nombre":"Teclado gaming", "precio":80.00},
{"codigo":"8812", "nombre":"Mouse inalámbrico", "precio":25.00},
{"codigo":"8813", "nombre":"Disco duro externo", "precio":70.00},
{"codigo":"8814", "nombre":"Cable HDMI", "precio":15.00},
{"codigo":"8815", "nombre":"Batería recargable", "precio":35.00},
{"codigo":"8816", "nombre":"Lápiz para tablet", "precio":30.00},
{"codigo":"8817", "nombre":"Soporte para celular", "precio":10.00},
{"codigo":"8818", "nombre":"Memoria USB", "precio":20.00},
{"codigo":"8819", "nombre":"Tablet Android", "precio":200.00},
{"codigo":"8820", "nombre":"Monitor de computadora", "precio":150.00},
{"codigo":"8821", "nombre":"Cámara deportiva", "precio":80.00},
{"codigo":"8822", "nombre":"Estabilizador de video", "precio":90.00},
{"codigo":"8823", "nombre":"Adaptador Bluetooth", "precio":15.00},
{"codigo":"8824", "nombre":"Micrófono USB", "precio":50.00},
{"codigo":"8825", "nombre":"Tarjeta de memoria SD", "precio":30.00},
{"codigo":"8826", "nombre":"Pendrive", "precio":15.00},
{"codigo":"8827", "nombre":"Teclado inalámbrico", "precio":40.00},
{"codigo":"8828", "nombre":"Mouse gamer", "precio":30.00},
{"codigo":"8829", "nombre":"Cable de carga USB-C", "precio":10.00},
{"codigo":"8830", "nombre":"Base de carga inalámbrica", "precio":25.00},]

productos:Producto = []
def cargar_datos_productos():
    for data in data_productos:
        productos.append(Producto(data["codigo"],
                                data["nombre"],
                                data["precio"]))
    return productos

def insertar_producto():
    codigo:str=input("Ingrese codigo del producto: ")
    nombre:str=input("Ingrese nombre del producto: ")
    precio:str=input("Ingrese precio del producto: ")
    productos.append(Producto(codigo,nombre,precio))
    return productos

def listar_productos():
    for producto in productos:
        print(producto.convertir_a_texto())
    return productos

def buscar_producto():
    codigo:str=input("Ingrese codigo del producto para buscar producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            return producto

def editar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para editar producto: ")
    for producto in productos:
        if producto.codigo==codigo:
            print(producto.convertir_a_texto())
            producto.nombre=input("Ingrese nuevo nombre del producto: ")
            producto.precio=float(input("Ingrese nuevo precio del producto: "))
           
    listar_productos()
    return productos

def eliminar_producto():
    listar_productos()
    codigo:str=input("Ingrese codigo del producto para eliminar producto: ")
    for indice, producto in enumerate(productos):
        if producto.codigo==codigo:
            productos.pop(indice)
    listar_productos()
    return productos

# CRUD VENTA
ventas:Venta=[]
venta_detalles:VentaDetalle=[]
def agregar_productos():
    producto:Producto=buscar_producto()
    cantidad:float=float(input("Ingrese la cantidad del producto: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,
                                       producto.codigo,
                                       producto.nombre,
                                       cantidad,
                                       producto.precio))
    return venta_detalles


def insertar_venta():
    cliente:Cliente=buscar_cliente()
    continuar_venta:bool=True
    while continuar_venta:
        opcion:str=input("1: para agregar producto, 2 para guargar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_venta=False
    total:float=0
    for venta_detalle in venta_detalles:
        total=total+venta_detalle.total
    ventas.append(Venta(len(ventas)+1,cliente,venta_detalles,total))
    return ventas
def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
    return ventas
        
def buscar_venta():
    numero: int = int(input("Ingrese el número de la venta para buscar: "))
    for venta in ventas:
        if venta.numero == numero:
            print("-----------FACTURA--------")
            print("-----------CLIENTE--------")
            print(venta.convertir_a_texto())
            print("================================")
            for venta_detalle in venta.detalle:
                print(venta_detalle.convertir_a_texto())
            exportar_boleta(venta)  # Exportar la boleta en formato PDF
            return venta


def menu_texto():
    
    print("===============MENU===========")
    print("=========CRUD CLIENTE========")
    print(obtener_fecha_actual())
    print("1: para Insertar Cliente")
    print("2: para listar Cliente")
    print("3: para Buscar Cliente")
    print("4: para Editar Cliente")
    print("5: para Elimiar Cliente")
    print("=========CRUD PRODUCTO========")
    print("6: para Insertar Producto")
    print("7: para listar Producto")
    print("8: para Buscar Producto")
    print("9: para Editar Producto")
    print("10: para Elimiar Producto")

    print("=========CRUD VENTA========")
    print("11: para Insertar Venta")
    print("12: para Listar Venta")
    print("13: para buscar Venta")
    
    print("30: para terminar")

def menu():
    continuar:bool=True
    while continuar:
        menu_texto()
        opcion:str=input("Ingrese la opcion: ")
        match opcion:
            case "1":
                insertar_cliente()
            case "2":
                listar_clientes()
            case "3":
                buscar_cliente() 
            case "4":
                editar_cliente()   
            case "5":
                eliminar_cliente() 
            case "6":
                insertar_producto()
            case "7":
                listar_productos()
            case "8":
                buscar_producto() 
            case "9":
                editar_producto()   
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta() 
            case "30":
                continuar=False    


def main():
    cargar_datos_clientes()
    cargar_datos_productos()
    menu()
    print("iniciando programna")
    return True
if __name__=='__main__':
    main()

