CUSTOMERS = [
    {
        "id": 1,
        "firstName": "Mike",
        "lastName": "Wizotsky"
       
    },
    {
        "id": 2,
        "firstName": "Dave",
        "lastName": "McDave"
        
    },
    {
        "id": 3,
        "firstName": "Sherman",
        "lastName": "Werman"
       
    },
    {
        "id": 4,
        "firstName": "Fake",
        "lastName": "Dude"
       
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):

    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
