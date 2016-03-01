def addToInventory(inventory, addedItems):
    for val in addedItems:
        inventory.setdefault(val, 0)
        inventory[val] = inventory[val] + 1
    return inventory

def displayInventory(inv):
    total = 0
    for val in inv:
        print inv[val], val
        total += inv[val]
    print "\nTotal number of items " + str(total)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
