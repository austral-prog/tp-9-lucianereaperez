def create_inventory(items):
    dictionary = dict()
    for element in items:
        if element not in dictionary: 
            dictionary[element] = 1
        elif element in dictionary:
            cantidad = dictionary[element]
            dictionary[element] = cantidad + 1
    return dictionary

def add_items(inventory, items):
    for element in items:
        if element not in inventory.keys(): 
            inventory[element] = 1
        elif element in inventory.keys():
            cantidad = inventory[element]
            inventory[element] = cantidad + 1
    return inventory

def decrement_items(inventory, items):
    for element in items:
        if element in inventory.keys() and inventory[element] != 0 :
            cantidad = inventory[element]
            inventory[element] = cantidad - 1
    return inventory
def remove_item(inventory, item):
    if item in inventory.keys():
        del inventory[item]
    return inventory
def list_inventory(inventory):
    new_inventario = []
    for key, value in inventory.items():
        if value > 0:
           new_inventario.append((key, value))
    return new_inventario
