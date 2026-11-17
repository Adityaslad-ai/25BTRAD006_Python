sales = {}

while True:
    print("\n===== SALES DATA ANALYZER =====")
    print("1. Add Product")
    print("2. Update Sales")
    print("3. Display Sales")
    print("4. Calculate Total Sales")
    print("5. Find Highest-Selling Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity sold: "))

        sales[name] = {
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully.")

    
    elif choice == "2":
        name = input("Enter product name: ")

        if name in sales:
            quantity = int(input("Enter additional quantity sold: "))
            sales[name]["quantity"] += quantity
            print("Sales updated successfully.")
        else:
            print("Product not found.")

    
    elif choice == "3":
        print("\n===== PRODUCT SALES =====")

        for name, data in sales.items():
            revenue = data["price"] * data["quantity"]

            print("Product:", name)
            print("Price: Rs.", data["price"])
            print("Quantity Sold:", data["quantity"])
            print("Revenue: Rs.", revenue)
            print("------------------------")

    
    elif choice == "4":
        total = 0

        for data in sales.values():
            total += data["price"] * data["quantity"]

        print("Total Sales: Rs.", total)

    
    
    elif choice == "5":
        if len(sales) == 0:
            print("No sales data available.")
        else:
            highest_product = max(
                sales,
                key=lambda x: sales[x]["quantity"]
            )

            print("Highest-Selling Product:", highest_product)
            print("Quantity Sold:",
                  sales[highest_product]["quantity"])

    
    elif choice == "6":
        print("Thank you for using Sales Data Analyzer!")
        break

    else:
        print("Invalid choice.")
