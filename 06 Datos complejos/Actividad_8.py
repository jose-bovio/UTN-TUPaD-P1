stock_productos = {"zapatillas": 10, "buzos": 8, "pantalones": 11}

print("Productos Disponibles:", list(stock_productos.keys()))

# Consultar producto
producto = input("Ingrese el producto que querés consultar o actualizar: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    
    agregar = input("¿Deseás agregar unidades nuevas al stock? (si/no): ").lower()
    if agregar == "si":
        cantidad = int(input("¿Cuántas unidades deseas agregar? "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"El producto '{producto}' no existe en el stock.")
    agregar_nuevo = input("¿Querés agregar este nuevo producto? (si/no): ").lower()
    if agregar_nuevo == "si":
        cantidad = int(input("¿Cuántas unidades tiene? "))
        stock_productos[producto] = cantidad
        print(f"'{producto}' fue agregado al stock con {cantidad} unidades.")

# Mostrar stock final
print("\nStock final:")
for prod, cant in stock_productos.items():
    print(f"{prod}: {cant} unidades")
