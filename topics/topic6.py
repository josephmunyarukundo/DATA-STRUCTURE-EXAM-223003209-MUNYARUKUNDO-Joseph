
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

    def find_node(self, name):
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_node(name)
            if found:
                return found
        return None


def build_inventory_tree():
    root = TreeNode("Electronics")
    
    
    computers = TreeNode("Computers")
    phones = TreeNode("Phones")
    accessories = TreeNode("Accessories")
    
    root.add_child(computers)
    root.add_child(phones)
    root.add_child(accessories)
    
    
    computers.add_child(TreeNode("Laptops"))
    computers.add_child(TreeNode("Desktops"))
    
    phones.add_child(TreeNode("Smartphones"))
    phones.add_child(TreeNode("Feature Phones"))
    
    accessories.add_child(TreeNode("Chargers"))
    accessories.add_child(TreeNode("Headphones"))
    
    return root


def display_menu():
    print("\nInventory Control System - Hierarchical Data")
    print("1. Display the Tree Structure")
    print("2. Add a New Node")
    print("3. Exit")


def add_node_to_tree(root):
    parent_name = input("Enter the name of the parent node: ")
    parent_node = root.find_node(parent_name)
    
    if not parent_node:
        print(f"Parent node '{parent_name}' not found.")
        return
    
    new_node_name = input("Enter the name of the new node: ")
    new_node = TreeNode(new_node_name)
    parent_node.add_child(new_node)
    print(f"Node '{new_node_name}' added under '{parent_name}'.")

def main():
    inventory_tree = build_inventory_tree()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            inventory_tree.display()
        elif choice == "2":
            add_node_to_tree(inventory_tree)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
