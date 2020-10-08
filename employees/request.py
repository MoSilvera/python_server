import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "firstName": "Mo",
        "lastName": "Silvera",
        "locationId": 2
    },
    {
        "id": 2,
        "firstName": "Steve",
        "lastName": "Brownlee",
        "locationId": 1
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.name,
            e.address,
            e.location_id,
            e.id
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['name'], row['address'], row['location_id'], row['id'])

            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employee(id):
   with sqlite3.connect("./kennel.db") as conn:
       conn.row_factory = sqlite3.Row

       db_cursor = conn.cursor()

       db_cursor.execute("""
       SELECT 
        e.name,
        e.address,
        e.location_id,
        e.id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))
       data = db_cursor.fetchone()

       employee = Employee(data['name'], data['address'], data['location_id'], data['id'])

       return json.dumps(employee.__dict__)

def get_employee_by_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            e.name,
            e.address,
            e.location_id,
            e.id
            FROM employee e
            WHERE e.location_id = ?
            """, ( id, ))
        data = db_cursor.fetchone()

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset: 
             employee = Employee(row['name'], row['address'], row['location_id'], row['id'])
             employees.append(employee.__dict__)

        return json.dumps(employees)

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1 

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, employee):

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = employee
        break
