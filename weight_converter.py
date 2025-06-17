



print("Weight Converter")

weight = float(input("Enter your weight: "))

unit = input("Convert to Pounds or Kilograms? [k | l]: ")

if unit.lower() == 'k':
    print("Pounds to Kilograms")
    weight = weight * 0.453
    unit = "lbs"
    
elif unit.lower() == 'l':
    print("Kilograms to Pounds")
    weight = weight / 0.453
    unit = "kgs"
    
else:
    print("Invalid Input")
    
print(f"Converted: {weight} {unit} ")