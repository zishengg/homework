def calculate_diameter(radius):
    return 2 * radius

def calculate_circumference (radius):
    pi = 3.14159
    return 2 * pi * radius

def calculate_area(radius):
    pi = 3.14159
    return pi * radius **2


def display_menu():
    print('MENU')
    print('1. Calulate Diamater')
    print('2. Calulate Circumference')
    print('3. Calulate Area')
    
def function():
    display_menu()
    choice = int(input('Please enter the option number'))

    if choice == 1:
        try:   
            radius = float(input("Enter radius"))
            diameter = calculate_diameter(radius)
            print ('The diamater of the circle is', diameter)
        
        except ValueError:
            print('error')

    elif choice == 2:
        try: 
            radius = float(input('Enter radius'))
            circumference = calculate_circumference(radius)
            print('The circumeference is', circumference)
        
        except ValueError:
            print('Error')

    elif choice == 3:
        try:
            radius = float(input('Enter radius'))
            area = calculate_area(radius)
            print('The area is', area)
        except ValueError:
            print('Error')

    else:
        print('Error')


