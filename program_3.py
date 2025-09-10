def calculate_total_purchase():
    # A customer in a store is purchasing five items. 
    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: ")) 
    item3 = float(input("Enter price of item 3: ")) 
    item4 = float(input("Enter price of item 4: ")) 
    item5 = float(input("Enter price of item 5: "))  
    # Write a program that asks for each item, 
    Subtotal = item1 + item2 + item3 +item4 + item5
    # then displays the subtotal of the sale, 
    sales_tax = Subtotal * 0.07
    total = Subtotal + sales_tax
    # the amount of sales tax, and the total.  
    print("Subtotal: $", format(Subtotal, ".2f"), sep=" ")
    print("sales tax: $", format(sales_tax, ".2f"), sep=" ")
    print("Total: $", format(total, ".2f"), sep=" ")
    # Assume the sales tax is 7 percent.
calculate_total_purchase()