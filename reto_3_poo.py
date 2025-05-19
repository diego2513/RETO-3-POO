#Para mostrar el Menu al usuario
def show_menu():
    print("+--------------------- MENÚ ---------------------+")
    print("|                   🥤 BEBIDAS                   |")
    print("|------------------------------------------------|")
    print(f"| Fanta          | ${fanta.price} | {fanta.type_bebida}                  |")
    print(f"| Agua           | ${agua.price} | {agua.type_bebida}                  |")
    print(f"| Vino           | ${vino.price} | {vino.type_bebida}              |")
    
    print("+------------------------------------------------+")
    print("|                🍽️ APERITIVOS                    |")
    print("|------------------------------------------------|")
    print(f"| Arepa con queso | ${arepas_queso.price} | {arepas_queso.type_aperitivo} |")
    print(f"| Palitos de queso| ${palitos_queso.price} | {palitos_queso.type_aperitivo} |")
    print(f"| Ensalada        | ${ensalada.price} | {ensalada.type_aperitivo}  |")

    print("+------------------------------------------------+")
    print("|            🍛 PLATOS PRINCIPALES               |")
    print("|------------------------------------------------|")
    print(f"| Perro caliente | ${perro_caliente.price} | {perro_caliente.type_principio} |")
    print(f"| Bandeja paisa  | ${bandeja_paisa.price} | {bandeja_paisa.type_principio}  |")
    print(f"| Carne de Res   | ${carne_asada.price} | {carne_asada.type_principio} |")

    print("+------------------------------------------------+")
    print("|                🍰 POSTRES                      |")
    print("|------------------------------------------------|")
    print(f"| Helado de fresa | ${helado.price} | {helado.type_dessert} |")
    print(f"| Brownie         | ${brownie.price} | {brownie.type_dessert} |")
    print(f"| Galleta         | ${galleta.price} | {galleta.type_dessert} |")

    print("+------------------------------------------------+")
#Para mostrar despedida
def goodbye():
    print("+------------------------------------------------+")
    print("|    🙌 GRACIAS POR VISITAR EL RESTAURANTE 🙌    |")
    print("+------------------------------------------------+")
#clase padre Menu_item
class MenuItem:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def itemprice(self):
            return self.price
#clase bebida
class Beverage(MenuItem):
    def __init__ (self, name, price, type_bebida):
        super().__init__(name, price)
        self.type_bebida = type_bebida
#clase aperitivo
class Appetizer(MenuItem):
    def __init__ (self, name, price, type_aperitivo):
        super().__init__(name, price)
        self.type_aperitivo = type_aperitivo
#clase plato principal
class MainCourse(MenuItem):
    def __init__(self, name, price, type_pricipio):
        super().__init__(name, price)
        self.type_principio = type_pricipio
#clase postre
class Dessert(MenuItem):
    def __init__(self, name, price, type_dessert):
        super().__init__(name, price)
        self.type_dessert = type_dessert

#clase para la orden
class Order:
    #Inicializar lista para usar despues en la orden
    def __init__(self):
        self.finalorder = []
    #el usuario hace la orden a traves de iteraciones
    def add (self):
            #primer item de la orden o slair del programa en caso de digitar "no"
            item_name = input("\nIngresa el item del menu que quieras agregar a tu cuenta o 'no' para salir del programa: ").lower()
            if item_name in Menu:
                quantity = int(input(f"\n¿Cuántos {item_name} deseas ordenar?: "))
                self.finalorder.append((item_name, quantity)) #tupla en "finalorder" para generar la orden
            elif item_name == "no":
                quit()
            else:
                print(f"\nDisculpa {item_name} no esta en el menu")
            quantity = input
                
            if item_name == "no":
                quit() #si "no", sale del programa
            while True:
                item_name = input("\nHay algo mas que quieras agregar o digita 'no' para terminar la orden: ")
                if item_name == "no":
                    break  #si "no" se rompe la iteracion
                
                if item_name in Menu:
                    quantity = int(input(f"¿Cuántos {item_name} deseas ordenar?: "))
                    self.finalorder.append((item_name, quantity)) #tupla en "finalorder" para generar la orden
                else:
                    print(f"disculpa {item_name} no esta en el menu")

    def show_final_order(self):
        print(f"su orden es: {self.finalorder}") #Imprime la orden 
    
    def final_price(self):
        total = 0
        for final_item, quantity in self.finalorder:
            final_item = Menu[final_item] #ya que final_item es solo una palabra no tiene atributos por lo que aqui se convierte en un item de "Menu"
            if final_item == arepas_queso:
                print("Se ha aplicado un 50% de descuento en arepas con queso")  
                discount = final_item.price * 0.5     #50 % off en arepas con queso
                 
            elif final_item == carne_asada:
                print("Se ha aplicado un 30% de descuento en carne asada") 
                discount = final_item.price * 0.7    #30% off si en carne asada
                total += discount * quantity
                  
            elif final_item == brownie:  
                print("Se ha aplicado un 90% de descuento en brownies")
                discount = final_item.price * 0.1    #90 % off en brownies
                total += discount * quantity        
            else:
                total += final_item.price * quantity  # si no incluye ninguno de los anteriores simplemente se pone el precio normal
        return total
            
#declaro los elementios del menu
fanta = Beverage("Fanta", 4000, "soda")
agua = Beverage("Agua", 2500, "agua")
vino = Beverage("Vino", 15000, "alcohol")
arepas_queso = Appetizer("Arepa con queso", 10000, "COLOMBIANO")
palitos_queso = Appetizer("Palitos de queso", 10000, "panaderia")
ensalada = Appetizer("Ensalada", 10000, "Fresco")
perro_caliente = MainCourse("Perro caliente", 12000, "Comida rapida")
bandeja_paisa = MainCourse("Bandeja paisa", 25000, "COLOMBIANO")
carne_asada = MainCourse("Carne de Res", 25000, "Proteina")
helado = Dessert("Helado de fresa", 6000, "Frio")
brownie = Dessert("Brownie", 7000, "Dulce")
galleta = Dessert("galleta", 4000, "Dulce")

#diccionario del menu
Menu = {
    "fanta": fanta,
    "agua": agua,
    "vino": vino,
    "arepa con queso": arepas_queso,
    "palitos de queso": palitos_queso,
    "ensalada": ensalada,
    "perro caliente": perro_caliente,
    "bandeja paisa": bandeja_paisa,
    "carne asada": carne_asada,
    "helado": helado,
    "brownie": brownie,
    "galleta": galleta,
}

show_menu()    
O = Order()
O.add()
O.show_final_order()
O.final_price()

print (f"El precio final de tu cuenta aplicando las promociones seria de: ${O.final_price()} cop")

tip_cop = int(input("Cuanto de propina deseas agregar: "))

fprice = int(O.final_price()) + tip_cop
print (f"El precio final de tu cuenta con propia incluida seria de: ${fprice} cop")

goodbye()
