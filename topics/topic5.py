class InventoryControlSystem:
    def __init__(self):
        self.inventory = []  

    def add_item(self, item_id, description, quantity, price):
        
        
        for item in self.inventory:
            if item['item_id'] == item_id:
                print(f"Item ID {item_id} already exists in the inventory.")
                return

        
        self.inventory.append({
            'item_id': item_id,
            'description': description,
            'quantity': quantity,
            'price': price
        })
        print(f"Item {description} added successfully.")

    def update_item(self, item_id, quantity=None, price=None):
     
        for item in self.inventory:
            if item['item_id'] == item_id:
                if quantity is not None:
                    item['quantity'] = quantity
                if price is not None:
                    item['price'] = price
                print(f"Item ID {item_id} updated successfully.")
                return
        print(f"Item ID {item_id} not found in the inventory.")

    def remove_item(self, item_id):
        
        for i, item in enumerate(self.inventory):
            if item['item_id'] == item_id:
                self.inventory.pop(i)
                print(f"Item ID {item_id} removed successfully.")
                return
        print(f"Item ID {item_id} not found in the inventory.")

    def display_inventory(self):
        
        if not self.inventory:
            print("The inventory is empty.")
            return

        print("\nCurrent Inventory:")
        print(f"{'ID':<10}{'Description':<25}{'Quantity':<10}{'Price':<10}")
        print("-" * 60)
        for item in self.inventory:
            print(f"{item['item_id']:<10}{item['description']:<25}{item['quantity']:<10}{item['price']:<10}")
        print("-" * 60)

    def total_value(self):
        """Calculate the total value of the inventory."""
        total = sum(item['quantity'] * item['price'] for item in self.inventory)
        print(f"\nTotal Inventory Value: ${total:.2f}")



def menu():
    inventory_system = InventoryControlSystem()

    while True:
        print("\n-- Inventory Control System --")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Show Total Inventory Value")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                description = input("Enter Item Description: ")
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                inventory_system.add_item(item_id, description, quantity, price)
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == "2":
            try:
                item_id = int(input("Enter Item ID to update: "))
                quantity = input("Enter new Quantity (leave blank to skip): ")
                price = input("Enter new Price (leave blank to skip): ")
                inventory_system.update_item(
                    item_id,
                    quantity=int(quantity) if quantity else None,
                    price=float(price) if price else None
                )
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to remove: "))
                inventory_system.remove_item(item_id)
            except ValueError:
                print("Invalid input. Please enter a valid Item ID.")

        elif choice == "4":
            inventory_system.display_inventory()

        elif choice == "5":
            inventory_system.total_value()

        elif choice == "6":
            print("Exiting the Inventory Control System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")



menu()
