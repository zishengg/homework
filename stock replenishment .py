def delete_item(inventory, item_code):
    for item in inventory:
        if item_code == item['code']:
            inventory.remove(item)
            print('Item has been deleted from the inventory.')
            
        else:
            print("Item cannot be found from inventory.")

def stock_replenishment(inventory, item_code, quantity):
    for item in inventory:
        if item_code == item['code']:
            print(f"Quantity for item {item_code}: {item['quantity']}")
            item['quantity']+= quantity
        
        else:
            print("Item cannot be found from inventory.")
            
            