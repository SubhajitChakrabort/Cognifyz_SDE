def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter")

    while True:
        print("\nPlease choose the conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is {fahrenheit}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is {celsius}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            print("Exiting the Temperature Converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
