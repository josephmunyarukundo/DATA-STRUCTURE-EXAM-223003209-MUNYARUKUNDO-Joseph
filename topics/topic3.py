class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
       
        self.items.append(item)

    def dequeue(self):
        
        if not self.is_empty():
            return self.items.pop(0)  
        else:
            print("Queue is empty.")
            return None

    def size(self):
        
        return len(self.items)

    def peek(self):
        
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty.")
            return None

    def display(self):
        
        if not self.is_empty():
            print("Queue contents:", self.items)
        else:
            print("Queue is empty.")


def menu():
    inventory_queue = Queue()
    while True:
        print("\n-- Inventory Queue System --")
        print("1. Add item to the queue (Enqueue)")
        print("2. Process the first item in the queue (Dequeue)")
        print("3. View the first item in the queue (Peek)")
        print("4. Display all items in the queue")
        print("5. Check the queue size")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            
            if choice == 1:
                item = input("Enter the item to add to the queue: ")
                inventory_queue.enqueue(item)
                print(f"Item '{item}' added to the queue.")
                
            elif choice == 2:
                processed_item = inventory_queue.dequeue()
                if processed_item:
                    print(f"Processing item: {processed_item}")
                
            elif choice == 3:
                first_item = inventory_queue.peek()
                if first_item:
                    print(f"Next item to process: {first_item}")
                
            elif choice == 4:
                inventory_queue.display()
                
            elif choice == 5:
                print(f"Queue size: {inventory_queue.size()}")
                
            elif choice == 6:
                print("Exiting Inventory Queue System.")
                break
                
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


menu()
