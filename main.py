def convert_length():
    print("\nLength Conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles:.2f} miles.")
    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km:.2f} kilometers.")
    else:
        print("Invalid option. Please choose 1 or 2.")

def convert_weight():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is equal to {pounds:.2f} pounds.")
    elif choice == "2":
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kg:.2f} kilograms.")
    else:
        print("Invalid option. Please choose 1 or 2.")

def convert_temperature():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid option. Please choose 1 or 2.")

def main():
    while True:
        print("\n--- Unit Converter Calculator ---")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Convert Temperature")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
