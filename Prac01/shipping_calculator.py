number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    number_of_items = int(input("Number of items: "))
shipping_cost = 0.0
for i in range(number_of_items):
    shipping_cost += float(input("Price of item: "))
if shipping_cost > 100:
    shipping_cost = shipping_cost * 0.9
print("Total price for", number_of_items, "items is $ {:.2f}".format(shipping_cost))
