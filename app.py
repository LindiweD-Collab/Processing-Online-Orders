class Order:  
    def __init__(self, order_id, item, quantity):  
        self.order_id = order_id  
        self.item = item  
        self.quantity = quantity  

def process_order(order):  
    # Simulate order processing (e.g., checking inventory)  
    print(f"Processing Order ID: {order.order_id}")  
    print(f"Item: {order.item}, Quantity: {order.quantity}")  
    # Here you would add logic for payment, inventory updates, etc.  

# Example usage  
new_order = Order(order_id=101, item='Laptop', quantity=1)  
process_order(new_order)
