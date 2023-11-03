# customer_module.py

# Initialize an empty list to store customer records.
customers = []

# Function to add a new customer to the program.
def add_customer(customer_name, customer_postcode='', customer_phone=''):
    # Generate a unique customer ID based on the number of existing customers.
    customer_id = len(customers) + 1

    # Create a customer dictionary and add it to the list of customers.
    customer = {
        'customer_id': customer_id,
        'customer_name': customer_name,
        'customer_postcode': customer_postcode,
        'customer_phone': customer_phone
    }
    customers.append(customer)

    return customer_id  # Return the auto-generated customer ID.

# Function to search for customers using a search string.
def search_customers(search_string):
    matching_customers = []
    search_string = search_string.lower()  # Convert to lowercase for case-insensitive search.

    for customer in customers:
        # Check if the search string is found in any customer details.
        if search_string in str(customer['customer_id']).lower() \
            or search_string in customer['customer_name'].lower() \
            or search_string in str(customer['customer_postcode']).lower() \
            or search_string in str(customer['customer_phone']).lower():
            matching_customers.append(customer)

    return matching_customers

# Function to delete a customer with a given customer ID and their related transactions.
def delete_customer(customer_id):
    for customer in customers:
        if customer['customer_id'] == customer_id:
            customers.remove(customer)
            return True  # Customer deleted successfully.
    return False  # Customer not found.

# Other customer-related functions can be added as needed.

