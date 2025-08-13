def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
              
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

print(calculate_discount(price, discount_percent))
              
              
              
              
              
              
              
              
              
              
     