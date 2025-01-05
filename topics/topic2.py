class Node:
    
    def __init__(self, product_id, product_name, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.next = None  


class SinglyLinkedList:
   
    def __init__(self):
        self.head = None  


    def add_item(self, product_id, product_name, quantity):
        
        new_node = Node(product_id, product_name, quantity)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node
        print(f"Item added: {product_name} (ID: {product_id}, Quantity: {quantity})")

    def remove_item(self, product_id):
        
        if not self.head:
            print("The inventory is empty.")
            return
        
       
        if self.head.product_id == product_id:
            print(f"Item removed: {self.head.product_name} (ID: {product_id})")
            self.head = self.head.next
            return

        
        current = self.head
        while current.next and current.next.product_id != product_id:
            current = current.next

        if current.next:  
            print(f"Item removed: {current.next.product_name} (ID: {product_id})")
            current.next = current.next.next
        else:
            print(f"Item with ID {product_id} not found.")

    def search_item(self, product_id):
        
        current = self.head
        while current:
            if current.product_id == product_id:
                print(f"Item found: {current.product_name} (ID: {product_id}, Quantity: {current.quantity})")
                return current
            current = current.next
        print(f"Item with ID {product_id} not found.")
        return None

    def update_item(self, product_id):
       
        item = self.search_item(product_id)
        if not item:
            print(f"Cannot update: Item with ID {product_id} not found.")
            return

        print(f"\nUpdating Item: {item.product_name} (ID: {product_id})")
        try:
            update_name = input("Update product name? (yes/no): ").strip().lower()
            if update_name == "yes":
                new_name = input("Enter new product name: ").strip()
                item.product_name = new_name
                print(f"Product name updated to: {new_name}")

            update_quantity = input("Update quantity? (yes/no): ").strip().lower()
            if update_quantity == "yes":
                new_quantity = int(input("Enter new quantity: "))
                item.quantity = new_quantity
                print(f"Quantity updated to: {new_quantity}")
        except ValueError:
            print("Invalid input. Update failed.")

    def display_inventory(self):
       
        if not self.head:
            print("The inventory is empty.")
            return
        current = self.head
        print("\nInventory:")
        while current:
            print(f"ID: {current.product_id}, Name: {current.product_name}, Quantity: {current.quantity}")
            current = current.next


def main():
    inventory = SinglyLinkedList()
    while True:
        print("\nInventory Control System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Display Inventory")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                product_id = int(input("Enter Product ID: "))
                product_name = input("Enter Product Name: ")
                quantity = int(input("Enter Quantity: "))
                inventory.add_item(product_id, product_name, quantity)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 2:
            try:
                product_id = int(input("Enter Product ID to remove: "))
                inventory.remove_item(product_id)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 3:
            try:
                product_id = int(input("Enter Product ID to search: "))
                inventory.search_item(product_id)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 4:
            try:
                product_id = int(input("Enter Product ID to update: "))
                inventory.update_item(product_id)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == 5:
            inventory.display_inventory()
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
