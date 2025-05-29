temp = float(input("Temperature: "))
unit = input("C or F: ")

if unit == "C":
    print(f"{temp}°C = {(temp * 9/5) + 32:}°F")
elif unit == "F":
    print(f"{temp}°F = {(temp - 32) * 5/9:}°C")
else:
    print("invalid")


