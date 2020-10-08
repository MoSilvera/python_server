import sqlite3
import json
from models import Customer

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
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.name,
            c.address,
            c.email,
            c.password,
            c.id
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['name'], row['address'], row['email'], row['password'], row['id'])
            customers.append(customer.__dict__)

        return json.dumps(customers)



def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.name,
            c.address,
            c.email,
            c.password,
            c.id
        FROM customer c
        WHERE c.id = ? 
        """, (id,))

        data = db_cursor.fetchone()

        customer = Customer(data['name'], data['address'], data['email'], data['password'], data['id'])

        return json.dumps(customer.__dict__)


def get_customer_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['name'], data['address'], data['email'],
                            data['password'], data['id'])

        # Return the JSON serialized Customer object
        return json.dumps(customer.__dict__)


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


def update_customer(id, newCustomer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = newCustomer
        break