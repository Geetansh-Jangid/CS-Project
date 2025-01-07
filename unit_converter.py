def unit_converter():
    def display_menu():
        print("\n=== Unit Converter ===")
        print("1. Length Conversion (meters <-> kilometers, inches <-> centimeters)")
        print("2. Weight Conversion (kilograms <-> pounds)")
        print("3. Temperature Conversion (Celsius <-> Fahrenheit)")
        print("4. Exit")

    def length_conversion():
        print("\n[Length Conversion]")
        print("1. Meters to Kilometers")
        print("2. Kilometers to Meters")
        print("3. Inches to Centimeters")
        print("4. Centimeters to Inches")
        choice = input("Enter your choice: ")
        value = float(input("Enter the value to convert: "))

        if choice == '1':
            print(f"{value} meters = {value / 1000} kilometers")
        elif choice == '2':
            print(f"{value} kilometers = {value * 1000} meters")
        elif choice == '3':
            print(f"{value} inches = {value * 2.54} centimeters")
        elif choice == '4':
            print(f"{value} centimeters = {value / 2.54} inches")
        else:
            print("Invalid choice!")

    def weight_conversion():
        print("\n[Weight Conversion]")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        choice = input("Enter your choice: ")
        value = float(input("Enter the value to convert: "))

        if choice == '1':
            print(f"{value} kilograms = {value * 2.20462} pounds")
        elif choice == '2':
            print(f"{value} pounds = {value / 2.20462} kilograms")
        else:
            print("Invalid choice!")

    def temperature_conversion():
        print("\n[Temperature Conversion]")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = input("Enter your choice: ")
        value = float(input("Enter the temperature to convert: "))

        if choice == '1':
            print(f"{value}°C = {(value * 9/5) + 32}°F")
        elif choice == '2':
            print(f"{value}°F = {(value - 32) * 5/9}°C")
        else:
            print("Invalid choice!")

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            length_conversion()
        elif choice == '2':
            weight_conversion()
        elif choice == '3':
            temperature_conversion()
        elif choice == '4':
            print("Exiting Unit Converter.")
            break
        else:
            print("Invalid choice. Please try again!")