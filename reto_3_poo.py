class MenuItem:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def itemprice(self):
            return self.price

class Beverage(MenuItem):
    def __init__(self, name, price, type_bebida):
        super().__init__(name, price)
        self.type_bebida = type_bebida

class Appetizer(MenuItem):
    def __init__ (self,name, price, type_aperitivo):
        super().__init__(name, price)

class MainCourse(MenuItem):
    def __init__(self, name, price, Type_pricipio):
        super().__init__(name, price)

class Dessert(MenuItem):
    def __init__(self, name, price, type_dessert):
        super().__init__(name, price)

class Order:
    def __init__(self):
        self.finalorder = []
        self.items = []

    def add (self):
            item_name = input("Ingresa el item del menu que quieras agregar a tu cuenta o 'no' para salir del programa: ").lower()
            if item_name in Menu:
                quantity = int(input(f"¿Cuántos {item_name} deseas ordenar?: "))
                self.finalorder.append((item_name, quantity))
                self.items.append((Menu[item_name], quantity))
            elif item_name == "no":
                quit()
            else:
                print(f"disculpa {item_name} no esta en el menu")
            quantity = input
                
            if item_name == "no":
                quit()
            while True:
                item_name = input("hay algo mas que quieras agregar o digita 'no' para terminar la orden: ")
                if item_name == "no":
                    break
                
                if item_name in Menu:
                    quantity = int(input(f"¿Cuántos {item_name} deseas ordenar?: "))
                    self.finalorder.append((item_name, quantity))
                    self.items.append((Menu[item_name], quantity))
                else:
                    print(f"disculpa {item_name} no esta en el menu")

    def show_final_order(self):
        print(f"su orden es: {self.finalorder}")
    
    def final_price(self):
        total = 0
        for final_item, quantity in self.items:
            if final_item == arepas_queso:
                discount = final_item.price * 0.5
                total += discount * quantity
            elif final_item == carne_asada:
                discount = final_item.price * 0.3
                total += discount * quantity
            elif final_item == brownie:  
                discount = final_item.price * 0.9
                total += discount * quantity      
            else:
                total += final_item.price * quantity
        return total
            
    
fanta = Beverage("Aanta", 4000, "soda")
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
    
O = Order()
O.add()
O.show_final_order()
O.final_price()

print (f"El precio final de tu cuenta seria de: ${O.final_price()} cop")

tip_cop = int(input("Cuanto de propina deseas agregar: "))

fprice = int(O.final_price()) + tip_cop
print (f"El precio final de tu cuenta seria de: ${fprice} cop")
