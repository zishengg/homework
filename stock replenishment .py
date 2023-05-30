def delete_item():
    DeleteCode = int(input("Enter the item code for the list you wish to remove: "))
    for item in GroceryList:
        if DeleteCode in item:
            delete_confirmation = input("Are you sure?\tYes/No: ")
            if delete_confirmation == "Yes":
                GroceryList.remove(item)
                print('Item has been deleted from the inventory.')
            if delete_confirmation == "No":
                print("Removal cancelled")


delete_item()
print(GroceryList)


def stock_replenishment(inventory, item_code, quantity):
    for item in inventory:
        if item_code == item['code']:
            print(f"Quantity for item {item_code}: {item['quantity']}")
            item['quantity']+= quantity
        
        else:
            print("Item cannot be found from inventory.")

            