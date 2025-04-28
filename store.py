
item = input("What would you like to buy?: ")
quantity = int(input("How many are you buying?: "))
price = float(input("Show me the price: "))
total = quantity * price

print("\nPurchase Details:")
print(f"Item: {item} = {quantity} x {price}") 
#print(quantity)
#print(price)
print(f"Your Total Purchase is: {total} Pesos")

