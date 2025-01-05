import heapq


class TreeNode:
    def __init__(self, name, priority=0):
        self.name = name
        self.priority = priority
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + f"{self.name} (Priority: {self.priority})")
        for child in self.children:
            child.display(level + 1)

    def flatten(self):
      
        nodes = [(self.priority, self.name)]
        for child in self.children:
            nodes.extend(child.flatten())
        return nodes


def build_inventory_tree():
    root = TreeNode("Electronics", 1)
    
    
    computers = TreeNode("Computers", 2)
    phones = TreeNode("Phones", 3)
    accessories = TreeNode("Accessories", 4)
    
    root.add_child(computers)
    root.add_child(phones)
    root.add_child(accessories)
    
    
    computers.add_child(TreeNode("Laptops", 6))
    computers.add_child(TreeNode("Desktops", 5))
    
    phones.add_child(TreeNode("Smartphones", 8))
    phones.add_child(TreeNode("Feature Phones", 7))
    
    accessories.add_child(TreeNode("Chargers", 10))
    accessories.add_child(TreeNode("Headphones", 9))
    
    return root


def heap_sort(flattened_data):
    
    heapq.heapify(flattened_data) 
    sorted_data = [heapq.heappop(flattened_data) for _ in range(len(flattened_data))]
    return sorted_data


def display_sorted_data(sorted_data):
    print("\nSorted Inventory (by Priority):")
    for priority, name in sorted_data:
        print(f"Priority: {priority}, Item: {name}")


def display_menu():
    print("\nInventory Control System - Sorted Data")
    print("1. Display the Tree Structure")
    print("2. Display Sorted Data by Priority")
    print("3. Exit")


def main():
    inventory_tree = build_inventory_tree()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            inventory_tree.display()
        elif choice == "2":
            flattened_data = inventory_tree.flatten()
            sorted_data = heap_sort(flattened_data)
            display_sorted_data(sorted_data)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
