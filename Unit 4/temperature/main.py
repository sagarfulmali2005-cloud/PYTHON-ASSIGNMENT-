from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius

print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit.convert(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius.convert(f))

else:
    print("Invalid choice!")