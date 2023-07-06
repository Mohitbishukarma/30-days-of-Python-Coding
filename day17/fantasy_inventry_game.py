import copy #to copy dict to new var

def displayInventory(inventory: dict):
    print("Inventory".center(25,"="))
    print("Item".ljust(15)+"Value".rjust(10))
    for item, value in inventory.items():
        print(item.ljust(15,'-')+str(value).rjust(10,"-"))
    print("")


def addToInventory(inventory: dict, items: list):
    newInventory = copy.copy(inventory)
    
    for each in items:
        newInventory.setdefault(each, 0)
        newInventory[each] += 1
    
    return newInventory

if __name__ == "__main__":

    
    my_inventory = {
        "gold coin":20,
        "rope": 2,
        "dagger": 3,
        "diamond": 5,
    }

    displayInventory(my_inventory)
    
    dragonLoot = ["gold coin", "rope", "drink", "rope", "gold coin", "diamond","gold coin"]

    updatedInventory = addToInventory(my_inventory, dragonLoot)


    displayInventory(updatedInventory)
    print("\n\nTHis is INitial var\n\n")
    displayInventory(my_inventory)
