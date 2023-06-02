
GroceryList = [[10000, 'Milk, 1L', 'Dairy', 'Box', 7.00, 30, 5],
    [20000, 'Beef 200g' , 'Freezer', 'Pack', 20.00, 10, 5 ],
    [30000, 'Apple', 'Fruits','Pieces', 2.00, 50, 30],
    [32000, 'Fruits','Pieces', 2.50, 23, 30]]

# universal input by Mel
def UserInput():
    Item_Code = int(input("Please enter the item code: "))
    Name = input("Please enter the item name: ")
    Category = input("Please enter the item's category: ")
    Unit = input("Please enter a measurement unit: ")
    Price = float(input("Please enter selling price: "))
    Quantity = int(input("Please enter the stock quantity: "))
    Min_Quantity = int(input("Please enter the mininum quantity: "))
    return Item_Code, Name, Category, Unit, Price, Quantity, Min_Quantity


# Insert new item by JK
def AppendFile():
    new_data = []
    ItemCode = int(input("Please enter the item code: "))
    ItemName = input("Please enter the item name: ")
    ItemCtgy = input("Please enter the item's category: ")
    ItemUnit = input("Please enter a measurement unit: ")
    ItemPrice = float(input("Please enter selling price: "))
    ItemQuant = int(input("Please enter the stock quantity: "))
    ItemMin = int(input("Please enter the mininum quantity: "))
    new_data.append(ItemCode)
    new_data.append(ItemName)
    new_data.append(ItemCtgy)
    new_data.append(ItemUnit)
    new_data.append(ItemPrice)
    new_data.append(ItemQuant)
    new_data.append(ItemMin)
    GroceryList.append(new_data)
    write_to_file()

def write_to_file():
    with open('redoList.txt','w') as file:
        for List in GroceryList:
            for data in List:
                file.write(str(data))
                file.write('\t')
            file.write('\n')



# Update item by Scott
def ApplyUpdate(item_list, item_code, new_details):
    for item in item_list:
        if item[0] == item_code:
            item[0:] = new_details


    with open('redoList.txt', 'w') as file:
        for List in GroceryList:
            file.write(str(List))
            file.write('\n')

def InsertUpdate():
    select_item = int(input("Enter the item code for the list you wish to update: "))
    for Grocery in GroceryList:
        if select_item in GroceryList:
            print(Grocery)
    new_details = UserInput()
    ApplyUpdate(GroceryList, select_item, new_details)



# Delete Item by KuZi
def delete_item():
    DeleteCode = int(input("Enter the item code for the list you wish to remove: "))
    for item in GroceryList:
        if item[0] == DeleteCode:
            print(item)
            delete_confirmation = input("Are you sure?\tY/N: ")
            if delete_confirmation == "Y":
                GroceryList.remove(item)
                print('Item has been deleted from the inventory.')
            elif delete_confirmation == "N":
                print("Removal cancelled")

    with open('redoList.txt', 'w') as file:
        for List in GroceryList:
            file.write(str(List))
            file.write('\n')


# Stock Taking by YJ
def stock_taking():
    userinput = int(input('Enter the item code for the item you wish to check: '))
    for item in GroceryList:
        if userinput == item[0]:
            print(item)
            print(item[-2], item[-4], 'of', item[1], 'in stock')


# Show Understock by Mel
def ShowUnderstock():
    for item in GroceryList:
        if item[-1] > item[-2]:
            print(item[1], 'is understocked!')
            print('only', item[-2], 'in stock.')



# Stock Replenishment by KuZi | should be good
def stock_replenishment(inventory):
    InputCode = int(input("Enter the item code of the item you wish to replenish: "))
    for item in inventory:
        if InputCode == item[0]:
            print(f"Quantity for item {item[0]} - {item[1]}: {item[-2]}")
            ReplenishQuant = int(input("How much would you like to replenish?: "))
            item[-2] += ReplenishQuant
            replenished = item[-2]
            print("Stock replenished.")
            print(f"Quantity for item {item[0]} - {item[1]}: {item[-2]}")


    with open('redoList.txt', 'w') as file:
        for List in GroceryList:
            file.write(str(List))
            file.write('\n')



# search: description by Scott | kinda good
def search_item_by_description(item_list):
    search_description = input("Enter item description to search: ")
    for item in item_list:
        if item[1] == search_description:
            print(item)


# Search: item code range by JK | ALL GOOD NOW
def search_code_range():
    Min_range = int(input('Please enter the minimum code range: '))
    Max_range = int(input('Please enter the maximum code range: '))
    for item in GroceryList:
        Item_Code = item[0]
        if Item_Code > Min_range and Item_Code < Max_range:
            print(item)

# Search: Category by JK | horrible name choice for variables
def search_categories():
    Search_category = input("Please type a category: ")
    for item in GroceryList:
        Item_Category = item[2]
        if Search_category == Item_Category:
            print(item)


# Search: Price by Mel
def PriceSearch():
    MinPrice = int(input("enter the min price search range: "))
    MaxPrice = int(input("enter the max price search range: "))

    for grocery in GroceryList:
        price = grocery[-3]
        if price > MinPrice and price < MaxPrice:
                print(grocery)



# menu loop system by Mel
def ContTerm():
    print('Do you want to continue?\n‘0’ to Continue \t‘-1’ to Terminate')
    CTinput = int(input("Enter your choice: "))
    if CTinput == 0:
        MenuSystem()
    elif CTinput == -1:
        quit()


# ADDITIONAL | views the entire list by Mel
def ViewList():
    f = open("redoList.txt", "r")
    print(f.read())



# reads the text file to load in the masterlist
def LoadLastSave():
    f = open("redoList.txt", "r")
    for lists in f:
        SaveList = []
        data = lists.strip().split("\t")
        SaveList.append(int(data[0]))
        SaveList.append(data[1])
        SaveList.append(data[2])
        SaveList.append(data[3])
        SaveList.append(float(data[4]))
        SaveList.append(int(data[5]))
        SaveList.append(int(data[6]))
        GroceryList.append(SaveList)

# menu by Mel
def MenuSystem():
    print("Welcome to the Grocery Inventory System!!")
    print('\t1. Insert New item\n\t2. Update Item\n\t3. Delete Item\n\t4. View List')
    print('\t5. Stock Taking\n\t6. View Replenish Item\n\t7. Replenish Stock\n\t8. Search Inventory')
    print('\t0. Exit')
    MenuInput = int(input('Please select a function: '))
    if MenuInput == 1:
        AppendFile()
        ContTerm()
    elif MenuInput == 2:
        InsertUpdate()
        ContTerm()
    elif MenuInput == 3:
        delete_item()
        ContTerm()
    elif MenuInput == 4:
        ViewList()
        ContTerm()
    elif MenuInput == 5:
        stock_taking()
        ContTerm()
    elif MenuInput == 6:
        ShowUnderstock()
        ContTerm()
    elif MenuInput == 7:
        stock_replenishment(GroceryList)
        ContTerm()
    elif MenuInput == 8:
        print("\t1. by Item Name\n\t2. by Item Code\n\t3. by Category\n\t4. by Price Range")
        SearchInput = int(input("Choose a search function: "))
        if SearchInput == 1:
            search_item_by_description(GroceryList)
            ContTerm()
        elif SearchInput == 2:
            search_code_range()
            ContTerm()
        elif SearchInput == 3:
            search_categories()
            ContTerm()
        elif SearchInput == 4:
            PriceSearch()
            ContTerm()
    elif MenuInput ==0:
        quit()

LoadLastSave()
MenuSystem()
