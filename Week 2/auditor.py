inventory = 0
failed_entries = 0
while True:
    try:
        stock = input("Enter stock quantity (or 'quit'): ")
        if stock.lower() == "quit":
            break
        if not stock.isdigit():
             print(f"Error: '{stock}' is not a valid whole number. Please try again.")
             failed_entries += 1
             continue
        quantity = int(stock)

        if quantity < 0:
            print("Error! Negative entry is not allowed!")
            failed_entries += 1
            continue

        inventory = inventory + quantity
        print(f"Current Total Inventory: {inventory}")

        if inventory > 500:
            print("Just exceeded 500 ! ")
            break


    except ValueError:
         print("Error, try again! ")


print(f"Total Units Processed: {inventory}")
print(f"Number of Failed entries: {failed_entries}")