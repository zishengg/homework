import math

def calculate_diameter(radius):
    return 2 * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

def calculate_area(radius):
    return math.pi * radius ** 2

def display_menu():
    print('MENU')
    print('1. Calculate Diameter')
    print('2. Calculate Circumference')
    print('3. Calculate Area')

def main():
    display_menu()
    choice = int(input('Please enter the option number: '))

    if choice == 1:
        try:
            radius = float(input("Enter radius: "))
            diameter = calculate_diameter(radius)
            print('The diameter of the circle is', diameter)
        except ValueError:
            print('error')

    elif choice == 2:
        try:
            radius = float(input('Enter radius: '))
            circumference = calculate_circumference(radius)
            print('The circumference is', circumference)
        except ValueError:
            print('error')

    elif choice == 3:
        try:
            radius = float(input('Enter radius: '))
            area = calculate_area(radius)
            print('The area is', area)
        except ValueError:
            print('error')

    else:
        print('error')

main()
