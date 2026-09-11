"""Smart Inventory Auditor for INF1103 Lab 2."""


def main():
    """Collect delivery quantities until the operator quits or capacity is exceeded."""
    inventory = 0
    failed_entries = 0

    while True:
        stock = input("Enter stock quantity (or 'quit'): ").strip()

        if stock.lower() == "quit":
            break

        if stock.startswith("-") and stock[1:].isdigit():
            print("Error: negative entries are not allowed.")
            failed_entries += 1
            continue

        if not stock.isdigit():
            print(f"Error: '{stock}' is not a valid whole number. Please try again.")
            failed_entries += 1
            continue

        quantity = int(stock)
        inventory += quantity
        print(f"Current Total Inventory: {inventory}")

        if inventory > 500:
            print("Overstock alert: inventory has exceeded 500 units.")
            break

    print(f"Total Units Processed: {inventory}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")


if __name__ == "__main__":
    main()
