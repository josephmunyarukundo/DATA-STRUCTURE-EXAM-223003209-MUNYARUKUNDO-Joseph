class AVLNode:
    def __init__(self, key, details, quantity, price):
        self.key = key  
        self.details = details  
        self.quantity = quantity  
        self.price = price 
        self.height = 1 
        self.left = None  
        self.right = None  


class AVLTree:
    def __init__(self, max_orders):
        self.root = None
        self.max_orders = max_orders
        self.current_orders = 0

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, key, details, quantity, price):
        if not node:
            if self.current_orders < self.max_orders:
                self.current_orders += 1
                return AVLNode(key, details, quantity, price)
            else:
                print("Order limit reached. Cannot add more orders.")
                return node

        if key < node.key:
            node.left = self.insert(node.left, key, details, quantity, price)
        elif key > node.key:
            node.right = self.insert(node.right, key, details, quantity, price)
        else:
            print(f"Order ID {key} already exists. Skipping insertion.")
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, node, key):
        if not node:
            print(f"Order ID {key} not found. Cannot delete.")
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                self.current_orders -= 1
                return temp
            elif not node.right:
                temp = node.left
                node = None
                self.current_orders -= 1
                return temp

            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.details = temp.details
            node.quantity = temp.quantity
            node.price = temp.price
            node.right = self.delete(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def pre_order_traversal(self, node):
        if node:
            print(f"Order ID: {node.key}, Details: {node.details}, Quantity: {node.quantity}, Price: {node.price}")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def add_order(self, order_id, details, quantity, price):
        self.root = self.insert(self.root, order_id, details, quantity, price)

    def remove_order(self, order_id):
        self.root = self.delete(self.root, order_id)

    def display_orders(self):
        print("\nCurrent Orders (Pre-Order Traversal):")
        self.pre_order_traversal(self.root)
        print(f"Total orders: {self.current_orders}/{self.max_orders}")



def menu():
    max_orders = int(input("Enter the maximum number of orders: "))
    inventory = AVLTree(max_orders)

    while True:
        print("\n-- Inventory Control System --")
        print("1. Add Order")
        print("2. Remove Order")
        print("3. Display All Orders")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                order_id = int(input("Enter Order ID: "))
                details = input("Enter Order Details (Item Description): ")
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                inventory.add_order(order_id, details, quantity, price)
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == "2":
            try:
                order_id = int(input("Enter Order ID to remove: "))
                inventory.remove_order(order_id)
            except ValueError:
                print("Invalid input. Please enter a valid Order ID.")

        elif choice == "3":
            inventory.display_orders()

        elif choice == "4":
            print("Exiting the Inventory Control System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")



menu()
